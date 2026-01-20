from fastapi import APIRouter, HTTPException, Depends
from backend.services.recommender import (
    recommend_by_index,
    find_song_index
)
from backend.utils.loader import load_raw_songs
from backend.utils.deps import get_current_user
from sqlalchemy.orm import Session
from backend.db import SessionLocal
from backend.services.playlist_db import save_user_playlist
import logging

logging.basicConfig(level=logging.INFO)


router = APIRouter()
@router.get("/")
def recommend(
    track_name: str,
    artist_name: str | None = None,
    limit: int = 10,
    save: bool = False,
    playlist_name: str | None = None,
    current_user: str = Depends(get_current_user)
):
    logging.info(f"Finding song index for {track_name} by {artist_name}")
    song_index = find_song_index(track_name, artist_name)
    if song_index is None:
        raise HTTPException(status_code=404, detail="Song not found")

    df = load_raw_songs()
    recs = recommend_by_index(song_index, limit)

    response = []
    for rec in recs:
        row = df.iloc[rec["index"]]
        response.append({
            "track_name": row["track_name"],
            "artist_name": row["artist_name"],
            "similarity": rec["similarity"]
        })

    if save:
        db: Session = SessionLocal()
        playlist = save_user_playlist(
            db=db,
            username=current_user,
            name=playlist_name or "My Playlist",
            seed_track={
                "track_name": track_name,
                "artist_name": artist_name
            },
            recommendations=response
        )
        db.close()

        if not playlist:
            raise HTTPException(status_code=400, detail="Could not save playlist")

        return {
            "playlist_id": playlist.id,
            "name": playlist.name,
            "items": response
        }

    return response
