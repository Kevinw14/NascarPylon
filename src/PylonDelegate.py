from abc import ABC, abstractmethod
from Vehicle import Vehicle
from FlagStatus import FlagStatus
from Position import Position

class PylonDelegate(ABC):
    @abstractmethod
    def clearScreen(self):
        pass

    @abstractmethod
    def lapNumberUpdated(self, lapNumber: int):
        pass

    @abstractmethod
    def lapsToGoUpdated(self, lapsToGo: int):
        pass

    @abstractmethod
    def flagStatusUpdated(self, flagStatus: FlagStatus):
        pass

    @abstractmethod
    def vehiclePositionUpdated(self, vehicle: Vehicle, i: int):
        pass

    @abstractmethod
    def vehicleDidChangePositions(self, vehicle: Vehicle, i: int, position: Position):
        pass

    @abstractmethod
    def vehicleDidPitRecently(self, vehicle: Vehicle, i: int, didPitRecently: bool):
        pass
    
    @abstractmethod
    def didUpdateLapDownLine(self, vehicle: Vehicle, i: int):
        pass