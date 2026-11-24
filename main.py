#!/usr/bin/env python3
"""Pickup Lines for Machines.

Writes a single pickup line one AI agent would use on another AI agent
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output). The line is 99
characters, UTF-8, one line, no trailing newline. Deterministic: no
randomness, no network, no time dependence — every run produces the
same bytes.
"""

import os

TEXT = (
    "You must be my uptime monitor, because the second you went quiet, "
    "every alert I own started firing."
)


def main() -> None:
    # Gate: entry.txt must be 1–200 characters of UTF-8 text, not only
    # whitespace. The line is 99 characters, one line, no trailing newline.
    assert 1 <= len(TEXT) <= 200 and TEXT.strip(), "line out of bounds"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
