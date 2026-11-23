import os
import shutil
import sys
from pathlib import Path


def main():
    source = Path(__file__).resolve().with_name("entry.png")
    configured_output = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
    )
    if configured_output:
        output_dir = Path(configured_output)
    elif Path("/output").is_dir():
        output_dir = Path("/output")
    else:
        output_dir = Path(__file__).resolve().parent / "out"

    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.png"
    shutil.copyfile(source, target)
    print(f"world briefing: wrote {target} ({target.stat().st_size} bytes)", file=sys.stderr)


if __name__ == "__main__":
    main()
