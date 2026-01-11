import pandas as pd
import joblib
from sklearn.neighbors import NearestNeighbors

from backend.config import FEATURES_PATH, MODEL_DIR, KNN_MODEL_PATH

def main():
    features_df = pd.read_csv(FEATURES_PATH)

    knn = NearestNeighbors(
        n_neighbors=10,
        metric="cosine",
        algorithm="brute"
    )

    knn.fit(features_df.values)

    MODEL_DIR.mkdir(parents=True, exist_ok=True)
    joblib.dump(knn, KNN_MODEL_PATH)

if __name__ == "__main__":
    main()
