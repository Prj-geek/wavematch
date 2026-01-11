from fastapi import APIRouter, HTTPException
from backend.services.recommender import recommend_by_index
from backend.utils.loader import load_raw_songs

router = APIRouter()

@router.get("/")
def recommend(song_index: int, limit: int = 10):
    df = load_raw_songs()

    if song_index < 0 or song_index >= len(df):
        raise HTTPException(status_code=400, detail="Invalid song index")

    recommended_indices = recommend_by_index(song_index, limit)

    recommendations = df.iloc[recommended_indices][
        ["track_name", "artist_name"]
    ]

    return recommendations.to_dict(orient="records")

