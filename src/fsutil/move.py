# src/fsutil/move.py
"""Filesystem move utility for the fsutil CLI.

This module provides a simple ``move`` function that wraps :func:`shutil.move` with
basic validation and error handling. It is intended to be used by the Click
command defined in :mod:`src.fsutil.cli`. The logic is deliberately small so it can
be unit‑tested independently from Click.
"""

from __future__ import annotations

import shutil
from pathlib import Path
from typing import Union

PathLike = Union[str, Path]

__all__ = ["move"]


def move(src: PathLike, dst: PathLike) -> None:
    """Move *src* to *dst*.

    Parameters
    ----------
    src : str | pathlib.Path
        The source path. Must exist.
    dst : str | pathlib.Path
        The destination path. Its parent directories will be created if they
        do not already exist.

    Raises
    ------
    FileNotFoundError
        If the source does not exist.
    RuntimeError
        If the underlying move operation fails for any reason.
    """
    src_path = Path(src)
    dst_path = Path(dst)

    if not src_path.exists():
        raise FileNotFoundError(f"Source path {src} does not exist.")

    # Ensure the destination parent exists; this mimics many CLI tools that
    # happily create intermediate directories when moving into a new
    # location.
    dst_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        shutil.move(str(src_path), str(dst_path))
    except Exception as exc:  # pragma: no cover - defensive
        raise RuntimeError(f"Failed to move {src} to {dst}: {exc}") from exc
