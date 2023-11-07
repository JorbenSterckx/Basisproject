from sqlalchemy.orm import Session

import models
import schemas


def create_football_club(db: Session, football_club: schemas.FootballClubCreate):
    db_football_club = models.FootballClub(**football_club.dict())
    db.add(db_football_club)
    db.commit()
    db.refresh(db_football_club)
    return db_football_club


def get_football_clubs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.FootballClub).offset(skip).limit(limit).all()


def get_football_club_by_id(db: Session, club_id: int):
    return db.query(models.FootballClub).filter(models.FootballClub.id == club_id).first()


def create_player(db: Session, player: schemas.PlayerCreate, club_id: int):
    db_player = models.Player(**player.dict(), club_id=club_id)
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player


def get_players(db: Session, club_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Player).filter(models.Player.club_id == club_id).offset(skip).limit(limit).all()


def get_player_by_id(db: Session, player_id: int):
    return db.query(models.Player).filter(models.Player.id == player_id).first()
