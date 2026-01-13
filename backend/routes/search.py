from fastapi import APIRouter
from backend.utils.loader import load_raw_songs

router = APIRouter()

@router.get("/")
def search(q: str, limit: int = 10):
    df = load_raw_songs()

    mask = df["track_name"].astype(str).str.lower().str.contains(
        q.lower(),
        na=False
    )

    results = df[mask][["track_name", "artist_name"]].head(limit)
    return results.to_dict(orient="records")
