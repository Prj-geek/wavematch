import pandas as pd
from preprocess import prepare_features

def load_data(path);
  return pd.read_csv(path)

if __name__ == "__main__":
    df = load_data("data/songs.csv")
    X_scaled, scaler = prepare_features(df)
    print(X_scaled.shape)
