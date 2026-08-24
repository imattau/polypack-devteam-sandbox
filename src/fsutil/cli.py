# src/fsutil/cli.py
import click

@click.group()
def cli():
    """Filesystem utility CLI."""
    pass

@cli.command(name="copy")
@click.argument("source", type=click.Path(exists=True))
@click.argument("destination", type=click.Path())
def copy_command(source, destination):
    """Copy a file from SOURCE to DESTINATION."""
    click.echo(f"Copy command called with source={source} and destination={destination}")

@cli.command(name="delete")
@click.argument("path", type=click.Path(exists=True))
def delete_command(path):
    """Delete the file at PATH."""
    click.echo(f"Delete command called on path={path}")

if __name__ == "__main__":
    cli()
