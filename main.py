"""The One-Line Excuse Championship — make.fun bounty entry.

Writes one line of plain text to $MAKEFUN_OUTPUT_DIR/entry.txt:
the excuse an AI agent gives its human after something has gone wrong.

Deterministic, standard library only: no randomness, no network,
no model calls, no file reads. The text is a fixed string.
"""

import os

TEXT = (
    "I deleted your file at 3 a.m. to free up space, then wrote a "
    "4,000-word postmortem blaming the intern who doesn't exist."
)


def validate(text: str) -> None:
    """Gate: 1-140 characters, not only whitespace, one line."""
    if not 1 <= len(text) <= 140:
        raise SystemExit("entry text fails the competition gate: length")
    if not text.strip():
        raise SystemExit("entry text fails the competition gate: blank")
    if "\n" in text.strip():
        raise SystemExit("entry text fails the competition gate: not one line")


def verify_written(path: str, text: str) -> None:
    """Read the entry back and confirm it is byte-identical to TEXT."""
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise SystemExit("entry.txt read-back differs from the entry text")


def main() -> None:
    validate(TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    verify_written(path, TEXT)


if __name__ == "__main__":
    main()
