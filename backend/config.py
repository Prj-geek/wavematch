from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

MODEL_DIR = BASE_DIR / "models"

RAW_DATA_PATH = RAW_DATA_DIR / "spotify.csv"
FEATURES_PATH = PROCESSED_DATA_DIR / "features.csv"

KNN_MODEL_PATH = MODEL_DIR / "knn_model.pkl"
SCALER_PATH = MODEL_DIR / "scaler.pkl"
