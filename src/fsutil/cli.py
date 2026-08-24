# src/fsutil/cli.py
"""fsutil command line interface.

This module provides a Click group named `cli` with subcommands for basic filesystem
operations: `list`, `copy`, and `delete`.
"""

import os
import shutil

import click


@click.group()
def cli():
    """Root command group for the filesystem utility."""
    pass


@cli.command(name="list")
@click.argument("path", type=click.Path(exists=True, file_okay=False))
def list_cmd(path):
    """List the names of entries in PATH, one per line."""
    for name in sorted(os.listdir(path)):
        click.echo(name)


@cli.command(name="copy")
@click.argument("src", type=click.Path(exists=True))
@click.argument("dst", type=click.Path())
def copy(src, dst):
    """Copy SRC to DST."""
    try:
        shutil.copy2(src, dst)
    except OSError as exc:
        raise click.ClickException(str(exc))


@cli.command(name="delete")
@click.argument("path", type=click.Path(exists=True))
def delete(path):
    """Delete PATH (a file)."""
    try:
        os.remove(path)
    except OSError as exc:
        raise click.ClickException(str(exc))
