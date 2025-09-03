from sqlalchemy.orm import Session
from app.models.user import Usuario as User
from app.schemas.user import UserCreate
from fastapi import HTTPException

# --- Usuarios ---
def create_user(db: Session, user: UserCreate):
    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session):
    return db.query(User).all()