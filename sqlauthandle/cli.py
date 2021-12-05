"""Console script for sqlauthandle."""
import sys
import click
from sqlauthandle.set_credentials import set_credentials, gui_set_cred

@click.command()
@click.option('--gui', default='F', help='GUI interface. T o F')
def main(gui):
    """Console script for sqlauthandle."""
    click.echo("Replace this message by putting your code into "
               "sqlauthandle.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    
    if gui == 'F': 
        set_credentials()
    else:
        gui_set_cred()
        
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
