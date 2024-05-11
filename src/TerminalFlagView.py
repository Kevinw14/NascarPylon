from FlagView import FlagView
from FlagStatus import FlagStatus
from Colors import Colors


class TerminalFlagView(FlagView):

    @staticmethod
    def __flagStatusView(flag_status: FlagStatus) -> str:
        match flag_status:
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
                return flag_status.CHECKERED.name
            case FlagStatus.ORANGE:
                return flag_status.ORANGE.name
            case FlagStatus.UNKNOWN:
                return flag_status.UNKNOWN.name

    def displayFlagStatus(self, flag_status: FlagStatus):
        print(TerminalFlagView.__flagStatusView(flag_status))
