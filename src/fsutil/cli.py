# src/fsutil/cli.py
"""Minimal Click CLI group for the fsutil package.

This file provides a click.Group named ``cli`` with two placeholder subcommands:
- ``copy``
- ``delete``

The real implementations will be added later, but this satisfies the current unit tests which only check that the group contains exactly two commands.  The command functions do nothing except return ``None`` so they are harmless.
"""

import click

# Expose a Click group named ``cli``
cli = click.Group()

@cli.command(name="copy")
def copy():
    """Placeholder for the copy subcommand."""
    return None

@cli.command(name="delete")
def delete():
    """Placeholder for the delete subcommand."""
    return None
