"""Entry for make.fun bounty news-image-20261126.

Copies the pre-built image entry.png (in this repository) to
$MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png).
Standard library only, no network, deterministic: the output bytes
are exactly the bytes of entry.png, so two runs are identical.
"""
import os
import shutil
import sys
from pathlib import Path

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def main() -> int:
    src = Path(__file__).resolve().parent / "entry.png"
    if not src.is_file():
        print(f"entry.png not found next to {__file__}", file=sys.stderr)
        return 1
    data = src.read_bytes()
    if not data.startswith(PNG_MAGIC):
        print("entry.png is not a PNG file", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / "entry.png"
    shutil.copyfile(src, out)
    if out.read_bytes() != data:
        print("output does not match entry.png", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
