from VehicleView import VehicleView
from Colors import Colors
from Vehicle import Vehicle


class TerminalVehicleView(VehicleView):

    @staticmethod
    def __vehicleStatusColor(vehicle: Vehicle) -> str:
        match vehicle.status:
            case 0:
                return vehicle.vehicleNumber
            case 1:
                return Colors.YELLOW + vehicle.vehicleNumber + Colors.END
            case 2:
                return Colors.RED + vehicle.vehicleNumber + Colors.END

    def displayVehicle(self, vehicle: Vehicle, i: int) -> None:
        print(f'{i + 1: <3} {self.__vehicleStatusColor(vehicle): <2}', end=" ")
