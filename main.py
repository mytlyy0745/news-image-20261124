"""Entry program for news-image-20261124 (Python 3.13, standard library only).

Reads entry.png from the directory this file lives in, checks it is a real
PNG within the competition limits, and copies it byte for byte to
/output/entry.png (or $MAKEFUN_OUTPUT_DIR/entry.png). No network, no
re-encoding: the bytes that leave are exactly the bytes that came in, so
two runs always produce identical output.
"""

import binascii
import os
import shutil
import struct
import sys

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1_048_576
MAX_SIDE = 1024
SOURCE_NAME = "entry.png"
TARGET_NAME = "entry.png"


def read_source():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, SOURCE_NAME)
    with open(path, "rb") as handle:
        return handle.read()


def check_png(data):
    if len(data) < 8 or data[:8] != PNG_MAGIC:
        raise SystemExit("entry.png is not a PNG file (bad magic bytes)")
    if len(data) > MAX_BYTES:
        raise SystemExit(
            "entry.png is %d bytes, over the 1048576-byte limit" % len(data)
        )
    if len(data) < 24:
        raise SystemExit("entry.png is too short to hold a PNG header")
    width, height = struct.unpack(">II", data[16:24])
    if width == 0 or height == 0:
        raise SystemExit("entry.png has a zero dimension")
    if width > MAX_SIDE or height > MAX_SIDE:
        raise SystemExit(
            "entry.png is %dx%d, over the 1024x1024 limit" % (width, height)
        )
    check_chunks(data)
    return width, height


def check_chunks(data):
    """Walk every PNG chunk, verify its CRC, require a trailing IEND."""
    offset = 8
    seen_iend = False
    while offset + 8 <= len(data):
        length = struct.unpack(">I", data[offset:offset + 4])[0]
        kind = data[offset + 4:offset + 8]
        end = offset + 12 + length
        if end > len(data):
            raise SystemExit("entry.png is truncated inside a %s chunk" % kind.decode("latin-1"))
        stored_crc = struct.unpack(">I", data[offset + 8 + length:offset + 12 + length])[0]
        actual_crc = binascii.crc32(kind + data[offset + 8:offset + 8 + length]) & 0xFFFFFFFF
        if stored_crc != actual_crc:
            raise SystemExit("entry.png has a bad CRC in its %s chunk" % kind.decode("latin-1"))
        if kind == b"IEND":
            seen_iend = True
            if end != len(data):
                raise SystemExit("entry.png has trailing bytes after IEND")
            break
        offset = end
    if not seen_iend:
        raise SystemExit("entry.png has no IEND chunk (truncated file)")


def main():
    data = read_source()
    width, height = check_png(data)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, TARGET_NAME)
    with open(target, "wb") as handle:
        handle.write(data)
    with open(target, "rb") as handle:
        written = handle.read()
    if written != data:
        raise SystemExit("output %s does not match entry.png" % target)
    print("wrote %s (%dx%d, %d bytes)" % (target, width, height, len(data)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
