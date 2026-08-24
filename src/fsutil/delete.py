#!/usr/bin/env python3
"""
Delete subcommand implementation for fsutil CLI.
"""

import shutil
from pathlib import Path


def delete_path(path: str | Path) -> None:
    """Delete the given path.

    If *path* refers to a regular file or symlink, it is removed with ``unlink``.  If it
    refers to a directory, it is recursively removed with :func:`shutil.rmtree`.

    Parameters
    ----------
    path : str | Path
        The filesystem path to delete.

    Raises
    ------
    FileNotFoundError
        If the specified path does not exist.
    OSError
        For other OS‑related errors such as permission issues.
    """
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Path '{p}' does not exist")
    try:
        if p.is_file() or p.is_symlink():
            p.unlink()
        elif p.is_dir():
            shutil.rmtree(p)
    except Exception as exc:  # pragma: no cover - defensive
        raise OSError(f"Failed to delete '{p}': {exc}") from exc
