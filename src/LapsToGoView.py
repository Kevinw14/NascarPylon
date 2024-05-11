from abc import ABC, abstractmethod


class LapsToGoView(ABC):
    @abstractmethod
    def displayLapsToGo(self, laps_to_go):
        pass
