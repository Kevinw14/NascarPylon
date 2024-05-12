from abc import ABC, abstractmethod


class LapsToGoView(ABC):
    @abstractmethod
    def displayLapsToGo(self, lapsToGo):
        pass
