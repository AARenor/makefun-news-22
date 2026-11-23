"""Copy the repository's entry.png into a resolved output directory.

Standard library only, no network. --out wins, then MAKEFUN_OUTPUT_DIR,
then OUTPUT_DIR, then /output when that directory exists, and finally
out/ beside this script. The copied bytes are the repository file's
bytes, unchanged.
"""

from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
IMAGE = "entry.png"
SYSTEM_OUTPUT = Path("/output")
ENV_KEYS = ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR")


def source_image() -> Path:
    """Return the repository file that is the single source of the bytes."""
    return HERE / IMAGE


def fallback_output() -> Path:
    """Return /output when it is a directory, else out/ beside this script."""
    if SYSTEM_OUTPUT.is_dir():
        return SYSTEM_OUTPUT
    return HERE / "out"


def parse_args(argv: list[str]) -> Path | None:
    """Return the --out directory from argv, or None when it is absent."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", metavar="DIR", help="override the output directory")
    chosen = parser.parse_args(argv).out
    return Path(chosen).expanduser() if chosen else None


def resolve_output(override: Path | None = None) -> Path:
    """Return the destination directory, before it is created."""
    if override is not None:
        return override
    for key in ENV_KEYS:
        value = os.environ.get(key, "").strip()
        if value:
            return Path(value).expanduser()
    return fallback_output()


def copy_entry(destination: Path) -> Path:
    """Create destination, then copy entry.png into it byte for byte."""
    destination.mkdir(parents=True, exist_ok=True)
    target = destination / IMAGE
    shutil.copyfile(source_image(), target)
    return target


def main() -> int:
    source = source_image()
    if not source.is_file():
        print(f"error: {source} is missing", file=sys.stderr)
        return 1
    target = copy_entry(resolve_output(parse_args(sys.argv[1:])))
    print(f"wrote {target} ({target.stat().st_size} bytes)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

