import click

@click.command()
def dt():
    click.echo("running dt")


if __name__ == "__main__":
    dt()