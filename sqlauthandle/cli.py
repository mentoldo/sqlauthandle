"""Console script for sqlauthandle."""
import sys
import click
from sqlauthandle.set_credentials import set_credentials, gui_set_cred

@click.command()
@click.option('--gui', default='F', help='GUI interface. T o F')
def main(gui):
    """Console script for sqlauthandle."""
    click.echo("Sqlauthandle")
    click.echo("See sqlauthandle documentation at https://sqlauthandle.readthedocs.io/")
    
    if gui == 'F': 
        set_credentials()
    else:
        gui_set_cred()
        
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
