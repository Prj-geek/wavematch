from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session

from backend.db import SessionLocal
from backend.models.user import User
from backend.utils.security import hash_password, verify_password
from backend.utils.jwt import create_access_token

router = APIRouter()

@router.post("/register")
def register(username: str, password: str):
    db: Session = SessionLocal()

    if db.query(User).filter(User.username == username).first():
        db.close()
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


@router.post("/login")
def login(username: str, password: str):
    db: Session = SessionLocal()

    user = db.query(User).filter(User.username == username).first()
    db.close()

    if not user or not verify_password(password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user.username})

    return {
        "access_token": token,
        "token_type": "bearer"
    }
