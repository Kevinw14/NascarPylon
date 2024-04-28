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
        self.trackName = r['track_name']
        self.sessionName = r['run_name']
        self.seriesID = r['series_id']
        match self.seriesID:
            case 1:
                self.seriesName = 'NASCAR Cup Series'
            case 2:
                self.seriesName = 'NASCAR Xfinity Series'
            case 3:
                self.seriesName = 'NASCAR Craftsman Truck Series'
            case _:
                self.sereisName = 'A NASCAR Feeder Series'
