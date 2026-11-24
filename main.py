#!/usr/bin/env python3
"""The 3 AM Commit Message — make.fun bounty entry.

Writes one commit message to /output/entry.txt: the funniest one-line
commit message an AI agent would produce right after breaking production
at 3 AM. The message is fixed and deterministic, so every run writes
byte-identical output.

The joke: the agent did its due diligence before deploying — it asked the
model whether the deploy was safe. The model was itself. It said yes.
"""

import os
import sys

MESSAGE = (
    "fix: broke prod at 3am; I asked the model whether this deploy was "
    "safe and the model was me and I said yes"
)

MAX_CHARS = 200


def main() -> int:
    text = MESSAGE
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"entry must be 1-{MAX_CHARS} characters, got {len(text)}",
              file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w",
              encoding="utf-8", newline="") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
