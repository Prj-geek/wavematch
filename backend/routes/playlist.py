import json
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.db import SessionLocal
from backend.models.user import User
from backend.models.playlist import Playlist
from backend.utils.deps import get_current_user

router = APIRouter()

@router.get("/")
def list_my_playlists(current_user: str = Depends(get_current_user)):
    db: Session = SessionLocal()
    user = db.query(User).filter(User.username == current_user).first()

    playlists = []
    if user:
        rows = db.query(Playlist).filter(Playlist.user_id == user.id).all()
        for r in rows:
            playlists.append({
                "id": r.id,
                "name": r.name,
                "data": json.loads(r.data)
            })

    db.close()
    return playlists
