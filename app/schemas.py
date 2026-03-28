from pydantic import BaseModel
from typing import Optional

#Clase para crear el usaurio  (registro)
class UserCreate(BaseModel):
    username:str
    password:str
#datos para el login, ingresar
class UserLogin(BaseModel):
    username:str
    password:str
#lo que regreso sin contraseña
class UserResponsive(BaseModel):
    id:int
    username:str
    is_active:bool
    is_admin:bool
    
    class Config:
        from_attributes=True