import numpy as np
from backend.utils.loader import (
    load_features,
    load_knn,
    load_raw_songs
)

def recommend_by_index(song_index: int, n_recommendations: int = 10):
    features_df = load_features()
    knn = load_knn()

    song_vector = features_df.iloc[song_index].values.reshape(1, -1)

    distances, indices = knn.kneighbors(
        song_vector,
        n_neighbors=n_recommendations + 1
    )

    recommended_indices = indices[0][1:]
    return recommended_indices.tolist()

def find_song_index(track_name: str, artist_name: str | None = None):
    df = load_raw_songs()

    if artist_name:
        matches = df[
            (df["track_name"].str.lower() == track_name.lower()) &
            (df["artist_name"].str.lower() == artist_name.lower())
        ]
    else:
        matches = df[
            df["track_name"].str.lower() == track_name.lower()
        ]

    if matches.empty:
        return None

    return matches.index[0]
