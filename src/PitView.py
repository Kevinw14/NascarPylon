from abc import ABC, abstractmethod
from Vehicle import Vehicle


class PitView(ABC):
    @abstractmethod
    def displayPitView(self, vehicle: Vehicle, i: int, recentlyPitted: bool):
        pass
