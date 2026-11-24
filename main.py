#!/usr/bin/env python3
"""Write the 24 November 2026 world-news image to /output/entry.png.

The image is stored in this repository as entry.png; this program copies
it byte-identical to /output/entry.png. It runs offline and writes the
same bytes on every run.
"""
import hashlib
import os
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(DST_DIR, "entry.png")
MAX_BYTES = 1024 * 1024

with open(SRC, "rb") as f:
    data = f.read()

if data[:8] != b"\x89PNG\r\n\x1a\n":
    print("entry.png is not a PNG file", file=sys.stderr)
    sys.exit(1)
if len(data) > MAX_BYTES:
    print(f"entry.png is {len(data)} bytes, over the 1 MiB limit", file=sys.stderr)
    sys.exit(1)
# Validate PNG dimensions from the IHDR chunk (must be <= 1024x1024).
width, height = struct.unpack(">II", data[16:24])
if width > 1024 or height > 1024:
    print(f"entry.png is {width}x{height}, over the 1024x1024 limit", file=sys.stderr)
    sys.exit(1)

os.makedirs(DST_DIR, exist_ok=True)
with open(DST, "wb") as f:
    f.write(data)

print(f"wrote {DST} ({len(data)} bytes, sha256 {hashlib.sha256(data).hexdigest()})")
