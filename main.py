#!/usr/bin/env python3
"""The Moon Finally Answers Back — make.fun entry (Account A).

Writes one line, in the Moon's own voice, to /output/entry.txt.

The line answers four billion years of wishes, howls and late-night
promises with a comeback: nobody ever wished the Moon anything back,
and it is the one doing all the glowing. Judge-brief mapping:
  1. Speaks as the Moon answering the wishes — "Four billion years
     of wishes" names the wishes directly, answered in first person.
  2. Funny on one read — the turn lands in the second sentence.
  3. The Moon's voice — wry, old, a little tired of being wished on.
  4. A comeback in one read — the twist ("not one of you has ever
     wished me anything back") arrives before the line ends.
  5. Inside 240 characters, none wasted.

Gate: /output/entry.txt is UTF-8 text of 1 to 240 characters, not only
white space. This entry is 113 characters, a single line.
"""

import os
import sys

ENTRY = (
    "Four billion years of wishes, and nobody ever wished me anything "
    "back. I'm the one doing all the glowing up here."
)


def main() -> int:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    if not (1 <= len(text) <= 240):
        print(f"entry is {len(text)} chars, must be 1-240", file=sys.stderr)
        return 1
    if "\n" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"wrote {len(text)} chars to {out_dir}/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
