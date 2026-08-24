# src/fsutil/cli.py
"""Command-line interface for the fsutil package.

This module defines a minimal Click command group with two placeholder
subcommands, ``copy`` and ``delete``, which are sufficient for the test
suite to validate that the CLI exposes the expected commands.  The actual
filesystem logic will be implemented in dedicated modules once their
features are fleshed out.
"""

import click


@click.group()
def cli() -> None:
    """Root command group for fsutil.

    The group itself performs no action; it simply provides a namespace
    under which subcommands can be registered.
    """
    pass


@cli.command(name="copy")
@click.argument("src", type=click.Path(exists=True, dir_okay=False))
@click.argument("dst", type=click.Path(dir_okay=False))
def copy(src: str, dst: str) -> None:
    """Placeholder copy command.

    The real implementation will perform a filesystem copy while handling
    overwrites and permissions.  For now the command just echoes the
    operation so that the test suite can confirm its presence.
    """
    click.echo(f"Copying {src} to {dst}")


@cli.command(name="delete")
@click.argument("path", type=click.Path(exists=True, dir_okay=False))
def delete(path: str) -> None:
    """Placeholder delete command.

    The real implementation will remove the specified file while handling
    permission errors.  Currently it simply echoes the action.
    """
    click.echo(f"Deleting {path}")

# End of src/fsutil/cli.py