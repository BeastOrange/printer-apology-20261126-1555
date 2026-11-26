import os
from pathlib import Path

APOLOGY_LINE = (
    "Sorry I said Tray 2 was empty; there was a ream of cheap paper, but none of it looked appetizing."
)


def main():
    # Runtime guard: ensure single line of 1 to 120 characters before writing
    line = APOLOGY_LINE.strip("\r\n")
    assert "\n" not in line and "\r" not in line, "Line must be a single line"
    assert 1 <= len(line) <= 120, f"Line length must be 1 to 120 chars, got {len(line)}"
    assert not line.isspace(), "Line must not be only whitespace"

    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_file = output_dir / "entry.txt"
    content = f"{line}\n"
    assert 1 <= len(content) <= 120, "Total output length must not exceed 120 characters"

    with open(entry_file, "w", encoding="utf-8") as f:
        f.write(content)


if __name__ == "__main__":
    main()

