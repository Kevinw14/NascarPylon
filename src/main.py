from Pylon import Pylon
from Series import Series
from PylonController import PylonController
from TerminalLapNumberView import TerminalLapNumberView
from TerminalFlagView import TerminalFlagView
from TerminalLapsToGoView import TerminalLapsToGoView
from TerminalVehicleView import TerminalVehicleView
from TerminalPitView import TerminalPitView
from TerminalPositionChangeView import TerminalPositionChangeView
from LapNumberView import LapNumberView
from FlagView import FlagView
from LapsToGoView import LapsToGoView
from VehicleView import VehicleView
from PitView import PitView
from PositionChangeView import PositionChangeView
from LapDownView import LapDownView
from TerminalLapDownView import TerminalLapDownView

if __name__ == '__main__':
    lapNumberView: LapNumberView = TerminalLapNumberView()
    flagView: FlagView = TerminalFlagView()
    lapsToGoView: LapsToGoView = TerminalLapsToGoView()
    vehicleView: VehicleView = TerminalVehicleView()
    pitView: PitView = TerminalPitView()
    lapDownView: LapDownView = TerminalLapDownView()
    positionChangeView: PositionChangeView = TerminalPositionChangeView()

    pylon = Pylon(Series.CUP)
    controller = PylonController(pylon, lapNumberView, flagView, lapsToGoView, vehicleView, positionChangeView, pitView, lapDownView)
    controller.run()
