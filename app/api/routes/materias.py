from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.materias import Materia, MateriaCreate
from app.database.database import get_db
from app.api.controllers.materias import create_materia as CrearMateria
from app.api.controllers.materias import get_materias as ObtenerMaterias

router = APIRouter(
    prefix="/materias",
    tags=["materias"]
)

@router.get("/", response_model=list[Materia])
def get_materias(db: Session = Depends(get_db)):
    return ObtenerMaterias(db=db)

@router.post("/", response_model=Materia)
def create_materia(materia: MateriaCreate, db: Session = Depends(get_db)):
    return CrearMateria(db=db, materia=materia)