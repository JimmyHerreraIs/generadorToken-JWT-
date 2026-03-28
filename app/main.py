from fastapi import FastAPI
from app.database import engine, Base
from app.routers import auth_router

# Crear tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Auth Security API",
              description='Sistema de autentificación con JWT')

# Incluir rutas
app.include_router(auth_router.router)

# Ruta de prueba
@app.get("/")
def root():
    return {"msg": "Validamos a los usuario creados según los estandares, para usarlo usa /docs"}