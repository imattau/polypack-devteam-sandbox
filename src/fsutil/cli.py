# src/fsutil/cli.py
"""fsutil command line interface.

This module provides a Click group named ``cli`` that serves as the root of the
:mod:`fsutil` command line utility. The group is configured with
``invoke_without_command=True`` so that running the command without any subcommand
does not produce the default help output; this satisfies the existing test suite
which expects an empty output when invoking ``cli`` with no arguments.
"""

import click

# The root Click group. Using invoke_without_command=True allows the command
# to be called with no subcommands without printing the default usage/help.
@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    """Root of the fsutil CLI.

    When invoked without a subcommand, this function does nothing and simply
    exits successfully. Subcommands such as ``copy``, ``move`` and ``delete``
    will be added in subsequent feature branches.
    """
    # If no subcommand was supplied, do nothing (exit code 0).
    if ctx.invoked_subcommand is None:
        return

# Placeholder for future commands – they will live in dedicated modules and
# be registered here via ``@cli.command()`` decorators.

if __name__ == "__main__":
    cli()
