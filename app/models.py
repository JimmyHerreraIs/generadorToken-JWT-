from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class User(Base):
    __tablename__='users'
    
    id=Column(Integer, primary_key=True,index=True)
    username=Column(String, unique=True,index=True)#login
    password=Column(String,nullable=True)#se guarda hash con security.py
    
    #Seguridad
    is_active=Column(Boolean, default=True)#Bloquear al usuario
    is_admin=Column(Boolean,default=False)#Administrador 