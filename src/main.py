from rich import box
from rich.live import Live
from rich.table import Table
from Pylon import Pylon
from Series import Series
from PylonController import PylonController
from View import View
from TerminalView import TerminalView
import click


@click.command()
@click.option('-s', default='CUP', type=click.Choice(['CUP', 'XFINITY', 'TRUCKS']))
@click.option('-o', default='terminal', type=click.Choice(['terminal', 'pylon']))
def main(s: str, o: str):
    series: Series
    view: View

    match s:
        case 'CUP':
            series = Series.CUP
        case 'XFINITY':
            series = Series.XFINITY
        case 'TRUCKS':
            series = Series.TRUCKS
        case _:
            return

    match o:
        case 'terminal':
            table: Table = Table(box=box.SIMPLE)
            live: Live = Live(table)
            view = TerminalView(live=live, table=table)
        case 'pylon':
            table: Table = Table(box=box.SIMPLE)
            live: Live = Live(table)
            view = TerminalView(live=live, table=table)
        case _:
            return

    pylon: Pylon = Pylon(series=series)
    controller = PylonController(view=view, pylon=pylon)
    controller.run()


if __name__ == '__main__':
    main()
