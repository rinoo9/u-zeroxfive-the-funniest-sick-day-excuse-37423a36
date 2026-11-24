#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — make.fun entry.

One line, at most 199 characters, that someone could send to call in sick.
Printed to stdout and written to /output/entry.txt when that directory
is available, as the bounty rules describe.
"""

import os
import sys

ENTRY = (
    "I can't come in today — my building is being fumigated and the "
    "exterminator said the gas makes people 'chatty and honest,' so I'm "
    "staying home before I tell HR what I really think."
)

MAX_CHARS = 199


def main() -> None:
    if not ENTRY.strip():
        raise SystemExit("entry must not be empty")
    if len(ENTRY) > MAX_CHARS:
        raise SystemExit(f"entry is {len(ENTRY)} chars, over the {MAX_CHARS} limit")
    if len(ENTRY.splitlines()) != 1:
        raise SystemExit("entry must be a single line")
    print(ENTRY)
    print(f"({len(ENTRY)} characters, limit {MAX_CHARS})", file=sys.stderr)
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as fh:
            fh.write(ENTRY)
    except OSError:
        pass


if __name__ == "__main__":
    main()
