"""Fail unless the committed pyproject.toml version is higher than on a base ref.

Usage: check_version_bump.py [BASE_REF]
Without BASE_REF, the merge-base of HEAD with origin's default branch is used.
"""

import re
import subprocess
import sys

from packaging.version import Version


def git(*args: str) -> str:
    return subprocess.run(
        ["git", *args], capture_output=True, text=True, check=True
    ).stdout.strip()


def committed_version(ref: str) -> Version:
    text = git("show", f"{ref}:pyproject.toml")
    match = re.search(r'^version\s*=\s*"([^"]+)"', text, re.MULTILINE)
    if match is None:
        raise SystemExit(f"No version found in {ref}:pyproject.toml")
    return Version(match.group(1))


def default_base() -> str | None:
    for ref in ("origin/HEAD", "origin/main", "origin/master"):
        try:
            return git("merge-base", "HEAD", ref)
        except subprocess.CalledProcessError:
            continue
    return None


def main() -> int:
    base = sys.argv[1] if len(sys.argv) > 1 else default_base()
    if base is None or git("rev-parse", "HEAD") == git("rev-parse", base):
        return 0  # no remote yet, or nothing new to push
    try:
        old = committed_version(base)
    except subprocess.CalledProcessError:
        return 0  # pyproject.toml did not exist on the base ref
    new = committed_version("HEAD")
    if new > old:
        return 0
    print(
        f"pyproject.toml version {new} must be higher than {old} "
        f"(base {base[:12]}). Run: uv version --bump patch"
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
