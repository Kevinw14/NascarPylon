from LapDownView import LapDownView
from Colors import Colors

class TerminalLapDownView(LapDownView):

    def displayLapDownLine(self, vehicle, i):
        print(Colors.CYAN + '-----------' + Colors.END)