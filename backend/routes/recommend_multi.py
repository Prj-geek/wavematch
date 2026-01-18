from fastapi import APIRouter, HTTPException, Depends
from backend.services.recommender import find_song_index, recommend_by_indices
from backend.utils.loader import load_raw_songs
from backend.utils.deps import get_current_user

router = APIRouter()

@router.post("/")
def recommend_multi(
    track_names: list[str],
    limit: int = 10,
    current_user: str = Depends(get_current_user)
):
    if len(track_names) < 2:
        raise HTTPException(status_code=400, detail="Provide at least 2 songs")

    indices = []
    for name in track_names:
        idx = find_song_index(name)
        if idx is None:
            raise HTTPException(status_code=404, detail=f"Song not found: {name}")
        indices.append(idx)

    df = load_raw_songs()
    recs = recommend_by_indices(indices, limit)

    return [
        {
            "track_name": df.iloc[r["index"]]["track_name"],
            "artist_name": df.iloc[r["index"]]["artist_name"],
            "similarity": r["similarity"],
        }
        for r in recs
    ]
