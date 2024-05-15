from requests import Response
from ApiClient import ApiClient
from Position import Position
from Vehicle import Vehicle
from PitStop import PitStop
from LiveFeed import LiveFeed
from pydantic import BaseModel
from Series import Series
from PylonDelegate import PylonDelegate
from typing import Optional, Dict
import time


class Pylon(BaseModel):
    series: Series
    delegate: Optional[PylonDelegate] = None
    apiClient: ApiClient = ApiClient()
    positions: Dict[str, int] = {}
    foundLuckyDog: bool = False

    @staticmethod
    def didRecentlyPit(vehicle, lapNumber) -> bool:
        if len(vehicle.pitStops) > 0:
            lastPit: PitStop = vehicle.pitStops[len(vehicle.pitStops) - 1]
            return lapNumber - lastPit.pitInLeaderLap < 5

        return False

    @staticmethod
    def positionChanged(oldPosition, newPosition) -> Position:
        if newPosition < oldPosition:
            return Position.GAINED
        elif newPosition > oldPosition:
            return Position.LOST
        else:
            return Position.NONE

    def setDelegate(self, delegate) -> None:
        self.delegate = delegate

    def run(self) -> None:
        try:
            while True:
                feedResponse: Response = self.apiClient.getLiveFeedResponse(self.series)
                if feedResponse.status_code == 200:
                    feed: LiveFeed = LiveFeed(**feedResponse.json())
                    self.delegate.didClear()
                    self.delegate.lapNumberUpdated(feed.lapNumber)
                    self.delegate.flagStatusUpdated(feed.flagStatus)
                    self.delegate.lapsToGoUpdated(feed.lapsToGo)
                    for i in range(min(40, len(feed.vehicles))):
                        vehicle: Vehicle = feed.vehicles[i]
                        position_changed: Position = self.positionChanged(self.positions.get(vehicle.vehicleNumber, i),
                                                                          i)
                        didRecentlyPit: bool = self.didRecentlyPit(vehicle, feed.lapNumber)
                        self.delegate.vehiclePositionUpdated(vehicle, i, didRecentlyPit, position_changed)
                        self.positions[vehicle.vehicleNumber] = i
                        if vehicle.delta < 0 and not self.foundLuckyDog:
                            self.delegate.didUpdateLapDownLine(vehicle, i)
                            self.foundLuckyDog = True
                    self.delegate.didShow()
                    time.sleep(6)
                    self.foundLuckyDog = False
                else:
                    self.delegate.didClear()
                    break
        except KeyboardInterrupt:
            self.delegate.didEnd()
