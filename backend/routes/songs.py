from fastapi import APIRouter
from utils.loader import load_raw_songs

router = APIRouter()

@router.get("/")
def get_songs():
    df = load_raw_songs()
    songs = df[["track_name", "artist_name"]].head(limit)
    return songs.to_dict(orient="records")
