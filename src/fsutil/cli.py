# src/fsutil/cli.py
"""Filesystem utility CLI entry point.

This module defines a minimal Click command group for the skeleton
implementation. The two placeholder subcommands `copy` and `delete`
are provided to satisfy the test suite which verifies that the root
group contains exactly two commands.
"""

import click

@click.group()
def cli() -> None:
    """Root command group for fsutil."""
    pass

@cli.command(name="copy")
@click.argument("src", type=click.Path(exists=True, dir_okay=False))
@click.argument("dst", type=click.Path())
def copy(src: str, dst: str) -> None:
    """Placeholder copy command.

    The real implementation will handle edge cases such as
    overwriting and permission checks. For now it simply prints a
    message so that the CLI is usable during tests.
    """
    click.echo(f"Copying {src} to {dst}")

@cli.command(name="delete")
@click.argument("path", type=click.Path(dir_okay=False))
def delete(path: str) -> None:
    """Placeholder delete command.

    The real implementation will remove the specified file and
    handle errors appropriately. Here we just echo a message for
    test purposes.
    """
    click.echo(f"Deleting {path}")
