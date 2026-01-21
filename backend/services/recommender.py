import numpy as np
from backend.utils.loader import (
    load_features,
    load_knn,
    load_raw_songs
)
from typing import List, Dict

def recommend_by_index(song_index: int, n_recommendations: int = 10):
    features_df = load_features()
    knn = load_knn()

    song_vector = features_df.iloc[song_index].values.reshape(1, -1)

    distances, indices = knn.kneighbors(
        song_vector,
        n_neighbors=n_recommendations + 1
    )

    results = []
    for dist, idx in zip(distances[0][1:], indices[0][1:]):
        results.append({
            "index": int(idx),
            "similarity": float(1 - dist)
        })

    return results


def find_song_index(track_name: str, artist_name: str | None = None):
    df = load_raw_songs()

    name_mask = df["track_name"].str.lower().str.contains(
        track_name.lower(),
        na=False
    )

    if artist_name:
        artist_mask = df["artist_name"].str.lower().str.contains(
            artist_name.lower(),
            na=False
        )
        matches = df[name_mask & artist_mask]
    else:
        matches = df[name_mask]

    if matches.empty:
        return None

    return matches.index[0]
from backend.services.feature_utils import average_vectors
from backend.utils.loader import load_knn

def recommend_by_indices(indices: list[int], n_recommendations: int = 10):
    knn = load_knn()

    seed_vector = average_vectors(indices)

    distances, nn_indices = knn.kneighbors(
        seed_vector,
        n_neighbors=n_recommendations + len(indices)
    )

    # remove seeds from results
    recs = []
    for dist, idx in zip(distances[0], nn_indices[0]):
        if idx not in indices:
            recs.append({
                "index": int(idx),
                "similarity": float(1 - dist)
            })
        if len(recs) >= n_recommendations:
            break

    return recs
