from fastapi import FastAPI
from backend.routes.songs import router as songs_router
from backend.routes.auth import router as auth_router
from backend.routes.recommend import router as recommend_router
from backend.routes.search import router as search_router
from backend.routes.playlist import router as playlists_router

app = FastAPI(title="WaveMatch API")

app.include_router(songs_router, prefix="/songs", tags=["songs"])
app.include_router(search_router, prefix="/search", tags=["search"])
app.include_router(recommend_router, prefix="/recommend", tags=["recommend"])
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(playlists_router, prefix="/playlists", tags=["playlists"])

@app.get("/")
def health_check():
    return {"status": "OK"}
