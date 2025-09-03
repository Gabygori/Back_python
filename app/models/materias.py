from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.database import Base

class Materia(Base):
    __tablename__ = "materias"
    id = Column(String(8), primary_key=True, index=True)  # <-- autoincrementable
    profesor_id = Column(Integer, ForeignKey("usuarios.dni"), nullable=False)
    nombre = Column(String(100), nullable=False)
    dia_horario = Column(String(100), nullable=False)

    inscripciones = relationship("Inscripcion", back_populates="materia")
    estudiantes = relationship("Usuario", secondary="inscripciones", back_populates="materias")

# Importación para evitar error de relación
from app.models.inscripciones import Inscripcion