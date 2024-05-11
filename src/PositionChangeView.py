from abc import ABC, abstractmethod
from Vehicle import Vehicle
from Position import Position


class PositionChangeView(ABC):
    @abstractmethod
    def displayPositionChange(self, vehicle: Vehicle, i: int, position: Position):
        pass
