#!/usr/bin/env python3
"""Entrypoint: copy the front page to the output directory.

Standard library only, no network. Deterministic: the same entry.png bytes
are copied on every run, and the copy is verified byte for byte.
"""
import hashlib
import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    with open(source, "rb") as handle:
        head = handle.read(8)
    if head != b"\x89PNG\r\n\x1a\n":
        print("entry.png is not a PNG file", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, target)
    with open(source, "rb") as handle:
        want = hashlib.sha256(handle.read()).hexdigest()
    with open(target, "rb") as handle:
        got = hashlib.sha256(handle.read()).hexdigest()
    if want != got:
        print("entry.png copy mismatch", file=sys.stderr)
        return 1
    print("entry.png copied to " + target
          + " (" + str(os.path.getsize(target)) + " bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
