from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class FootballClub(Base):
    __tablename__ = "football_clubs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    founded = Column(Integer)
    stadium = Column(String)
    manager = Column(String)

    players = relationship("Player", back_populates="club")


class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    position = Column(String)
    club_id = Column(Integer, ForeignKey("football_clubs.id"))

    club = relationship("FootballClub", back_populates="players")
