from abc import ABC, abstractmethod
from Vehicle import Vehicle


class VehicleView(ABC):
    @abstractmethod
    def displayVehicle(self, vehicle: Vehicle, i: int):
        pass
