import pandas as pd
from sklearn.preprocessing import StandardScaler

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

def prepare_features(df):
    X = df[FEATURE_COLUMNS]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled, scaler
