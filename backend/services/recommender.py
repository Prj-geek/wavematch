import numpy as np
from backend.utils.loader import (
    load_features,
    load_knn
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
