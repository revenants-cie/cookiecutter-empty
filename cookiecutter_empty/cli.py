# -*- coding: utf-8 -*-

"""Console script for cookiecutter_empty."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for cookiecutter_empty."""
    click.echo("Replace this message by putting your code into "
               "cookiecutter_empty.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
