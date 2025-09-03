# app/main.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.database.database import get_db
from app.api.routes import user, materias, inscripciones  # 👈 importa tus routers

# Crear la aplicación FastAPI
app = FastAPI(
    title="Sistema Educativo API",
    description="API para gestionar profesores, alumnos y materias",
    version="1.0.0"
)

# Incluir routers de tu API
app.include_router(user.router)
app.include_router(materias.router)
app.include_router(inscripciones.router)

# Ruta de prueba
@app.get("/")
async def root():
    """Ruta de bienvenida."""
    return {"message": "¡Bienvenido al Sistema Educativo API!"}

# Ruta para probar la conexión a la base de datos
@app.get("/health")
async def health_check(db: Session = Depends(get_db)):
    """Verificar el estado de la aplicación y la base de datos."""
    try:
        db.execute(text("SELECT 1"))  # consulta simple
        return {
            "status": "healthy",
            "database": "connected",
            "message": "La aplicación está funcionando correctamente"
        }
    except Exception as e:
        return {
            "status": "unhealthy",
            "database": "disconnected",
            "error": str(e)
        }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
