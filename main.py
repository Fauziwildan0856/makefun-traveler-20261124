import os
import sys

ENTRY = "Every post office, library, and shop in the world is joined by one road of light, and a letter sent along it arrives before the ink is dry."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    with open(path, "r", encoding="utf-8") as handle:
        back = handle.read()
    if back != ENTRY:
        print("read-back mismatch", file=sys.stderr)
        return 1
    if not 1 <= len(ENTRY) <= 200:
        print("entry must be 1 to 200 characters", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
