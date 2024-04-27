from PitStop import PitStop

class Vehicle:
    def __init__(self, r):
        self.vehicleNumber = r['vehicle_number']
        self.lapsCompleted = r['laps_completed']
        self.passingDifferential = r['passing_differential']
        self.status = r['status']
        self.isOnDVP = r['is_on_dvp']
        self.isOnTrack = r['is_on_track']
        pitstops = []
        for pitstopData in r['pit_stops']:
            pitstop = PitStop(pitstopData)
            pitstops.append(pitstop)
        self.pitstops = pitstops