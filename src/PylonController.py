import os
from PylonDelegate import PylonDelegate
from Vehicle import Vehicle
from Position import Position
from FlagStatus import FlagStatus
from LapNumberView import LapNumberView
from FlagView import FlagView
from LapsToGoView import LapsToGoView
from PitView import PitView
from VehicleView import VehicleView
from PositionChangeView import PositionChangeView
from LapDownView import LapDownView
from Pylon import Pylon

class PylonController(PylonDelegate):

    def __init__(self, pylon: Pylon, lapNumberView: LapNumberView, flagView: FlagView, lapsToGo_view: LapsToGoView,
                 vehicleView: VehicleView, positionChangeView: PositionChangeView, pitView: PitView, lapDownView: LapDownView):
        self.__lapNumberView: LapNumberView = lapNumberView
        self.__flagView: FlagView = flagView
        self.__lapsToGoView: LapsToGoView = lapsToGo_view
        self.__vehicleView: VehicleView = vehicleView
        self.__positionChangeView: PositionChangeView = positionChangeView
        self.__pitView: PitView = pitView
        self.__lapDownView: LapDownView = lapDownView
        self.__pylon: Pylon = pylon
        self.__pylon.setDelegate(self)

    def clearScreen(self) -> None:
        os.system('clear')

    def lapNumberUpdated(self, lapNumber: int) -> None:
        self.__lapNumberView.displayLapNumber(lapNumber)

    def lapsToGoUpdated(self, lapsToGo: int) -> None:
        self.__lapsToGoView.displayLapsToGo(lapsToGo)

    def flagStatusUpdated(self, flagStatus: FlagStatus) -> None:
        self.__flagView.displayFlagStatus(flagStatus)

    def vehiclePositionUpdated(self, vehicle: Vehicle, i: int) -> None:
        self.__vehicleView.displayVehicle(vehicle, i)

    def vehicleDidChangePositions(self, vehicle: Vehicle, i: int, position: Position) -> None:
        self.__positionChangeView.displayPositionChange(vehicle, i, position)

    def vehicleDidPitRecently(self, vehicle: Vehicle, i: int, didPitRecently: bool) -> None:
        self.__pitView.displayPitView(vehicle, i, didPitRecently)

    def didUpdateLapDownLine(self, vehicle: Vehicle, i: int):
        self.__lapDownView.displayLapDownLine(vehicle, i)

    def run(self) -> None:
        self.__pylon.run()