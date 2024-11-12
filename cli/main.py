import click

@click.command()
def dt():
    click.echo("Running dt!")


if __name__ == "__main__":
    print("Running __main__!")
    dt()
