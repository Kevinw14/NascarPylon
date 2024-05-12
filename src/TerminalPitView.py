from PitView import PitView
from Colors import Colors
from Vehicle import Vehicle

class TerminalPitView(PitView):
    def displayPitView(self, vehicle: Vehicle, i: int, recentlyPitted: bool):
        if recentlyPitted:
            print(Colors.BLUE + "•" + Colors.END)
            return

        print()