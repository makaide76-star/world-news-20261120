#!/usr/bin/env python3
"""Entry point (program/v1): write the entry image to /output/entry.png.

Stdlib only, no network, deterministic: the image ships in the repository
at assets/entry.png (drawn by tools/make_image.py from the wire headlines
of Friday 20 November 2026) and is copied byte for byte, so every run
writes identical bytes.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "assets", "entry.png")
OUT_DIR = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
OUT = os.path.join(OUT_DIR, "entry.png")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, OUT)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
