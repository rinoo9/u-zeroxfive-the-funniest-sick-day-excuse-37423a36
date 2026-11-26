#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — make.fun entry.

One line, at most 199 characters, that someone could send to call in sick.
Printed to stdout and written to /output/entry.txt when that directory
is available, as the bounty rules describe.

Craft notes (revision round 2, 26 Nov 2026): the previous line sent the
caller to urgent care over an ironed shirt; this one stays in the home
office instead. The joke works because the escalation is bureaucratic
rather than medical — a cat's random keyboard walk is treated as a
promotion, and the punchline flips the hierarchy: the human now reports
to the cat. Remote-work life makes the absurd promotion feel one small
step from a real standup, which is what makes the excuse land.
"""

import os
import sys

ENTRY = (
    "I can't come in today — my cat walked across my keyboard during "
    "standup, got promoted to team lead, and now I report to her."
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
