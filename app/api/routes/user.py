from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import User, UserCreate
from app.database.database import get_db
from app.api.controllers.user import create_user as CrearUsuario
from app.api.controllers.user import get_users as ObtenerUsuarios

router = APIRouter(
    prefix="/users",
    tags=["users"]
    
    
)

@router.get("/", response_model=list[User])
def get_users(db: Session = Depends(get_db)):
    return ObtenerUsuarios(db=db)


@router.post("/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return CrearUsuario(db=db, user=user)


#crear ruta para materias y usuario-materias