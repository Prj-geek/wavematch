from fastapi import APIRouter, HTTPException
from backend.services.recommender import (
    recommend_by_index,
    find_song_index
)
from backend.utils.loader import load_raw_songs

router = APIRouter()

@router.get("/")
def recommend(
    track_name: str,
    artist_name: str | None = None,
    limit: int = 10
):
    song_index = find_song_index(track_name, artist_name)

    if song_index is None:
        raise HTTPException(status_code=404, detail="Song not found")

    df = load_raw_songs()
    recommended_indices = recommend_by_index(song_index, limit)

    recommendations = df.iloc[recommended_indices][
        ["track_name", "artist_name"]
    ]

    return recommendations.to_dict(orient="records")
