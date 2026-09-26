# Upstream Snapshots

`skm-cli.txt` is the complete `--help` output of the skm version this
registry's documentation was last reviewed against. Its first line names that
version.

The `Upstream Release` workflow diffs each new skm production release against
this file and opens a `docs-review` issue. When you close that issue, replace
this file with the `skm-cli.txt` artifact from the workflow run linked in it.
To capture it yourself from a released binary:

```sh
python3 scripts/upstream_release.py skm-cli --binary /path/to/skm > docs/upstream/skm-cli.txt
```
