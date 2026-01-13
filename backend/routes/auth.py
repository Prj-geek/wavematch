from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session

from backend.db import SessionLocal
from backend.models.user import User
from backend.utils.security import hash_password

router = APIRouter()

@router.post("/register")
def register(username: str, password: str):
    db: Session = SessionLocal()

    if db.query(User).filter(User.username == username).first():
        raise HTTPException(status_code=400, detail="User exists")

    user = User(
        username=username,
        password_hash=hash_password(password)
    )

    db.add(user)
    db.commit()
    db.refresh(user)
    db.close()

    return {"message": "User created"}
