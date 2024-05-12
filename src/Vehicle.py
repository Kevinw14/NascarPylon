from PitStop import PitStop


class Vehicle:
    def __init__(self, r):
        self.vehicleNumber: str = r['vehicle_number']
        self.lapsCompleted: int = r['laps_completed']
        self.status: int = r['status']
        self.isOnDVP: bool = r['is_on_dvp']
        self.isOnTrack: bool = r['is_on_track']
        self.delta: int = r['delta']
        pit_stops: [PitStop] = []
        for pit_stop_data in r['pit_stops']:
            pit_stop: PitStop = PitStop(pit_stop_data)
            pit_stops.append(pit_stop)
        self.pit_stops = pit_stops
