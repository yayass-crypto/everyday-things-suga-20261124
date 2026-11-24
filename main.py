#!/usr/bin/env python3
"""Everyday Things, Two Lines: a traffic jam explained to a 10-year-old.

Line 1 explains the jam through a single analogy (a stuck zipper).
Line 2 says, in one sentence, what that analogy maps and what it
leaves out. The program writes exactly those two lines to
/output/entry.txt.
"""

from pathlib import Path

LINE_1 = (
    "A traffic jam is a zipper stuck halfway, with every car a tooth "
    "waiting for the one in front to move before it can slide forward."
)
LINE_2 = (
    "The zipper shows why one stopped car freezes the whole line, but "
    "it leaves out that drivers can honk, switch lanes, or turn off, "
    "while zipper teeth can only wait."
)

ENTRY = LINE_1 + "\n" + LINE_2 + "\n"


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")
    text = out.read_text(encoding="utf-8")
    print(text, end="")
    print(
        f"[entry: {len(text)} chars, "
        f"{len(text.encode('utf-8'))} bytes, "
        f"{text.count(chr(10))} lines]"
    )


if __name__ == "__main__":
    main()
