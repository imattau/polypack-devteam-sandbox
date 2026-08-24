# src/fsutil/cli.py
"""Minimal filesystem utility CLI skeleton.

This module provides a Click group named `cli` with two placeholder subcommands:
- `copy`: echoes the source and destination paths.
- `delete`: echoes the path to be deleted.

The commands are intentionally simple so that the test suite can invoke them without performing real file operations.
"""

import click

@click.group()
def cli():
    """Root command group for the filesystem utility."""
    pass

@cli.command(name="copy")
@click.argument("src", type=click.Path())
@click.argument("dst", type=click.Path())
def copy(src, dst):
    """Placeholder copy command.

    In a full implementation this would copy ``src`` to ``dst``.  For now it simply prints the intended action.
    """
    click.echo(f"Copying {src} to {dst}")

@cli.command(name="delete")
@click.argument("path", type=click.Path())
def delete(path):
    """Placeholder delete command.

    In a full implementation this would delete ``path``.  For now it simply prints the intended action.
    """
    click.echo(f"Deleting {path}")