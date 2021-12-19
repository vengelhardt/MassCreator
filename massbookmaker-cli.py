import click

import aelf.aelf as aelf
import latex.latex as latex

@click.group()
def cli():
  pass

@cli.command()
@click.option('--date', default='2021-09-05')
@click.option('--zone', default='france')
def first_reading(date, zone):
    aelf.get_first_reading(date, zone)

@cli.command()
@click.option('--date', default='2021-09-05')
@click.option('--zone', default='france')
def second_reading(date, zone):
    aelf.get_second_reading(date, zone)

@cli.command()
@click.option('--date', default='2021-09-05')
@click.option('--zone', default='france')
def evangile(date, zone):
    aelf.get_evangile(date, zone)

@cli.command()
@click.option('--date', default='2021-09-05')
@click.option('--zone', default='france')
def makemassbook(date, zone):
    latex.make_doc(date, zone)
    word.make_word(date, zone)

if __name__ == '__main__':
    cli()
