from pydantic import BaseModel


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


class FootballClubBase(BaseModel):
    name: str
    founded: int
    stadium: str
    manager: str


class FootballClubUpdate(BaseModel):
    name: str | None = None
    founded: int | None = None
    stadium: str | None = None
    manager: str | None = None


class FootballClubCreate(FootballClubBase):
    pass


class FootballClub(FootballClubBase):
    id: int
    players: list[Player] = []

    class Config:
        orm_mode = True