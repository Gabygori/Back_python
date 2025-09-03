from pydantic import BaseModel

class MateriaBase(BaseModel):
    id: str
    nombre: str
    profesor_id: int
    dia_horario: str

class MateriaCreate(MateriaBase):
    pass

class Materia(MateriaBase):
    id: str

    class Config:
        orm_mode = True