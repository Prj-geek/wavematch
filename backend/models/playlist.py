from sqlalchemy import Column, Integer, String, ForeignKey, Text
from backend.db import Base

class Playlist(Base):
    __tablename__ = "playlists"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String)
    data = Column(Text)
