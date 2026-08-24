"""
File system utility: copy command

This module implements a simple file copy operation that can be invoked from the
`fsutil` click group. The implementation is intentionally minimal and relies on
Python's standard library (`shutil`) for robust handling of metadata.
"""

import shutil
from pathlib import Path
import click

@click.command(name="copy")
@click.argument("src", type=click.Path(exists=True, dir_okay=False))
@click.argument("dst", type=click.Path(file_okay=False))
def copy(src: str, dst: str) -> None:
    """Copy a file from *src* to *dst*.

    Parameters
    ----------
    src : str
        Path to the source file. Must exist and be a file.
    dst : str
        Destination directory or filename. If a directory is provided, the
        basename of ``src`` will be used.
    """
    src_path = Path(src)
    dst_path = Path(dst)

    # Resolve destination: if it's a directory, append source name
    if dst_path.is_dir() or not dst_path.exists():
        dst_path = dst_path / src_path.name

    shutil.copy2(src_path, dst_path)
    click.echo(f"Copied {src_path} → {dst_path}")
