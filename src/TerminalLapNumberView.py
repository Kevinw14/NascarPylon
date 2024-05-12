from LapNumberView import LapNumberView

class TerminalLapNumberView(LapNumberView):

    def displayLapNumber(self, lapNumber: int):
        print(f'Lap {lapNumber} ', end=" ")