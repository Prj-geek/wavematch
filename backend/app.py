from fastapi import FastAPI

app = FastAPI(title="WaveMatch API"0

@app.get("/")
def health_check():
  return {"status": "OK"}
