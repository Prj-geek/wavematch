import json
from datetime import datetime
from pathlib import Path

from backend.config import DATA_DIR

PLAYLIST_DIR = DATA_DIR / "playlists"
PLAYLIST_DIR.mkdir(parents=True, exist_ok=True)

def save_playlist(seed_track, recommendations):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"playlist_{timestamp}.json"
    path = PLAYLIST_DIR / filename

    playlist = {
        "created_at": timestamp,
        "seed_track": seed_track,
        "recommendations": recommendations
    }

    with open(path, "w", encoding="utf-8") as f:
        json.dump(playlist, f, indent=2)

    return filename
