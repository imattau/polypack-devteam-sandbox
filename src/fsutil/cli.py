#!/usr/bin/env python3
"""Simple CLI utility for filesystem operations."""
import argparse
from pathlib import Path
import sys


def list_directory(path: Path):
    """Return a sorted list of entries in the directory."""
    return sorted([p.name for p in path.iterdir()])


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="List contents of a directory."
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=Path.cwd(),
        type=Path,
        help="Directory to list (default: current working directory)",
    )
    args = parser.parse_args(argv)

    if not args.path.is_dir():
        print(f"{args.path} is not a directory", file=sys.stderr)
        sys.exit(1)

    for name in list_directory(args.path):
        print(name)


if __name__ == "__main__":
    main()
