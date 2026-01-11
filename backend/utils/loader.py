import pandas as pd
import joblib

from backend.config import (
    RAW_DATA_PATH,
    FEATURES_PATH,
    KNN_MODEL_PATH,
    SCALER_PATH
)

_raw_df = None
_features_df = None
_knn = None
_scaler = None

def load_raw_songs():
    global _raw_df
    if _raw_df is None:
        _raw_df = pd.read_csv(RAW_DATA_PATH)
    return _raw_df

def load_features():
    global _features_df
    if _features_df is None:
        _features_df = pd.read_csv(FEATURES_PATH)
    return _features_df

def load_knn():
    global _knn
    if _knn is None:
        _knn = joblib.load(KNN_MODEL_PATH)
    return _knn

def load_scaler():
    global _scaler
    if _scaler is None:
        _scaler = joblib.load(SCALER_PATH)
    return _scaler
