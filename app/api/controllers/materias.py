from sqlalchemy.orm import Session
from app.models.materias import Materia as MateriaModel
from app.models.user import Usuario as User
from app.schemas.materias import MateriaCreate
from fastapi import HTTPException

def create_materia(db: Session, materia: MateriaCreate):
    profesor = db.query(User).filter(User.dni == materia.profesor_id).first()
    if not profesor:
        raise HTTPException(status_code=404, detail="Profesor no encontrado")
    if not profesor.is_profe:
        raise HTTPException(status_code=400, detail="El usuario no es profesor")

    db_materia = MateriaModel(**materia.dict())
    db.add(db_materia)
    try:
        db.commit()
        db.refresh(db_materia)
        return db_materia
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al crear materia: {str(e)}")

def get_materias(db: Session):
    return db.query(MateriaModel).all()
