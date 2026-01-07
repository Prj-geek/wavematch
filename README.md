🎧 Wavematch

Wavematch is a content-based music recommendation system that matches songs based on their audio features using the K-Nearest Neighbors (KNN) algorithm.
Instead of relying on popularity or user history, Wavematch focuses on vibe similarity—energy, mood, tempo, and other musical attributes.

🚀 Features

Content-based music recommendations

KNN similarity search on audio features

Mood / vibe-based matching

Simple and interpretable recommendation logic

Modular backend + frontend architecture

🧠 How It Works

Songs are represented as numerical feature vectors (energy, valence, tempo, etc.)

All features are normalized for fair distance comparison

KNN finds the most similar songs using distance metrics

The closest matches are returned as recommendations

🛠 Tech Stack
Backend

Python

Flask / FastAPI

scikit-learn

pandas, numpy

Frontend

HTML, CSS, JavaScript (or React)

ML

K-Nearest Neighbors (KNN)

StandardScaler for feature normalization
