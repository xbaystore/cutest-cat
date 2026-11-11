#!/usr/bin/env python3
"""Cutest Cat — make.fun bounty entry (cutest-cat-01).

Writes one picture of a cat to /output/entry.png.
The picture ships inside this repository as cat.png; the program simply
copies it, byte for byte, so every run produces the identical file.
No network, no randomness, no dependencies beyond the standard library.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "cat.png")
OUTPUT_DIR = "/output"
OUTPUT = os.path.join(OUTPUT_DIR, "entry.png")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT)
    print(f"wrote {OUTPUT} ({os.path.getsize(OUTPUT)} bytes)")


if __name__ == "__main__":
    main()
