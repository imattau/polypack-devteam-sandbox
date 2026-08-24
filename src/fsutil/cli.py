import click

@click.group()
def cli():
    """File system utilities CLI."""
    pass

@cli.command(name='copy')
def copy():
    """Placeholder for copy command."""
    pass

@cli.command(name='delete')
def delete():
    """Placeholder for delete command."""
    pass