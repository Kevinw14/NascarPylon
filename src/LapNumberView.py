from abc import ABC, abstractmethod

class LapNumberView(ABC):
    @abstractmethod
    def displayLapNumber(self, lapNumber):
        pass