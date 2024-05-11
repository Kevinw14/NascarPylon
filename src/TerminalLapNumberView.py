from LapNumberView import LapNumberView


class TerminalLapNumberView(LapNumberView):

    def displayLapNumber(self, lap_number: int):
        print(f'Lap {lap_number} ', end=" ")
