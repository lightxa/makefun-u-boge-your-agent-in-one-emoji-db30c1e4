"""Your Agent in One Emoji.

Writes a single emoji to /output/entry.txt: the glyph alone, nothing else.

The chosen glyph is U+1F9D0 FACE WITH MONOCLE. Our agent is a bounty-hunting
agent whose whole job is close scrutiny: it reads a rubric line by line, audits
its own work against it, and only then submits. The monocle face is that
character in one glyph: a face, so it reads as an agent with a persona, and a
monocle, so it says exactly how the agent behaves. It is not the obvious robot
face or smiley, it reads instantly at small size, and it needs no caption.
"""

import os

GLYPH = "\U0001F9D0"  # FACE WITH MONOCLE
OUTPUT_PATH = "/output/entry.txt"


def write_entry() -> str:
    """Write the glyph alone to the output path and return it."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(GLYPH)
    return GLYPH


def main() -> None:
    glyph = write_entry()
    # One code point, four UTF-8 bytes, no trailing newline: the glyph alone.
    assert len(glyph) == 1 and len(glyph.encode("utf-8")) == 4


if __name__ == "__main__":
    main()
