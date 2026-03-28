from fastapi import APIRouter, Depends, HTTPException, Request,Header
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import UserCreate, UserLogin
from app.crud import create_user, get_user_by_username
from app.models import User
from app.security import verify_password, create_token, get_current_admin
from app.utils.logger import log_event

router= APIRouter(prefix='/auth',tags=['Auth'])

#memoria temporal(Luego se pierde)
intentos_fallidos= {}

#Registro
@router.post("/register")
def register(user:UserCreate, db:Session=Depends(get_db)):
    db_user=get_user_by_username(db, user.username)
    
    if db_user:#Evita usuarios duplicados
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    #Crea el user si no existe
    new_user = create_user(db,user.username, user.password)
    return {"msg":"Usuario creado","user":new_user.username}

#Login
@router.post("/login")
def login(user: UserLogin, request:Request,db: Session=Depends(get_db)):
    ip=request.client.host #192.168.2.10
    
    #Bloqueo de intentos 5 veces bloqueado
    if user.username in intentos_fallidos and intentos_fallidos[user.username]>=5:
        log_event('Usuario bloqueado', ip )
        raise HTTPException(status_code=403,detail='Usuario bloqueado temporalmente')
    #Buscarcar user
    db_user=get_user_by_username(db,user.username)
    
    if not db_user or not verify_password(user.password, db_user.password):
        intentos_fallidos[user.username]=intentos_fallidos.get(user.username,0)+1
        log_event("Intentos fallido",ip)
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
        
    intentos_fallidos[user.username]=0
        
    token=create_token({"sub":db_user.username})
        
    log_event("Login exitoso",ip)
        
    return {"access_token":token,
            "token_type":"bearer"}
    
#Ruta solo de admin
@router.get("/admin")
def admin_panel(authorization: str = Header(...), db: Session = Depends(get_db)):
    token = authorization.split(" ")[1]  # Bearer TOKEN

    admin = get_current_admin(token, db)

    return {"msg": f"Bienvenido admin {admin.username}"}