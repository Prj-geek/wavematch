# WaveMatch 🎧

WaveMatch is a full-stack music recommendation system that generates
personalized song and playlist recommendations using audio feature
similarity.

## Features

- 🎵 Single-song recommendations
- 🎶 Multi-song (playlist seed) recommendations
- 📊 Cosine similarity with KNN
- 🔐 User authentication with JWT
- 💾 Save and view personal playlists
- ⚡ FastAPI backend + React frontend

## How It Works

1. Spotify audio features are scaled using StandardScaler
2. Songs are represented as numerical vectors
3. Similarity is computed using cosine distance
4. KNN retrieves the closest matches
5. Multiple seed songs are combined by averaging vectors

## Tech Stack

- Backend: FastAPI, scikit-learn, SQLite
- Frontend: React, Context API
- Auth: JWT
- ML: Content-based filtering (KNN)

## Project Status

This project is feature-complete as an MVP and suitable for deployment
and portfolio demonstration.
