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
from Pylon import Pylon


class PylonController(PylonDelegate):

    def __init__(self, pylon: Pylon, lap_number_view: LapNumberView, flag_view: FlagView, laps_to_go_view: LapsToGoView,
                 vehicle_view: VehicleView, position_change_view: PositionChangeView, pit_view: PitView):
        self.__lapNumberView: LapNumberView = lap_number_view
        self.__flagView: FlagView = flag_view
        self.__lapsToGoView: LapsToGoView = laps_to_go_view
        self.__vehicle_view: VehicleView = vehicle_view
        self.__position_change_view: PositionChangeView = position_change_view
        self.__pitView: PitView = pit_view
        self.__pylon: Pylon = pylon
        self.__pylon.setDelegate(self)

    def clearScreen(self) -> None:
        os.system('clear')

    def lapNumberUpdated(self, lap_number: int) -> None:
        self.__lapNumberView.displayLapNumber(lap_number)

    def lapsToGoUpdated(self, laps_to_go: int) -> None:
        self.__lapsToGoView.displayLapsToGo(laps_to_go)

    def flagStatusUpdated(self, flag_status: FlagStatus) -> None:
        self.__flagView.displayFlagStatus(flag_status)

    def vehiclePositionUpdated(self, vehicle: Vehicle, i: int) -> None:
        self.__vehicle_view.displayVehicle(vehicle, i)

    def vehicleDidChangePositions(self, vehicle: Vehicle, i: int, position: Position) -> None:
        self.__position_change_view.displayPositionChange(vehicle, i, position)

    def vehicleDidPitRecently(self, vehicle: Vehicle, i: int, did_pit_recently: bool) -> None:
        self.__pitView.displayPitView(vehicle, i, did_pit_recently)

    def run(self) -> None:
        self.__pylon.run()
