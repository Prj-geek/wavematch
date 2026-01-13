from backend.db import engine, Base
from backend.models.user import User
from backend.models.playlist import Playlist

Base.metadata.create_all(bind=engine)
print("Database initialized")
