from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine
import os

if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')

#"sqlite:///./sqlitedb/sqlitedata.db"
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/football-clubs/", response_model=schemas.FootballClub)
def create_football_club(football_club: schemas.FootballClubCreate, db: Session = Depends(get_db)):
    return crud.create_football_club(db=db, football_club=football_club)


@app.get("/football-clubs/", response_model=list[schemas.FootballClub])
def read_football_clubs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    football_clubs = crud.get_football_clubs(db, skip=skip, limit=limit)
    return football_clubs


@app.post("/football-clubs/{club_id}/players/", response_model=schemas.Player)
def create_player_for_club(club_id: int, player: schemas.PlayerCreate, db: Session = Depends(get_db)):
    return crud.create_player(db=db, player=player, club_id=club_id)


@app.get("/football-clubs/{club_id}/players/", response_model=list[schemas.Player])
def read_players(club_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    players = crud.get_players(db, club_id, skip=skip, limit=limit)
    return players


@app.delete("/football-clubs/{club_id}/players/{player_id}", response_model=schemas.Player)
def delete_player_from_club(club_id: int, player_id: int, db: Session = Depends(get_db)):
    db_player = db.query(models.Player).filter(
        models.Player.club_id == club_id,
        models.Player.id == player_id
    ).first()

    if db_player is None:
        raise HTTPException(status_code=404, detail="Player not found")

    db.delete(db_player)
    db.commit()
    return db_player
