

from fastapi import FastAPI, Request, HTTPException, Depends, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from db import get_session
from models import User
from services import auth, user, device
from jose import JWTError


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_db():
    db = get_session()
    try:
        yield db
    finally:
        db.close()


async def get_current_user(token: str = Depends(oauth2_scheme), session: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = auth.decode_token(token)
        username: str = payload.get("username")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    success, user_data = user.get_user_by_username(session, username)
    if user_data is None:
        raise credentials_exception
    return user_data

async def admin_middlweware(current_user: User = Depends(get_current_user)):
    if current_user.account_type != 2:
        raise HTTPException(status_code=403, detail="You are not admin")