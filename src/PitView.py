from abc import ABC, abstractmethod
from Vehicle import Vehicle


class PitView(ABC):
    @abstractmethod
    def displayPitView(self, vehicle: Vehicle, i: int, recently_pitted: bool):
        pass
