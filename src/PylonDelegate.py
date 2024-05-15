from abc import ABC, abstractmethod
from Vehicle import Vehicle
from FlagStatus import FlagStatus
from Position import Position
from pydantic import BaseModel


class PylonDelegate(BaseModel, ABC):
    @abstractmethod
    def didClear(self) -> None:
        pass

    @abstractmethod
    def lapNumberUpdated(self, lapNumber: int) -> None:
        pass

    @abstractmethod
    def lapsToGoUpdated(self, lapsToGo: int) -> None:
        pass

    @abstractmethod
    def flagStatusUpdated(self, flagStatus: FlagStatus) -> None:
        pass

    @abstractmethod
    def vehiclePositionUpdated(self, vehicle: Vehicle, i: int, didRecentlyPit: bool, position: Position) -> None:
        pass

    @abstractmethod
    def didUpdateLapDownLine(self, vehicle: Vehicle, i: int) -> None:
        pass

    @abstractmethod
    def didShow(self):
        pass

    @abstractmethod
    def didEnd(self) -> None:
        pass
