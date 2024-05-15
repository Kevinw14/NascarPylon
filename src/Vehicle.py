from PitStop import PitStop
from typing import List
from pydantic import BaseModel, Field


class Vehicle(BaseModel):
    vehicleNumber: str = Field(alias="vehicle_number")
    lapsCompleted: int = Field(alias="laps_completed")
    status: int = Field(alias="status")
    isOnDVP: bool = Field(alias="is_on_dvp")
    isOnTrack: bool = Field(alias="is_on_track")
    delta: float = Field(alias="delta")
    pitStops: List[PitStop] = Field(alias="pit_stops")
