from PylonDelegate import PylonDelegate
from Vehicle import Vehicle
from Position import Position
from FlagStatus import FlagStatus
from View import View
from Pylon import Pylon


class PylonController(PylonDelegate):
    view: View
    pylon: Pylon

    def __init__(self, **kw):
        super().__init__(**kw)
        self.pylon.delegate = self

    def didClear(self) -> None:
        self.view.clear()

    def lapNumberUpdated(self, lapNumber: int) -> None:
        self.view.updateLapNumber(lapNumber)

    def lapsToGoUpdated(self, lapsToGo: int) -> None:
        self.view.updateLapsToGo(lapsToGo)

    def flagStatusUpdated(self, flagStatus: FlagStatus) -> None:
        self.view.updateFlagStatus(flagStatus)

    def vehiclePositionUpdated(self, vehicle: Vehicle, i: int, didRecentlyPit: bool, position: Position) -> None:
        self.view.updateVehicle(vehicle, i, didRecentlyPit, position)

    def didUpdateLapDownLine(self, vehicle: Vehicle, i: int) -> None:
        self.view.updateLapDownLine(vehicle, i)

    def didShow(self):
        self.view.show()

    def run(self) -> None:
        self.pylon.run()

    def didEnd(self) -> None:
        self.view.end()
