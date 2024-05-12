from ApiClient import ApiClient
from Position import Position
from Vehicle import Vehicle
from PitStop import PitStop
import time


class Pylon:

    def __init__(self, series):
        self.__series = series
        self.__delegate = None
        self.__apiClient = ApiClient()
        self.__positions = {}
        self.__foundLuckyDog = False

    @staticmethod
    def __didRecentlyPit(vehicle, lap_number):
        if len(vehicle.pit_stops) > 0:
            lastPit: PitStop = vehicle.pit_stops[len(vehicle.pit_stops) - 1]
            return lap_number - lastPit.pitInLeaderLap < 5

        return False

    @staticmethod
    def __positionChanged(oldPosition, newPosition):
        if newPosition < oldPosition:
            return Position.GAINED
        elif newPosition > oldPosition:
            return Position.LOST
        else:
            return Position.NONE

    def setDelegate(self, delegate):
        self.__delegate = delegate

    def run(self):
        feed = self.__apiClient.getLiveFeed(self.__series)
        while feed.lapsToGo > 0:
            self.__delegate.clearScreen()
            self.__delegate.lapNumberUpdated(feed.lapNumber)
            self.__delegate.flagStatusUpdated(feed.flagStatus)
            self.__delegate.lapsToGoUpdated(feed.lapsToGo)
            for i in range(min(40, len(feed.vehicles))):
                vehicle: Vehicle = feed.vehicles[i]
                if vehicle.delta < 0 and not self.__foundLuckyDog:
                    self.__delegate.didUpdateLapDownLine(vehicle, i)
                    self.__foundLuckyDog = True
                self.__delegate.vehiclePositionUpdated(vehicle, i)
                position_changed: Position = self.__positionChanged(self.__positions.get(vehicle.vehicleNumber, i), i)
                self.__delegate.vehicleDidChangePositions(vehicle, i, position_changed)
                self.__delegate.vehicleDidPitRecently(vehicle, i, self.__didRecentlyPit(vehicle, feed.lapNumber))
                self.__positions[vehicle.vehicleNumber] = i
            time.sleep(6)
            self.__foundLuckyDog = False
            feed = self.__apiClient.getLiveFeed(self.__series)
