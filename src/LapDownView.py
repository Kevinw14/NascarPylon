from abc import ABC, abstractmethod

class LapDownView(ABC):
    @abstractmethod
    def displayLapDownLine(self, vehicle, i):
        pass