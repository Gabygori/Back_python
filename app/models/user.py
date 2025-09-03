from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from app.database.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    dni = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    mail = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    is_profe = Column(Integer, nullable=False)

    inscripciones = relationship("Inscripcion", back_populates="user")
    materias = relationship("Materia", secondary="inscripciones", back_populates="estudiantes")
