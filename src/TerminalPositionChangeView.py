from PositionChangeView import PositionChangeView
from Colors import Colors
from Position import Position
from Vehicle import Vehicle


class TerminalPositionChangeView(PositionChangeView):

    def displayPositionChange(self, vehicle: Vehicle, i: int, position: Position):
        match position:
            case Position.GAINED:
                print(Colors.GREEN + "|" + Colors.END, end=" ")
            case Position.LOST:
                print(Colors.RED + "|" + Colors.END, end=" ")
            case Position.NONE:
                print(" ", end=" ")
