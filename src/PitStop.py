from pydantic import BaseModel, Field


class PitStop(BaseModel):
    pitInLeaderLap: int = Field(alias="pit_in_leader_lap")
