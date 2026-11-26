import os
from pathlib import Path


def main():
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_file = output_dir / "entry.txt"
    line = "Sorry I said Tray 2 was empty; there was a ream of cheap paper, but none of it looked appetizing.\n"
    with open(entry_file, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
