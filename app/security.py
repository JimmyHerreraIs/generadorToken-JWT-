from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from fastapi import HTTPException
from app.models import User
from jose import jwt,JWTError
from passlib.context import CryptContext

#Salt mi clave que se agregara al token
SECRET_TOKE='DON PATAS'
ALGORITH='HS256'
TIME_TOKEN_VALID=30

pwd_context=CryptContext(schemes=['bcrypt'],deprecated='auto')

#encriptar la contraseña, 
def hash_password(password:str):
    return pwd_context.hash(password)

#Verificar la contraseña
def verify_password(password:str, hash:str):
    return pwd_context.verify(password,hash)

#Crear token
def create_token(data:dict):
    copy=data.copy()
    expire=datetime.utcnow()+timedelta(minutes=TIME_TOKEN_VALID)
    data.update({'exp':expire})
    
    return jwt.encode(copy,SECRET_TOKE,ALGORITH)

#Obtener el estado del usuario
def get_current_user(token:str,db:Session):
    try:
        payload=jwt.decode(token,SECRET_TOKE,ALGORITH)
        username=payload.get('sub')
        
        if username is None:
            raise HTTPException(status_code=401, detail='Verifica que el usuario este correctamente ingresado')
    except JWTError:
        raise HTTPException(status_code=401, detail=('Verifica el token'))
    
    user=db.query(User).filter(User.username==username).first()
    
    if not user: #el usuario gener el token y despues se elimino o baneo
        raise HTTPException(status_code=401, detail=('Verifica el usuario'))
    return user #retornamos todo el objeto, con sus propiedades

#Obtener admin
def get_current_admin(token:str,db:Session):
    user=get_current_user(token,db)
    if not user:
        raise HTTPException(status_code=403, detail='No tienes permisos suficientes')
    return user
