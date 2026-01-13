from fastapi import FastAPI
from backend.routes.songs import router as songs_router
from backend.routes.recommend import router as recommend_router
from backend.routes.search import router as search_router

app = FastAPI(title="WaveMatch API")

app.include_router(songs_router, prefix="/songs", tags=["songs"])
app.include_router(search_router, prefix="/search", tags=["search"])
app.include_router(recommend_router, prefix="/recommend", tags=["recommend"])

@app.get("/")
def health_check():
    return {"status": "OK"}
