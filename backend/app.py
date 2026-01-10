from fastapi import FastAPI
from routes.songs import router as songs_router

app = FastAPI(title="WaveMatch API")

app.include_router(songs_router, prefix="/songs", tags=["songs"])

@app.get("/")
def health_check():
  return {"status": "OK"}
