from sqlalchemy.orm import Session
from app.models.user import Usuario as User
from app.models.materias import Materia as MateriaModel
from app.models.inscripciones import Inscripcion 
from app.schemas.inscripciones import InscripcionCreate
from fastapi import HTTPException

def create_inscripcion(db: Session, inscripcion: InscripcionCreate):
    # Verificar que el alumno exista
    alumno = db.query(User).filter(User.dni == inscripcion.alumno_id).first()
    if not alumno:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")

    # Verificar que la materia exista
    materia = db.query(MateriaModel).filter(MateriaModel.id == inscripcion.materia_id).first()
    if not materia:
        raise HTTPException(status_code=404, detail="Materia no encontrada")

    # Verificar que no esté ya inscrito
    existente = db.query(Inscripcion).filter(
        Inscripcion.alumno_id == inscripcion.alumno_id,
        Inscripcion.materia_id == inscripcion.materia_id
    ).first()
    if existente:
        raise HTTPException(status_code=400, detail="El alumno ya está inscrito en esta materia")

    # Crear inscripción
    db_inscripcion = Inscripcion(**inscripcion.dict())
    db.add(db_inscripcion)
    try:
        db.commit()
        db.refresh(db_inscripcion)
        return db_inscripcion
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al inscribir: {str(e)}")

def get_inscripciones_by_alumno(db: Session, alumno_id: str):
    return db.query(Inscripcion).filter(Inscripcion.alumno_id == alumno_id).all()

def get_inscripciones_by_materia(db: Session, materia_id: int):
    return db.query(Inscripcion).filter(Inscripcion.materia_id == materia_id).all()