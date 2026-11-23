import os
import shutil
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
    shutil.copyfile(source, output_dir / "entry.png")


if __name__ == "__main__":
    main()
