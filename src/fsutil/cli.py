# src/fsutil/cli.py
import click

@click.group()
def cli() -> None:
    """Root command group for fsutil."""
    pass

@cli.command(name='copy')
@click.argument('src', type=click.Path(exists=True))
@click.argument('dst', type=click.Path())
def copy(src: str, dst: str) -> None:
    """Copy a file from SRC to DST."""
    # Placeholder implementation – actual logic will be added later.
    click.echo(f"Copying {src} to {dst}")

@cli.command(name='delete')
@click.argument('path', type=click.Path(exists=True))
def delete(path: str) -> None:
    """Delete the specified PATH."""
    # Placeholder implementation – actual logic will be added later.
    click.echo(f"Deleting {path}")