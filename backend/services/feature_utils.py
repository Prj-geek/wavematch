import numpy as np
from backend.utils.loader import load_features, load_scaler

def get_song_vector(index: int) -> np.ndarray:
    features = load_features()
    return features.iloc[index].values.reshape(1, -1)


def average_vectors(indices: list[int]) -> np.ndarray:
    features = load_features()
    vectors = features.iloc[indices].values
    return np.mean(vectors, axis=0).reshape(1, -1)


def scale_raw_vector(raw_vector: np.ndarray) -> np.ndarray:
    scaler = load_scaler()
    return scaler.transform(raw_vector)
