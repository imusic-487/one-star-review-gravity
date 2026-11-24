#!/usr/bin/env python3
"""One-star review of gravity: write the entry line to /output/entry.txt.

Reads line.txt (the exact review, one line, no trailing newline), checks it
against the competition gate (UTF-8, 1-160 characters, not only whitespace),
then copies it byte for byte to /output/entry.txt and verifies the copy
byte for byte. A multi-line text is refused even when it fits the length
limit: the brief asks for one single-line review. A failed byte-for-byte
check reports the expected and actual sizes, so a bad copy is diagnosable.

Standard library only. No network, no secrets, no input besides line.txt.
"""

from __future__ import annotations

import sys
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "line.txt"
DEST = Path("/output/entry.txt")
MAX_CHARS = 160


def fail(message: str) -> "NoReturn":
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    raw = SOURCE.read_bytes()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        fail("line.txt is not valid UTF-8")
    if not 1 <= len(text) <= MAX_CHARS:
        fail(f"entry must be 1-{MAX_CHARS} characters, got {len(text)}")
    if not text.strip():
        fail("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        fail("entry must be exactly one line, no embedded newline")
    DEST.parent.mkdir(parents=True, exist_ok=True)
    DEST.write_bytes(raw)
    written = DEST.read_bytes()
    if written != raw:
        fail(
            "verify failed: /output/entry.txt differs from line.txt "
            f"(expected {len(raw)} bytes, got {len(written)})"
        )
    print(f"wrote {len(written)} bytes to {DEST}")


if __name__ == "__main__":
    main()
