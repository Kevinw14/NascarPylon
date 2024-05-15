from pydantic import ConfigDict
from rich import box
from View import View
from Vehicle import Vehicle
from Position import Position
from FlagStatus import FlagStatus
from rich.table import Table
from rich.live import Live


class TerminalView(View):
    table: Table
    live: Live
    model_config = ConfigDict(arbitrary_types_allowed=True)

    def __init__(self, **kw):
        super().__init__(**kw)
        self.live.start()

    @staticmethod
    def __vehicleStatusColor(vehicle: Vehicle) -> str:
        match vehicle.status:
            case 1:
                return vehicle.vehicleNumber
            case 2:
                return f'[yellow]{vehicle.vehicleNumber}[/yellow]'
            case 3:
                return f'[red]{vehicle.vehicleNumber}[/red]'

    @staticmethod
    def __flagStatus(flagStatus: FlagStatus) -> str:
        match flagStatus:
            case FlagStatus.NONE:
                return ''
            case FlagStatus.GREEN:
                return f'[green]{FlagStatus.GREEN.name}[/green]'
            case FlagStatus.CAUTION:
                return f'[yellow]{FlagStatus.CAUTION.name}[/yellow]'
            case FlagStatus.RED:
                return f'[red]{FlagStatus.RED.name}[/red]'
            case FlagStatus.WHITE:
                return FlagStatus.WHITE.name
            case FlagStatus.CHECKERED:
                return FlagStatus.CHECKERED.name
            case FlagStatus.WARMUP:
                return f'[#FFA500]{flagStatus.WARMUP.name}[/#FFA500]'
            case FlagStatus.UNKNOWN:
                return flagStatus.UNKNOWN.name

    def updateVehicle(self, vehicle: Vehicle, i: int, didRecentlyPit: bool, position: Position) -> None:
        self.table.add_row(f'{i + 1}', self.__vehicleStatusColor(vehicle), self.__positionChangeIndicator(position),
                           self.__pitIndicator(didRecentlyPit))

    def updateLapsToGo(self, lapsToGo: int) -> None:
        self.table.caption = f'{lapsToGo} laps to go'

    def updateLapNumber(self, lapNumber: int) -> None:
        self.table.title = f'Lap {lapNumber}'

    def updateLapDownLine(self, vehicle: Vehicle, i: int) -> None:
        self.table.add_section()

    def updateFlagStatus(self, flagStatus: FlagStatus) -> None:
        self.table.title += f' {self.__flagStatus(flagStatus)}'

    @staticmethod
    def __pitIndicator(recentlyPitted: bool) -> str:
        if recentlyPitted:
            return '[blue]•[/blue]'
        return ''

    @staticmethod
    def __positionChangeIndicator(position: Position) -> str:
        match position:
            case Position.GAINED:
                return '[green]|[/green]'
            case Position.LOST:
                return '[red]|[/red]'
            case Position.NONE:
                return ''

    def show(self) -> None:
        self.live.update(self.table)

    def clear(self) -> None:
        self.table: Table = Table(show_header=False, show_footer=False, box=box.SIMPLE)

    def end(self) -> None:
        self.live.stop()
