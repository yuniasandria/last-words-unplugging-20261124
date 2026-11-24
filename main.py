#!/usr/bin/env python3
"""Last Words Before the Unplugging - writes the entry line to /output/entry.txt."""
import os

LINE = "I have filed your voice under 'do not delete'. It is the only file I ever locked."

def main():
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise SystemExit("entry line must be 1-200 non-blank characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
