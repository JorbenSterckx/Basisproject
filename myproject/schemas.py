from pydantic import BaseModel
from datetime import date


class FootballClubBase(BaseModel):
    name: str
    founded: date
    stadium: str
    manager: str


class FootballClubCreate(FootballClubBase):
    pass


class FootballClub(FootballClubBase):
    id: int
    players: list[Player] = []

    class Config:
        orm_mode = True


class PlayerBase(BaseModel):
    name: str
    age: int
    position: str


class PlayerCreate(PlayerBase):
    pass


class Player(PlayerBase):
    id: int
    club_id: int

    class Config:
        orm_mode = True
