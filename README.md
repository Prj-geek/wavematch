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

📁 Project Structure
wavematch/
├── backend/        # API + ML logic
├── frontend/       # User interface
├── data/           # Dataset
├── models/         # Saved KNN model & scaler
├── notebooks/      # Experiments & EDA
├── scripts/        # Training & preprocessing scripts
└── README.md

▶️ Getting Started
1. Clone the repository
git clone https://github.com/yourusername/wavematch.git
cd wavematch

2. Install dependencies
pip install -r requirements.txt

3. Run the backend
python app.py

📌 Use Cases

Discover songs with a similar vibe

Mood-based playlist generation

Understanding similarity-based recommendation systems

📈 Future Improvements

User profiles and history-based recommendations

Hybrid model (KNN + clustering)

Playlist saving

Deployment (Render / Vercel)

📄 License

This project is licensed under the MIT License.

👤 Author

Priyanshu
Student | Computer Science
Built as a learning-focused machine learning project.
