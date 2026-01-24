from fastapi import FastAPI
from backend.routes.songs import router as songs_router
from backend.routes.auth import router as auth_router
from backend.routes.recommend import router as recommend_router
from backend.routes.search import router as search_router
from backend.routes.playlist import router as playlists_router
from backend.routes.recommend_multi import router as recommend_multi_router
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app = FastAPI(title="WaveMatch API")

app.include_router(songs_router, prefix="/songs", tags=["songs"])
app.include_router(search_router, prefix="/search", tags=["search"])
app.include_router(recommend_router, prefix="/recommend", tags=["recommend"])
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(playlists_router, prefix="/playlists", tags=["playlists"])
app.include_router(
    recommend_multi_router,
    prefix="/recommend/multi",
    tags=["recommend"]
)

@app.get("/")
def health_check():
    return {"status": "OK"}

@app.get("/health")
def health():
    return {"status": "ok"}
