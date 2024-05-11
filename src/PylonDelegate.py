from abc import ABC, abstractmethod
from Vehicle import Vehicle
from FlagStatus import FlagStatus
from Position import Position


class PylonDelegate(ABC):
    @abstractmethod
    def clearScreen(self):
        pass

    @abstractmethod
    def lapNumberUpdated(self, lap_number: int):
        pass

    @abstractmethod
    def lapsToGoUpdated(self, laps_to_go: int):
        pass

    @abstractmethod
    def flagStatusUpdated(self, flag_status: FlagStatus):
        pass

    @abstractmethod
    def vehiclePositionUpdated(self, vehicle: Vehicle, i: int):
        pass

    @abstractmethod
    def vehicleDidChangePositions(self, vehicle: Vehicle, i: int, position: Position):
        pass

    @abstractmethod
    def vehicleDidPitRecently(self, vehicle: Vehicle, i: int, did_pit_recently: bool):
        pass
