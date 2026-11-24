#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes a single sentence (at most 200 characters) explaining the modern
internet to a time traveler from 1800, to /output/entry.txt.

The sentence builds only from things a person from 1800 already knows --
a road, a post office, a library, a market, a letter, ink -- and carries
one picture: one road joining them all, and a letter read at any door
before the ink dries.

Revision: the first draft said a letter "can reach any door", which taken
literally overclaims -- a letter does not travel to a door. The revised
sentence says it "can be read at any door", which is what the internet
actually does, and it puts the single road first so one image carries
the whole sentence.
"""

import os

ENTRY = (
    "Picture one road joining every library, post office, and market "
    "on earth, so a letter you write can be read at any door before "
    "the ink dries."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} characters"
    assert text.count(".") == 1, "entry must be a single sentence"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
