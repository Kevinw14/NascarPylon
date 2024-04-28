import os
import time
from ApiClient import ApiClient
from Colors import Colors
from FlagStatus import FlagStatus
from Series import Series

def positionChangeSymbol(oldPostion, newPosition):
    if (newPosition < oldPostion):
        return Colors.GREEN + "|" + Colors.ENDC
    elif (newPosition > oldPostion):
        return Colors.RED + "|" + Colors.ENDC
    else:
        return " "

def flag(flag):
    if (flag == FlagStatus.NONE):
        return ""
    elif (flag == FlagStatus.GREEN):
        return Colors.GREEN + flag.GREEN.name + Colors.ENDC
    elif (flag == FlagStatus.CAUTION):
        return Colors.YELLOW + flag.CAUTION.name + Colors.ENDC
    elif (flag == FlagStatus.RED):
        return Colors.RED + flag.RED.name + Colors.ENDC
    elif (flag == FlagStatus.WHITE):
        return flag.WHITE.name
    elif (flag == FlagStatus.CHECKERED):
        return flag.CHECKERED.name
    elif (flag == FlagStatus.ORANGE):
        return flag.ORANGE.name

# CHANGE THIS TO SEE DIFFERENT SERIES DATA
series = Series.CUP
client = ApiClient()
feed = client.getLiveFeed(series)
positionChange = {}

while feed.lapsToGo > 0:
    os.system('clear')
    i = 1
    print(f'{feed.seriesName} --- {feed.sessionName} at {feed.trackName}')
    print(f'Lap {feed.lapNumber} of {feed.lapsInRace} --- {feed.lapsToGo} Laps To Go --- {flag(feed.flagStatus)} Flag')
    for vehicle in feed.vehicles:
        print(f'{i} {positionChangeSymbol(positionChange.get(vehicle.vehicleNumber, i), i)}{vehicle.vehicleNumber}')
        # Update new postion
        positionChange[vehicle.vehicleNumber] = i
        i += 1
    time.sleep(2)
    feed = client.getLiveFeed(series)