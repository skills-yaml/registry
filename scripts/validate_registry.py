#!/usr/bin/env python3
"""Validate registry package structure, provenance, dependencies, and immutability."""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import stat
import struct
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as error:  # pragma: no cover - exercised only on an invalid host
    raise SystemExit("PyYAML is required to validate the registry") from error


NAME_PATTERN = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
SEMVER_PATTERN = re.compile(
    r"(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)"
    r"(?:-((?:0|[1-9]\d*|[a-zA-Z-][0-9A-Za-z-]*)"
    r"(?:\.(?:0|[1-9]\d*|[a-zA-Z-][0-9A-Za-z-]*))*))?"
    r"(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?"
)
VERSION_DIR_PATTERN = re.compile(r"v(" + SEMVER_PATTERN.pattern + r")")
DEPENDENCY_PATTERN = re.compile(
    r"([a-z0-9]+(?:-[a-z0-9]+)*)/([a-z0-9]+(?:-[a-z0-9]+)*)@(" + SEMVER_PATTERN.pattern + r")"
)
REVISION_PATTERN = re.compile(r"[0-9a-f]{40}")
INTEGRITY_PATTERN = re.compile(r"sha256:[0-9a-f]{64}")
SOURCE_REPOSITORY = "https://github.com/skills-yaml/workspace.git"
WORKSPACE_METADATA = {
    "skm-version",
    "skm-source-repository",
    "skm-source-revision",
    "skm-source-path",
    "skm-source-integrity",
    "workspace-toolkit-version",
    "workspace-docs-compatibility",
    "minimum-skm-version",
    "skm-adapter-compatibility",
}
MAX_PACKAGE_FILES = 256
MAX_PACKAGE_BYTES = 10 * 1024 * 1024


class UniqueKeyLoader(yaml.SafeLoader):
    """Safe YAML loader that rejects ambiguous duplicate mapping keys."""


def _construct_mapping(loader: UniqueKeyLoader, node: yaml.MappingNode, deep: bool = False) -> dict[Any, Any]:
    mapping: dict[Any, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        try:
            duplicate = key in mapping
        except TypeError as error:
            raise ValueError("YAML mapping keys must be scalar") from error
        if duplicate:
            raise ValueError(f"duplicate YAML key: {key}")
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    _construct_mapping,
)


@dataclass(frozen=True)
class ReleasedSkill:
    namespace: str
    skill_id: str
    version: str
    path: Path
    metadata: dict[str, str]
    dependencies: tuple[str, ...]

    @property
    def coordinate(self) -> str:
        return f"{self.namespace}/{self.skill_id}@{self.version}"


def parse_yaml(text: str, context: str) -> dict[str, Any]:
    try:
        value = yaml.load(text, Loader=UniqueKeyLoader)
    except (yaml.YAMLError, ValueError) as error:
        raise ValueError(f"invalid YAML in {context}: {error}") from error
    if not isinstance(value, dict):
        raise ValueError(f"YAML in {context} must be a mapping")
    return value


def parse_frontmatter(path: Path) -> tuple[dict[str, Any], str, str]:
    try:
        content = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        raise ValueError(f"cannot read {path}: {error}") from error
    match = re.match(r"^---\n(?P<header>.*?)\n---(?P<body>\n.*|$)", content, re.DOTALL)
    if not match:
        raise ValueError(f"{path} must start with YAML frontmatter")
    return parse_yaml(match.group("header"), str(path)), match.group("header"), match.group("body")


def semver_key(version: str) -> tuple[Any, ...]:
    match = SEMVER_PATTERN.fullmatch(version)
    if not match:
        raise ValueError(f"invalid semantic version: {version}")
    prerelease = match.group(4)
    if prerelease is None:
        release_key: tuple[Any, ...] = (1,)
    else:
        identifiers = tuple(
            (0, int(item)) if item.isdigit() else (1, item)
            for item in prerelease.split(".")
        )
        release_key = (0, *identifiers)
    return int(match.group(1)), int(match.group(2)), int(match.group(3)), release_key


def source_tree_hash(version_path: Path, skill_header: str, skill_body: str) -> str:
    marker = "\nmetadata:\n"
    if marker not in skill_header:
        raise ValueError("generated Workspace SKILL.md metadata must be the final frontmatter field")
    canonical_header = skill_header.rsplit(marker, 1)[0]
    canonical_skill = ("---\n" + canonical_header + "\n---" + skill_body).encode()
    hasher = hashlib.sha256()
    files: list[Path] = []
    total_bytes = 0
    for directory, directories, names in os.walk(version_path, followlinks=False):
        directory_path = Path(directory)
        for name in directories:
            if (directory_path / name).is_symlink():
                raise ValueError(f"package contains symlink: {(directory_path / name).relative_to(version_path)}")
        for name in names:
            path = directory_path / name
            if path.is_symlink():
                raise ValueError(f"package contains symlink: {path.relative_to(version_path)}")
            mode = path.lstat().st_mode
            if not stat.S_ISREG(mode):
                raise ValueError(f"package contains unsupported file: {path.relative_to(version_path)}")
            total_bytes += path.stat().st_size
            if len(files) >= MAX_PACKAGE_FILES or total_bytes > MAX_PACKAGE_BYTES:
                raise ValueError("package exceeds source-integrity resource limits")
            files.append(path)
    for path in sorted(files):
        relative = path.relative_to(version_path).as_posix().encode()
        content = canonical_skill if relative == b"SKILL.md" else path.read_bytes()
        hasher.update(struct.pack(">Q", len(relative)))
        hasher.update(relative)
        hasher.update(struct.pack(">Q", len(content)))
        hasher.update(content)
    return "sha256:" + hasher.hexdigest()


class RegistryValidator:
    def __init__(self, root: Path, base_ref: str | None = None) -> None:
        self.root = root.resolve()
        self.base_ref = base_ref
        self.errors: list[str] = []
        self.releases: dict[str, ReleasedSkill] = {}
        self.current: dict[tuple[str, str], ReleasedSkill] = {}
        self.packages: set[tuple[str, str]] = set()

    def error(self, path: Path | str, message: str) -> None:
        if isinstance(path, Path):
            try:
                label = path.relative_to(self.root).as_posix()
            except ValueError:
                label = path.as_posix()
        else:
            label = path
        self.errors.append(f"{label}: {message}")

    def validate(self) -> list[str]:
        skills_root = self.root / "skills"
        if not skills_root.is_dir() or skills_root.is_symlink():
            self.error(skills_root, "must be a real directory")
            return self.errors
        for namespace_path in sorted(skills_root.iterdir()):
            if not namespace_path.is_dir() or namespace_path.is_symlink():
                self.error(namespace_path, "namespace must be a real directory")
                continue
            namespace = namespace_path.name
            if not NAME_PATTERN.fullmatch(namespace):
                self.error(namespace_path, "namespace must use kebab-case")
                continue
            for package_path in sorted(namespace_path.iterdir()):
                if package_path.name == "manifest.yaml" and namespace == "workspace":
                    continue
                if not package_path.is_dir() or package_path.is_symlink():
                    self.error(package_path, "skill package must be a real directory")
                    continue
                self.validate_package(namespace, package_path)
        self.validate_dependencies()
        self.validate_workspace_manifest(skills_root / "workspace" / "manifest.yaml")
        if self.base_ref:
            self.validate_immutability(self.base_ref)
        return sorted(set(self.errors))

    def validate_package(self, namespace: str, package_path: Path) -> None:
        skill_id = package_path.name
        self.packages.add((namespace, skill_id))
        if not NAME_PATTERN.fullmatch(skill_id):
            self.error(package_path, "skill directory must use kebab-case")
            return

        aliases: dict[str, str] = {}
        for alias in ("latest", "default"):
            alias_path = package_path / alias
            if not alias_path.is_symlink():
                self.error(alias_path, "required alias must be a symlink")
                continue
            target = os.readlink(alias_path)
            if "/" in target or "\\" in target or not VERSION_DIR_PATTERN.fullmatch(target):
                self.error(alias_path, "alias must target one contained exact version directory")
                continue
            target_path = package_path / target
            if target_path.is_symlink() or not target_path.is_dir():
                self.error(alias_path, "alias target must be a real exact version directory")
                continue
            try:
                target_path.resolve(strict=True).relative_to(package_path.resolve(strict=True))
            except (OSError, RuntimeError, ValueError):
                self.error(alias_path, "alias target escapes its package")
                continue
            aliases[alias] = target.removeprefix("v")

        versions: dict[str, Path] = {}
        for child in sorted(package_path.iterdir()):
            match = VERSION_DIR_PATTERN.fullmatch(child.name)
            if not match:
                continue
            version = child.name.removeprefix("v")
            if child.is_symlink() or not child.is_dir():
                self.error(child, "exact version must be a real directory")
                continue
            versions[version] = child
        if not versions:
            self.error(package_path, "must contain at least one exact version directory")
            return
        if aliases.get("latest") and aliases["latest"] != max(versions, key=semver_key):
            self.error(package_path / "latest", "must target the highest published semantic version")

        root_snapshot = self.payload_snapshot(
            package_path,
            excluded={"latest", "default", *(f"v{version}" for version in versions)},
        )
        latest_version = aliases.get("latest")
        if latest_version in versions:
            version_snapshot = self.payload_snapshot(versions[latest_version], excluded=set())
            if root_snapshot != version_snapshot:
                self.error(package_path, "root/current payload must exactly match the latest version")

        root_release = self.parse_release(namespace, skill_id, package_path, latest_version)
        if root_release is not None:
            self.current[(namespace, skill_id)] = root_release
        for version, version_path in versions.items():
            release = self.parse_release(namespace, skill_id, version_path, version)
            if release is None:
                continue
            if release.coordinate in self.releases:
                self.error(version_path, f"duplicate release coordinate {release.coordinate}")
            self.releases[release.coordinate] = release

    def payload_snapshot(self, path: Path, excluded: set[str]) -> dict[str, tuple[int, str]]:
        snapshot: dict[str, tuple[int, str]] = {}
        file_count = 0
        byte_count = 0
        for directory, directories, files in os.walk(path, followlinks=False):
            directory_path = Path(directory)
            kept: list[str] = []
            for name in directories:
                child = directory_path / name
                if directory_path == path and name in excluded:
                    continue
                if child.is_symlink():
                    self.error(child, "payload directories must not be symlinks")
                    continue
                if not child.is_dir():
                    self.error(child, "unsupported payload entry type")
                    continue
                kept.append(name)
            directories[:] = kept
            for name in files:
                child = directory_path / name
                if directory_path == path and name in excluded:
                    continue
                relative = child.relative_to(path).as_posix()
                mode = child.lstat().st_mode
                if stat.S_ISLNK(mode):
                    self.error(child, "payload files must not be symlinks")
                    continue
                if not stat.S_ISREG(mode):
                    self.error(child, "unsupported payload entry type")
                    continue
                size = child.stat().st_size
                file_count += 1
                byte_count += size
                if file_count > MAX_PACKAGE_FILES or byte_count > MAX_PACKAGE_BYTES:
                    continue
                content = child.read_bytes()
                if len(content) != size:
                    self.error(child, "payload changed while it was being validated")
                    continue
                snapshot[relative] = (
                    0o755 if mode & stat.S_IXUSR else 0o644,
                    hashlib.sha256(content).hexdigest(),
                )
        if file_count == 0:
            self.error(path, "package payload must contain at least one file")
        if file_count > MAX_PACKAGE_FILES:
            self.error(path, f"package payload exceeds {MAX_PACKAGE_FILES} files")
        if byte_count > MAX_PACKAGE_BYTES:
            self.error(path, f"package payload exceeds {MAX_PACKAGE_BYTES} bytes")
        return snapshot

    def parse_release(
        self,
        namespace: str,
        skill_id: str,
        path: Path,
        expected_version: str | None,
    ) -> ReleasedSkill | None:
        skill_path = path / "SKILL.md"
        if not skill_path.is_file() or skill_path.is_symlink():
            self.error(skill_path, "must be a real file")
            return None
        try:
            frontmatter, header, body = parse_frontmatter(skill_path)
        except ValueError as error:
            self.error(skill_path, str(error))
            return None
        if frontmatter.get("name") != skill_id:
            self.error(skill_path, f"frontmatter name must be {skill_id}")
        description = frontmatter.get("description")
        if not isinstance(description, str) or not description.strip():
            self.error(skill_path, "description must be a non-empty string")
        elif len(description) > 1024:
            self.error(skill_path, "description must not exceed 1024 characters")

        metadata_value = frontmatter.get("metadata", {})
        if not isinstance(metadata_value, dict):
            self.error(skill_path, "metadata must be a mapping")
            metadata: dict[str, str] = {}
        else:
            metadata = {}
            for key, value in metadata_value.items():
                if not isinstance(key, str) or not isinstance(value, str):
                    self.error(skill_path, "metadata keys and values must be strings")
                    continue
                metadata[key] = value
        top_version = frontmatter.get("version")
        if top_version is not None and not isinstance(top_version, str):
            self.error(skill_path, "top-level version must be a string")
        version = metadata.get("skm-version") or (top_version if isinstance(top_version, str) else "")
        if not SEMVER_PATTERN.fullmatch(version):
            self.error(skill_path, "release must declare an exact semantic version")
            return None
        if expected_version is not None and version != expected_version:
            self.error(skill_path, f"declared version must be {expected_version}")

        dependencies: tuple[str, ...] = ()
        raw_dependencies = metadata.get("skm-dependencies", "")
        if raw_dependencies:
            parts = tuple(item.strip() for item in raw_dependencies.split(","))
            if any(not item for item in parts) or raw_dependencies != ", ".join(parts):
                self.error(skill_path, "skm-dependencies must be a canonical comma-and-space list")
            if len(parts) != len(set(parts)):
                self.error(skill_path, "skm-dependencies must not contain duplicates")
            for dependency in parts:
                if not DEPENDENCY_PATTERN.fullmatch(dependency):
                    self.error(skill_path, f"invalid exact dependency coordinate {dependency!r}")
            dependencies = parts

        release = ReleasedSkill(namespace, skill_id, version, path, metadata, dependencies)
        if namespace == "workspace":
            self.validate_workspace_release(release, skill_path, header, body)
        return release

    def validate_workspace_release(
        self,
        release: ReleasedSkill,
        skill_path: Path,
        header: str,
        body: str,
    ) -> None:
        metadata = release.metadata
        missing = sorted(WORKSPACE_METADATA - metadata.keys())
        if missing:
            self.error(skill_path, "missing Workspace release metadata: " + ", ".join(missing))
            return
        if metadata["skm-version"] != release.version:
            self.error(skill_path, "skm-version must match the exact package version")
        if metadata["skm-source-repository"] != SOURCE_REPOSITORY:
            self.error(skill_path, f"skm-source-repository must be {SOURCE_REPOSITORY}")
        if not REVISION_PATTERN.fullmatch(metadata["skm-source-revision"]):
            self.error(skill_path, "skm-source-revision must be a full lowercase Git commit hash")
        expected_path = f"workspace/instructions/skills/{release.skill_id}"
        if metadata["skm-source-path"] != expected_path:
            self.error(skill_path, f"skm-source-path must be {expected_path}")
        if not INTEGRITY_PATTERN.fullmatch(metadata["skm-source-integrity"]):
            self.error(skill_path, "skm-source-integrity must be a sha256 digest")
        if not SEMVER_PATTERN.fullmatch(metadata["workspace-toolkit-version"]):
            self.error(skill_path, "workspace-toolkit-version must be an exact semantic version")
        if not re.fullmatch(r"(?:0|[1-9]\d*)\.x", metadata["workspace-docs-compatibility"]):
            self.error(skill_path, "workspace-docs-compatibility must be a major compatibility line")
        if not SEMVER_PATTERN.fullmatch(metadata["minimum-skm-version"]):
            self.error(skill_path, "minimum-skm-version must be an exact semantic version")
        if semver_key(metadata["minimum-skm-version"]) < semver_key("0.4.0"):
            self.error(skill_path, "Workspace packages require minimum-skm-version 0.4.0 or newer")
        if metadata["skm-adapter-compatibility"] != "2.x":
            self.error(skill_path, "skm-adapter-compatibility must be 2.x")
        if VERSION_DIR_PATTERN.fullmatch(release.path.name):
            try:
                computed = source_tree_hash(release.path, header, body)
            except (OSError, ValueError) as error:
                self.error(skill_path, f"cannot verify source integrity: {error}")
            else:
                if metadata["skm-source-integrity"] != computed:
                    self.error(skill_path, "skm-source-integrity does not match reconstructed canonical source")

    def validate_dependencies(self) -> None:
        graph: dict[str, tuple[str, ...]] = {}
        for coordinate, release in self.releases.items():
            graph[coordinate] = release.dependencies
            for dependency in release.dependencies:
                match = DEPENDENCY_PATTERN.fullmatch(dependency)
                if not match:
                    continue
                if dependency not in self.releases:
                    self.error(release.path / "SKILL.md", f"dependency is not published: {dependency}")
        active: list[str] = []
        complete: set[str] = set()

        def visit(coordinate: str) -> None:
            if coordinate in active:
                cycle = active[active.index(coordinate) :] + [coordinate]
                self.error("skills", "dependency cycle: " + " -> ".join(cycle))
                return
            if coordinate in complete:
                return
            active.append(coordinate)
            for dependency in graph.get(coordinate, ()):
                if dependency in graph:
                    visit(dependency)
            active.pop()
            complete.add(coordinate)

        for coordinate in sorted(graph):
            visit(coordinate)

    def validate_workspace_manifest(self, path: Path) -> None:
        workspace_packages = {
            skill_id: release
            for (namespace, skill_id), release in self.current.items()
            if namespace == "workspace"
        }
        if not workspace_packages:
            if path.exists() or path.is_symlink():
                self.error(path, "must not exist without Workspace packages")
            return
        if not path.is_file() or path.is_symlink():
            self.error(path, "must be a real file when Workspace packages are published")
            return
        if path.stat().st_size > 256 * 1024:
            self.error(path, "must not exceed 262144 bytes")
            return
        try:
            manifest = parse_yaml(path.read_text(encoding="utf-8"), str(path))
        except (OSError, UnicodeError, ValueError) as error:
            self.error(path, str(error))
            return
        allowed = {
            "schema_version",
            "namespace",
            "toolkit_version",
            "source_repository",
            "source_revision",
            "workspace_docs_compatibility",
            "minimum_skm_version",
            "skm_adapter_compatibility",
            "packages",
        }
        unknown = sorted(set(manifest) - allowed)
        if unknown:
            self.error(path, "unknown manifest fields: " + ", ".join(unknown))
        if manifest.get("schema_version") != 1 or manifest.get("namespace") != "workspace":
            self.error(path, "schema_version must be 1 and namespace must be workspace")
        packages_value = manifest.get("packages")
        if not isinstance(packages_value, dict) or not all(
            isinstance(key, str) and isinstance(value, str)
            for key, value in packages_value.items()
        ):
            self.error(path, "packages must map skill ids to exact version strings")
            return
        expected = {skill_id: release.version for skill_id, release in workspace_packages.items()}
        if packages_value != dict(sorted(expected.items())):
            self.error(path, "package inventory must exactly match Workspace root/current releases")
        field_map = {
            "toolkit_version": "workspace-toolkit-version",
            "source_repository": "skm-source-repository",
            "source_revision": "skm-source-revision",
            "workspace_docs_compatibility": "workspace-docs-compatibility",
            "minimum_skm_version": "minimum-skm-version",
            "skm_adapter_compatibility": "skm-adapter-compatibility",
        }
        for manifest_field, metadata_field in field_map.items():
            value = manifest.get(manifest_field)
            if not isinstance(value, str):
                self.error(path, f"{manifest_field} must be a string")
                continue
            mismatched = sorted(
                skill_id
                for skill_id, release in workspace_packages.items()
                if release.metadata.get(metadata_field) != value
            )
            if mismatched:
                self.error(path, f"{manifest_field} disagrees with packages: " + ", ".join(mismatched))

    def validate_immutability(self, base_ref: str) -> None:
        try:
            subprocess.run(
                ["git", "rev-parse", "--verify", f"{base_ref}^{{commit}}"],
                cwd=self.root,
                check=True,
                capture_output=True,
            )
            output = subprocess.run(
                ["git", "ls-tree", "-r", "-z", "--full-tree", base_ref, "--", "skills"],
                cwd=self.root,
                check=True,
                capture_output=True,
            ).stdout
            object_format = subprocess.run(
                ["git", "rev-parse", "--show-object-format"],
                cwd=self.root,
                check=True,
                capture_output=True,
                text=True,
            ).stdout.strip()
        except (OSError, subprocess.CalledProcessError) as error:
            self.error("git", f"cannot inspect immutability base {base_ref}: {error}")
            return
        base_entries: dict[str, tuple[str, str]] = {}
        exact_roots: set[str] = set()
        for record in output.split(b"\0"):
            if not record:
                continue
            metadata, raw_path = record.split(b"\t", 1)
            mode, object_type, object_id = metadata.decode().split()
            if object_type != "blob":
                continue
            path = raw_path.decode()
            parts = path.split("/")
            if len(parts) < 5 or parts[0] != "skills" or not VERSION_DIR_PATTERN.fullmatch(parts[3]):
                continue
            exact_root = "/".join(parts[:4])
            exact_roots.add(exact_root)
            base_entries[path] = (mode, object_id)
        if object_format not in hashlib.algorithms_available:
            self.error("git", f"unsupported Git object format: {object_format}")
            return
        current_entries: dict[str, tuple[str, str]] = {}
        for exact_root in sorted(exact_roots):
            absolute_root = self.root / exact_root
            if not absolute_root.is_dir() or absolute_root.is_symlink():
                continue
            for path in sorted(absolute_root.rglob("*")):
                if path.is_dir() and not path.is_symlink():
                    continue
                mode_value = path.lstat().st_mode
                if stat.S_ISLNK(mode_value):
                    mode = "120000"
                    content = os.readlink(path).encode()
                elif stat.S_ISREG(mode_value):
                    mode = "100755" if mode_value & stat.S_IXUSR else "100644"
                    content = path.read_bytes()
                else:
                    continue
                header = f"blob {len(content)}\0".encode()
                object_id = hashlib.new(object_format, header + content).hexdigest()
                current_entries[path.relative_to(self.root).as_posix()] = (mode, object_id)
        if base_entries != current_entries:
            changed = sorted(set(base_entries) ^ set(current_entries))
            changed.extend(
                path
                for path in sorted(set(base_entries) & set(current_entries))
                if base_entries[path] != current_entries[path]
            )
            self.error(
                "skills",
                "published exact versions are immutable relative to "
                f"{base_ref}; changed entries: " + ", ".join(changed[:10]),
            )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--base-ref", help="Git revision whose exact versions must remain unchanged")
    arguments = parser.parse_args()
    validator = RegistryValidator(arguments.root, arguments.base_ref)
    errors = validator.validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"Registry validation failed with {len(errors)} error(s)", file=sys.stderr)
        return 1
    print(
        f"Registry validation passed: {len(validator.packages)} packages, "
        f"{len(validator.releases)} exact releases"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
