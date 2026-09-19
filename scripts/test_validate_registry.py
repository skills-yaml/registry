#!/usr/bin/env python3
"""Regression tests for the registry validator."""

from __future__ import annotations

import hashlib
import os
import shutil
import struct
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))

from validate_registry import RegistryValidator  # noqa: E402


REVISION = "1" * 40


def canonical_hash(files: dict[str, bytes]) -> str:
    hasher = hashlib.sha256()
    for relative, content in sorted(files.items()):
        encoded = relative.encode()
        hasher.update(struct.pack(">Q", len(encoded)))
        hasher.update(encoded)
        hasher.update(struct.pack(">Q", len(content)))
        hasher.update(content)
    return "sha256:" + hasher.hexdigest()


class RegistryValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        (self.root / "skills" / "workspace").mkdir(parents=True)
        self.packages: dict[str, str] = {}

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def create_package(
        self,
        skill_id: str,
        version: str = "0.1.0",
        dependencies: tuple[str, ...] = (),
    ) -> Path:
        canonical_skill = (
            "---\n"
            f"name: {skill_id}\n"
            f"description: Exercise the {skill_id} validation fixture.\n"
            "---\n\n"
            f"# {skill_id}\n"
        ).encode()
        canonical_files = {
            "SKILL.md": canonical_skill,
            "agents/openai.yaml": b'interface:\n  display_name: "Fixture"\n',
        }
        integrity = canonical_hash(canonical_files)
        dependency_line = ""
        if dependencies:
            dependency_line = (
                '  skm-dependencies: "' + ", ".join(dependencies) + '"\n'
            )
        released_skill = (
            "---\n"
            f"name: {skill_id}\n"
            f"description: Exercise the {skill_id} validation fixture.\n"
            "metadata:\n"
            f'  skm-version: "{version}"\n'
            '  skm-source-repository: "https://github.com/skills-yaml/workspace.git"\n'
            f'  skm-source-revision: "{REVISION}"\n'
            f'  skm-source-path: "workspace/instructions/skills/{skill_id}"\n'
            f'  skm-source-integrity: "{integrity}"\n'
            '  workspace-toolkit-version: "0.3.0"\n'
            '  workspace-docs-compatibility: "5.x"\n'
            '  minimum-skm-version: "0.4.0"\n'
            '  skm-adapter-compatibility: "2.x"\n'
            + dependency_line
            + "---\n\n"
            + f"# {skill_id}\n"
        )
        package = self.root / "skills" / "workspace" / skill_id
        version_path = package / f"v{version}"
        (version_path / "agents").mkdir(parents=True)
        (version_path / "SKILL.md").write_text(released_skill, encoding="utf-8")
        (version_path / "agents" / "openai.yaml").write_bytes(
            canonical_files["agents/openai.yaml"]
        )
        (package / "SKILL.md").write_text(released_skill, encoding="utf-8")
        (package / "agents").mkdir()
        (package / "agents" / "openai.yaml").write_bytes(
            canonical_files["agents/openai.yaml"]
        )
        (package / "latest").symlink_to(f"v{version}")
        (package / "default").symlink_to(f"v{version}")
        self.packages[skill_id] = version
        return package

    def write_manifest(self) -> None:
        manifest = {
            "schema_version": 1,
            "namespace": "workspace",
            "toolkit_version": "0.3.0",
            "source_repository": "https://github.com/skills-yaml/workspace.git",
            "source_revision": REVISION,
            "workspace_docs_compatibility": "5.x",
            "minimum_skm_version": "0.4.0",
            "skm_adapter_compatibility": "2.x",
            "packages": dict(sorted(self.packages.items())),
        }
        (self.root / "skills" / "workspace" / "manifest.yaml").write_text(
            yaml.safe_dump(manifest, sort_keys=False),
            encoding="utf-8",
        )

    def create_generic_package(
        self,
        namespace: str,
        skill_id: str,
        version: str = "1.0.0",
    ) -> Path:
        content = (
            "---\n"
            f"name: {skill_id}\n"
            f'version: "{version}"\n'
            f"description: Exercise the {skill_id} generic fixture.\n"
            "---\n\n"
            f"# {skill_id}\n"
        )
        package = self.root / "skills" / namespace / skill_id
        version_path = package / f"v{version}"
        version_path.mkdir(parents=True)
        (version_path / "SKILL.md").write_text(content, encoding="utf-8")
        (package / "SKILL.md").write_text(content, encoding="utf-8")
        (package / "latest").symlink_to(f"v{version}")
        (package / "default").symlink_to(f"v{version}")
        return package

    def errors(self, base_ref: str | None = None) -> list[str]:
        return RegistryValidator(self.root, base_ref).validate()

    def replace_in_payload(self, package: Path, old: str, new: str) -> None:
        for skill_path in (package / "SKILL.md", package / "v0.1.0" / "SKILL.md"):
            skill_path.write_text(
                skill_path.read_text(encoding="utf-8").replace(old, new),
                encoding="utf-8",
            )

    def test_accepts_valid_workspace_packages_and_dependency(self) -> None:
        self.create_package("write-spec")
        self.create_package("wk-spec", dependencies=("workspace/write-spec@0.1.0",))
        self.write_manifest()
        self.assertEqual(self.errors(), [])

    def test_accepts_exact_dependency_from_another_namespace(self) -> None:
        self.create_generic_package("shared", "helper")
        self.create_package(
            "wk-spec",
            dependencies=("shared/helper@1.0.0",),
        )
        self.write_manifest()
        self.assertEqual(self.errors(), [])

    def test_rejects_root_current_drift(self) -> None:
        package = self.create_package("wk-spec")
        self.write_manifest()
        (package / "SKILL.md").write_text(
            (package / "SKILL.md").read_text(encoding="utf-8") + "\nDrift.\n",
            encoding="utf-8",
        )
        self.assertTrue(any("root/current payload" in item for item in self.errors()))

    def test_rejects_alias_escape(self) -> None:
        package = self.create_package("wk-spec")
        self.write_manifest()
        (package / "latest").unlink()
        (package / "latest").symlink_to("../../outside")
        self.assertTrue(any("alias must target" in item for item in self.errors()))

    def test_rejects_symlinked_exact_version(self) -> None:
        package = self.create_package("wk-spec")
        self.write_manifest()
        shutil.rmtree(package / "v0.1.0")
        (package / "v0.1.1").mkdir()
        (package / "v0.1.0").symlink_to("v0.1.1")
        self.assertTrue(any("exact version must be a real directory" in item for item in self.errors()))

    def test_rejects_symlink_inside_version_payload(self) -> None:
        package = self.create_package("wk-spec")
        self.write_manifest()
        (package / "v0.1.0" / "escape").symlink_to("../../outside")
        self.assertTrue(any("payload files must not be symlinks" in item for item in self.errors()))

    def test_rejects_missing_dependency(self) -> None:
        self.create_package(
            "wk-spec",
            dependencies=("workspace/write-spec@0.1.0",),
        )
        self.write_manifest()
        self.assertTrue(any("dependency is not published" in item for item in self.errors()))

    def test_rejects_dependency_cycle(self) -> None:
        self.create_package("one", dependencies=("workspace/two@0.1.0",))
        self.create_package("two", dependencies=("workspace/one@0.1.0",))
        self.write_manifest()
        self.assertTrue(any("dependency cycle" in item for item in self.errors()))

    def test_rejects_source_integrity_mismatch(self) -> None:
        package = self.create_package("wk-spec")
        self.write_manifest()
        self.replace_in_payload(package, "sha256:", "sha256:" + "0" * 64 + " # ")
        self.assertTrue(any("skm-source-integrity" in item for item in self.errors()))

    def test_rejects_manifest_inventory_mismatch(self) -> None:
        self.create_package("wk-spec")
        self.write_manifest()
        manifest_path = self.root / "skills" / "workspace" / "manifest.yaml"
        manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
        manifest["packages"] = {}
        manifest_path.write_text(yaml.safe_dump(manifest, sort_keys=False), encoding="utf-8")
        self.assertTrue(any("package inventory" in item for item in self.errors()))

    def test_rejects_duplicate_frontmatter_keys(self) -> None:
        package = self.create_package("wk-spec")
        self.write_manifest()
        for skill_path in (package / "SKILL.md", package / "v0.1.0" / "SKILL.md"):
            content = skill_path.read_text(encoding="utf-8")
            skill_path.write_text(content.replace("name: wk-spec\n", "name: wk-spec\nname: duplicate\n"), encoding="utf-8")
        self.assertTrue(any("duplicate YAML key" in item for item in self.errors()))

    def test_rejects_non_scalar_yaml_mapping_key_cleanly(self) -> None:
        package = self.create_package("wk-spec")
        self.write_manifest()
        for skill_path in (package / "SKILL.md", package / "v0.1.0" / "SKILL.md"):
            content = skill_path.read_text(encoding="utf-8")
            skill_path.write_text(
                content.replace("---\nname:", "---\n? [invalid]\n: value\nname:", 1),
                encoding="utf-8",
            )
        errors = self.errors()
        self.assertTrue(any("mapping keys must be scalar" in item for item in errors))

    def commit_baseline(self) -> None:
        subprocess.run(["git", "init", "-q"], cwd=self.root, check=True)
        subprocess.run(["git", "add", "."], cwd=self.root, check=True)
        subprocess.run(
            [
                "git",
                "-c",
                "user.name=Registry Test",
                "-c",
                "user.email=registry@example.invalid",
                "commit",
                "-qm",
                "baseline",
            ],
            cwd=self.root,
            check=True,
        )

    def supersede_generic_package(self, package: Path, old: str, new: str) -> None:
        """Publish `new`, retire `old`, and point the package at the replacement."""
        content = (package / f"v{old}" / "SKILL.md").read_text(encoding="utf-8")
        content = content.replace(f'version: "{old}"', f'version: "{new}"')
        (package / f"v{new}").mkdir()
        (package / f"v{new}" / "SKILL.md").write_text(content, encoding="utf-8")
        (package / "SKILL.md").write_text(content, encoding="utf-8")
        shutil.rmtree(package / f"v{old}")
        for alias in ("latest", "default"):
            (package / alias).unlink()
            (package / alias).symlink_to(f"v{new}")

    def write_withdrawal(self, coordinate: str, **overrides: object) -> None:
        entry: dict[str, object] = {
            "coordinate": coordinate,
            "withdrawn": "2026-09-19",
            "reason": "Disclosed private infrastructure.",
        }
        entry.update(overrides)
        (self.root / "WITHDRAWN.yaml").write_text(
            yaml.safe_dump({"schema_version": 1, "withdrawn": [entry]}, sort_keys=False),
            encoding="utf-8",
        )

    def test_rejects_mutation_of_published_exact_version(self) -> None:
        package = self.create_package("wk-spec")
        self.write_manifest()
        subprocess.run(["git", "init", "-q"], cwd=self.root, check=True)
        subprocess.run(["git", "add", "."], cwd=self.root, check=True)
        subprocess.run(
            [
                "git",
                "-c",
                "user.name=Registry Test",
                "-c",
                "user.email=registry@example.invalid",
                "commit",
                "-qm",
                "baseline",
            ],
            cwd=self.root,
            check=True,
        )
        version_skill = package / "v0.1.0" / "SKILL.md"
        version_skill.write_text(
            version_skill.read_text(encoding="utf-8") + "\nMutation.\n",
            encoding="utf-8",
        )
        self.assertTrue(any("published exact versions are immutable" in item for item in self.errors("HEAD")))

    def test_accepts_declared_withdrawal_of_published_exact_version(self) -> None:
        package = self.create_generic_package("system", "host-tools")
        self.commit_baseline()
        self.supersede_generic_package(package, "1.0.0", "1.1.0")
        self.write_withdrawal("system/host-tools@1.0.0")
        self.assertEqual(self.errors("HEAD"), [])

    def test_rejects_undeclared_withdrawal_of_published_exact_version(self) -> None:
        package = self.create_generic_package("system", "host-tools")
        self.commit_baseline()
        self.supersede_generic_package(package, "1.0.0", "1.1.0")
        self.assertTrue(
            any("published exact versions are immutable" in item for item in self.errors("HEAD"))
        )

    def test_accepts_withdrawal_after_it_has_left_the_base_ref(self) -> None:
        """The steady state: the withdrawal stays in the ledger once merged."""
        package = self.create_generic_package("system", "host-tools")
        self.supersede_generic_package(package, "1.0.0", "1.1.0")
        self.write_withdrawal("system/host-tools@1.0.0")
        self.commit_baseline()
        self.assertEqual(self.errors("HEAD"), [])

    def test_rejects_withdrawal_of_release_still_published(self) -> None:
        self.create_generic_package("system", "host-tools")
        self.commit_baseline()
        self.write_withdrawal("system/host-tools@1.0.0")
        self.assertTrue(
            any("must be removed from the tree" in item for item in self.errors("HEAD"))
        )

    def test_rejects_withdrawal_without_a_reason(self) -> None:
        package = self.create_generic_package("system", "host-tools")
        self.commit_baseline()
        self.supersede_generic_package(package, "1.0.0", "1.1.0")
        self.write_withdrawal("system/host-tools@1.0.0", reason="  ")
        self.assertTrue(any("non-empty reason" in item for item in self.errors("HEAD")))


if __name__ == "__main__":
    unittest.main()
