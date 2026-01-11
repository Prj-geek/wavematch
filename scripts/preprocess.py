import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib

from backend.config import (
    RAW_DATA_PATH,
    PROCESSED_DATA_DIR,
    FEATURES_PATH,
    SCALER_PATH
)

FEATURE_COLUMNS = [
    "danceability",
    "energy",
    "loudness",
    "speechiness",
    "acousticness",
    "instrumentalness",
    "liveness",
    "valence",
    "tempo"
]

def main():
    df = pd.read_csv(RAW_DATA_PATH)

    features = df[FEATURE_COLUMNS]

    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)

    features_df = pd.DataFrame(
        scaled_features,
        columns=FEATURE_COLUMNS
    )

    features_df.to_csv(FEATURES_PATH, index=False)
    joblib.dump(scaler, SCALER_PATH)

if __name__ == "__main__":
    main()
