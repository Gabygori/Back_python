from pydantic import BaseModel
from typing import Optional
from datetime import date

class InscripcionBase(BaseModel):
    estudiante_id: int
    curso_id: int
    fecha_inscripcion: Optional[date] = None

class InscripcionCreate(InscripcionBase):
    pass

class Inscripcion(InscripcionBase):
    id: int
    class Config:
        orm_mode = True