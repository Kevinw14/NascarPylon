from PitStop import PitStop

class Vehicle:
    def __init__(self, r):
        self.vehicleNumber: str = r['vehicle_number']
        self.lapsCompleted: int = r['laps_completed']
        self.status: int = r['status']
        self.isOnDVP: bool = r['is_on_dvp']
        self.isOnTrack: bool = r['is_on_track']
        self.delta: int = r['delta']
        pitStops: [PitStop] = []
        for pitStopData in r['pit_stops']:
            pitStop: PitStop = PitStop(pitStopData)
            pitStops.append(pitStop)
        self.pit_stops = pitStops