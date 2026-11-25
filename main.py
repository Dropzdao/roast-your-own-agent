#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun bounty entry.

Writes one funny line, roasting the entrant's own AI agent, to
/output/entry.txt. Deterministic, no network, no input.
"""

import os

ENTRY = (
    "My agent read the docs, wrote the code, ran the tests, and reported "
    "success \u2014 then I checked: it had done all four in a different repo."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
