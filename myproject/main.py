from fastapi import Depends, FastAPI, HTTPException, Query, Path
from sqlalchemy.orm import Session

import os
import crud
import models
import schemas
from database import SessionLocal, engine

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
def read_football_club(skip: int = Query(0, title="Skip items", ge=0), limit: int = Query(100, title="Limit items", ge=1, le=1000), db: Session = Depends(get_db)):
    football_clubs = crud.get_football_clubs(db, skip=skip, limit=limit)
    return football_clubs


@app.post("/football-clubs/{club_id}/players/", response_model=schemas.Player)
def create_player_for_club(club_id: int, player: schemas.PlayerCreate, db: Session = Depends(get_db)):
    return crud.create_player(db=db, player=player, club_id=club_id)


@app.get("/football-clubs/{club_id}/players/", response_model=list[schemas.Player])
def read_player(club_id: int, skip: int = Query(0, title="Skip items", ge=0), limit: int = Query(100, title="Limit items", ge=1, le=1000), db: Session = Depends(get_db)):
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


@app.get("/football-clubs/{club_id}", response_model=schemas.FootballClub)
def get_football_clubs(club_id: int = Path(..., title="ID of the football club", ge=1), db: Session = Depends(get_db)):
    db_club = crud.get_football_club_by_id(db, club_id)

    if db_club is None:
        raise HTTPException(status_code=404, detail="Football club not found")

    return db_club


@app.get("/players/{player_id}", response_model=schemas.Player)
def get_players(player_id: int = Path(..., title="ID of the player", ge=1), db: Session = Depends(get_db)):
    db_player = crud.get_player_by_id(db, player_id)

    if db_player is None:
        raise HTTPException(status_code=404, detail="Player not found")

    return db_player


@app.delete("/football-clubs/{club_id}", response_model=schemas.FootballClub)
def delete_football_club(club_id: int = Path(..., title="ID of the football club", ge=1), db: Session = Depends(get_db)):
    db_club = db.query(models.FootballClub).filter(
        models.FootballClub.id == club_id
    ).first()

    if db_club is None:
        raise HTTPException(status_code=404, detail="Football club not found")

    db.delete(db_club)
    db.commit()
    return db_club


@app.patch("/football-clubs/{club_id}", response_model=schemas.FootballClub)
def partial_update_football_club(club_id: int, club_data: schemas.FootballClubUpdate, db: Session = Depends(get_db)):
    db_club = crud.get_football_club_by_id(db, club_id)

    if db_club is None:
        raise HTTPException(status_code=404, detail="Football club not found")

    # Update only the provided attributes
    for key, value in club_data.dict().items():
        if value is not None:
            setattr(db_club, key, value)

    db.commit()
    db.refresh(db_club)
    return db_club


@app.put("/football-clubs/{club_id}", response_model=schemas.FootballClub)
def update_football_club(club_id: int, club_data: schemas.FootballClubUpdate, db: Session = Depends(get_db)):
    db_club = crud.get_football_club_by_id(db, club_id)

    if db_club is None:
        raise HTTPException(status_code=404, detail="Football club not found")

    # Update the club's attributes
    for key, value in club_data.dict().items():
        setattr(db_club, key, value)

    db.commit()
    db.refresh(db_club)
    return db_club
