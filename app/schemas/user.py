from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    dni: int
    nombre: str
    apellido: str
    mail: str
    password: str
    is_profe: int 

class UserCreate(UserBase):
    password: str

class User(UserBase):
    class Config:
        orm_mode = True
        
