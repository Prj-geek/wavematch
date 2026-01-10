from fastapi import FastAPI

app = FastAPI(title="WaveMatch API")

@app.get("/")
def health_check():
  return {"status": "OK"}
