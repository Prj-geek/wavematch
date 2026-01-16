import json
from sqlalchemy.orm import Session

from backend.models.user import User
from backend.models.playlist import Playlist

def save_user_playlist(
    db: Session,
    username: str,
    name: str,
    seed_track: dict,
    recommendations: list[dict],
):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return None

    payload = {
        "seed_track": seed_track,
        "recommendations": recommendations
    }

    playlist = Playlist(
        user_id=user.id,
        name=name,
        data=json.dumps(payload)
    )

    db.add(playlist)
    db.commit()
    db.refresh(playlist)
    return playlist
