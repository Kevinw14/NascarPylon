from FlagStatus import FlagStatus
from Vehicle import Vehicle


class LiveFeed:
    def __init__(self, r):
        self.lapNumber = r['lap_number']
        self.flagStatus = FlagStatus(r['flag_state'])
        self.lapsInRace = r['laps_in_race']
        self.lapsToGo = r['laps_to_go']
        vehicles = []
        for vehicleData in r['vehicles']:
            vehicle = Vehicle(vehicleData)
            vehicles.append(vehicle)
        self.vehicles = vehicles
