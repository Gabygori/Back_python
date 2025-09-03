from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from app.database.database import Base

class Inscripcion(Base):
    __tablename__ = "inscripciones"

    alumno_id = Column(Integer, ForeignKey("usuarios.dni"), primary_key=True, index=True)
    materia_id = Column(String(8), ForeignKey("materias.id"), primary_key=True, index=True)

    user = relationship("Usuario", back_populates="inscripciones")
    materia = relationship("Materia", back_populates="inscripciones")