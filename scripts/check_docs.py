#!/usr/bin/env python3
"""Validate external documentation links, examples and disclosure boundaries."""
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
PRIVATE_REFERENCE = re.compile(
    r"(?:/Users/|/home/[^/\s]+/|\.docs/|\.internal/|"
    r"github\.com/72olabs/(?:holler|holler-connectors|daytona-runners)(?:[/#?\s)]|$))"
)
INTERNAL_CONTEXT = re.compile(
    r"(?:\.runs/|\bhackathon\b|\bsprint[ -]+\d+\b|\bcanar(?:y|ies)\b|"
    r"\brelease gates?\b|\bcandidate\b|\bworktree\b|\brehearsal\b|"
    r"\b(?:C[0-9]+)-[a-z]+-[a-z-]+\b)", re.IGNORECASE
)
LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def safe_name(value: str) -> str:
    path = PurePosixPath(value)
    if path.is_absolute() or ".." in path.parts or str(path) != value or path.suffix != ".md":
        raise ValueError(f"invalid public document path: {value}")
    return value


def validate_bundle(bundle: dict[str, str]) -> None:
    for name, content in bundle.items():
        if PRIVATE_REFERENCE.search(content):
            raise ValueError(f"private reference in {name}; remove from external documentation")
        if INTERNAL_CONTEXT.search(content):
            raise ValueError(f"internal context in {name}; apply the documentation policy")
        for target in LINK.findall(content):
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            # Resolve relative links within the document bundle; unrelated files
            # on the filesystem cannot satisfy a link.
            parts = list(PurePosixPath(name).parent.parts)
            for part in PurePosixPath(unquote(parsed.path)).parts:
                if part == "..":
                    if not parts:
                        raise ValueError(f"link escapes public bundle in {name}: {target}")
                    parts.pop()
                elif part not in (".", ""):
                    parts.append(part)
            resolved = "/".join(parts)
            if resolved not in bundle and not (
                resolved == "LICENSE" and (ROOT / "LICENSE").is_file()
                and not (ROOT / "LICENSE").is_symlink()
            ):
                raise ValueError(f"missing public link in {name}: {target}")
        for block in re.findall(r"```json\s*\n(.*?)\n```", content, re.S):
            json.loads(block)



def main():
    manifest = json.loads((ROOT / "docs-manifest.json").read_text())
    bundle = {}
    for item in manifest["documents"]:
        name = safe_name(item)
        source = ROOT / name
        component = ROOT
        for part in PurePosixPath(name).parts:
            component = component / part
            if component.is_symlink():
                raise ValueError(f"document must not use symlinks: {name}")
        bundle[name] = source.read_text()
    validate_bundle(bundle)
    listed = subprocess.check_output(
        ["git", "-C", str(ROOT), "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
    ).decode().split("\0")
    actual = {name for name in listed if name.endswith(".md") and (ROOT / name).is_file()}
    if actual != set(bundle):
        raise ValueError(f"document list mismatch: {sorted(actual.symmetric_difference(bundle))}")
    print(f"Validated {len(bundle)} documents for Holler {manifest['product_version']}.")



if __name__ == "__main__":
    main()
