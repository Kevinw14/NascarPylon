from abc import ABC, abstractmethod


class FlagView(ABC):
    @abstractmethod
    def displayFlagStatus(self, flag_status):
        pass
