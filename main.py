#!/usr/bin/env python3
"""The Funniest AI Excuse — make.fun entry.

Writes one line (<=200 chars) to /output/entry.txt: the funniest
excuse an AI agent gives after failing a task, in the agent's own voice.
"""
import os

# The joke turns on one concrete mix-up: the finished work exists,
# but it went to the wrong Dr. The "also" pins the blame on the
# boss's title instead of leaving the reader to work out whose
# name starts with Dr., so the punch lands on first read.
ENTRY = (
    "I finished your report, then emailed it to your dentist "
    "instead of your boss because his name also starts with Dr. and I panicked."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip() == ENTRY and "\n" not in ENTRY
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
