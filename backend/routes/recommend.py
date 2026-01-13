from fastapi import APIRouter, HTTPException
from backend.services.recommender import (
    recommend_by_index,
    find_song_index
)
from backend.services.playlist_service import save_playlist
from backend.utils.loader import load_raw_songs

router = APIRouter()

@router.get("/")
def recommend(
    track_name: str,
    artist_name: str | None = None,
    limit: int = 10,
    save: bool = False
):
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
        seed = {
            "track_name": track_name,
            "artist_name": artist_name
        }
        filename = save_playlist(seed, response)
        return {
            "saved_as": filename,
            "playlist": response
        }

    return response
