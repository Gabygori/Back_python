from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.inscripciones import InscripcionCreate, Inscripcion as InscripcionResponse
from app.database.database import get_db
from app.api.controllers.inscripciones import create_inscripcion, get_inscripciones_by_alumno, get_inscripciones_by_materia

router = APIRouter(
    prefix="/inscripciones",
    tags=["inscripciones"]
)

@router.post("/", response_model=InscripcionResponse)
def inscribir_alumno(inscripcion: InscripcionCreate, db: Session = Depends(get_db)):
    """
    Inscribir un alumno a una materia.
    """
    return create_inscripcion(db=db, inscripcion=inscripcion)

@router.get("/alumno/{alumno_id}", response_model=list[InscripcionResponse])
def listar_inscripciones_alumno(alumno_id: str, db: Session = Depends(get_db)):
    """
    Listar todas las materias a las que está inscrito un alumno.
    """
    inscripciones = get_inscripciones_by_alumno(db=db, alumno_id=alumno_id)
    if not inscripciones:
        raise HTTPException(status_code=404, detail="No hay inscripciones para este alumno")
    return inscripciones

@router.get("/materia/{materia_id}", response_model=list[InscripcionResponse])
def listar_inscripciones_materia(materia_id: int, db: Session = Depends(get_db)):
    """
    Listar todos los alumnos inscritos en una materia.
    """
    inscripciones = get_inscripciones_by_materia(db=db, materia_id=materia_id)
    if not inscripciones:
        raise HTTPException(status_code=404, detail="No hay inscripciones para esta materia")
    return inscripciones