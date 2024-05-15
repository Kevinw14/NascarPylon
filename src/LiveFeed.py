from typing import List
from FlagStatus import FlagStatus
from Vehicle import Vehicle
from pydantic import BaseModel, Field


class LiveFeed(BaseModel):
    lapNumber: int = Field(alias="lap_number")
    flagStatus: FlagStatus = Field(alias="flag_state")
    lapsInRace: int = Field(alias="laps_in_race")
    lapsToGo: int = Field(alias="laps_to_go")
    vehicles: List[Vehicle] = Field(alias="vehicles")
