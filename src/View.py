from abc import ABC, abstractmethod
from Vehicle import Vehicle
from Position import Position
from FlagStatus import FlagStatus
from pydantic import BaseModel


class View(BaseModel, ABC):

    @abstractmethod
    def updateLapsToGo(self, lapsToGo: int) -> None:
        pass

    @abstractmethod
    def updateLapNumber(self, lapNumber: int) -> None:
        pass

    @abstractmethod
    def updateLapDownLine(self, vehicle: Vehicle, i: int) -> None:
        pass

    @abstractmethod
    def updateFlagStatus(self, flagStatus: FlagStatus) -> None:
        pass

    @abstractmethod
    def updateVehicle(self, vehicle: Vehicle, i: int, didRecentlyPit: bool, position: Position) -> None:
        pass

    @abstractmethod
    def show(self) -> None:
        pass

    @abstractmethod
    def clear(self) -> None:
        pass

    @abstractmethod
    def end(self) -> None:
        pass
