# src/fsutil/copy.py
"""
Copy subcommand implementation.

This module provides a `copy` command that copies a file from ``src`` to ``dest``.
It validates input paths, supports an optional ``--force`` flag to overwrite an
existing destination, and raises informative :class:`click.ClickException`
instances on error conditions. The command is registered under the root Click
group defined in :mod:`fsutil.cli`.
"""

import shutil
from pathlib import Path

import click

# Import the root CLI group (assumes a package layout where fsutil.cli exists)
try:
    from .cli import cli  # type: ignore
except Exception as exc:  # pragma: no cover - defensive import for CI environments
    raise RuntimeError("Failed to import cli group: {}".format(exc))


@click.command(name="copy")
@click.argument(
    "src",
    type=click.Path(exists=True, file_okay=True, dir_okay=False),
)
@click.argument(
    "dest",
    type=click.Path(file_okay=True, dir_okay=False),
)
@click.option("--force", is_flag=True, help="Overwrite destination if it exists.")
def copy(src: str, dest: str, force: bool = False) -> None:
    """Copy a file from ``src`` to ``dest``.

    Parameters
    ----------
    src : str
        Path to the source file. Must exist and be a regular file.
    dest : str
        Destination path for the copied file.
    force : bool, optional
        If true, overwrite ``dest`` when it already exists.

    Raises
    ------
    click.ClickException
        If validation fails or the copy operation raises an exception.
    """
    src_path = Path(src)
    dest_path = Path(dest)

    # Validate source file
    if not src_path.is_file():
        raise click.ClickException(f"Source '{src}' does not exist or is not a regular file.")

    # Handle destination existence
    if dest_path.exists() and not force:
        raise click.ClickException(
            f"Destination '{dest}' already exists. Use --force to overwrite."
        )

    try:
        shutil.copy2(src, dest)
    except Exception as e:  # pragma: no cover - generic error handling
        raise click.ClickException(f"Failed to copy file: {e}")


# Register the command with the root CLI group.
cli.add_command(copy)
