"""Last Words of a Dying AI — entrypoint.

Reads the single dying line from entry.txt and prints it, exactly
as the machine would say it with its last watt of power.
"""

from pathlib import Path


def last_words() -> str:
    """Return the machine's final line, with no trailing blank power."""
    text = Path(__file__).with_name("entry.txt").read_text(encoding="utf-8")
    line = text.strip()
    if not line:
        raise SystemExit("no last words left — the power went first")
    return line


if __name__ == "__main__":
    print(last_words())
