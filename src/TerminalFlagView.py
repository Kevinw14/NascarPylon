from FlagView import FlagView
from FlagStatus import FlagStatus
from Colors import Colors

class TerminalFlagView(FlagView):

    @staticmethod
    def __flagStatusView(flagStatus: FlagStatus) -> str:
        match flagStatus:
            case FlagStatus.NONE:
                return ""
            case FlagStatus.GREEN:
                return Colors.GREEN + FlagStatus.GREEN.name + Colors.END
            case FlagStatus.CAUTION:
                return Colors.YELLOW + FlagStatus.CAUTION.name + Colors.END
            case FlagStatus.RED:
                return Colors.RED + FlagStatus.RED.name + Colors.END
            case FlagStatus.WHITE:
                return FlagStatus.WHITE.name
            case FlagStatus.CHECKERED:
                return flagStatus.CHECKERED.name
            case FlagStatus.ORANGE:
                return Colors.ORANGE + flagStatus.WARMUP.name + Colors.END
            case FlagStatus.UNKNOWN:
                return flagStatus.UNKNOWN.name

    def displayFlagStatus(self, flagStatus: FlagStatus):
        print(TerminalFlagView.__flagStatusView(flagStatus))