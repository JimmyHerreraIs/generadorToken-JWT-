from sqlalchemy.orm import Session
from app.models import User
from app.security import hash_password

#Crear usuario
def create_user(db:Session,username:str,password:str):
    hashed_password=hash_password(password)
    
    new_user=User(
        username=username,
        password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
#Obtener el usuario por el username
def get_user_by_username(db:Session,username:str):
    return db.query(User).filter(User.username==username).first()