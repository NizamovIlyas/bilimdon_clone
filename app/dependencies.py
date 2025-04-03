from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session, sessionmaker
from .database import get_db
from .models import User
from .utils import SECRET_KEY, ALGORITHM
from app.database import DATABASE_URL


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


# Dependency to get a DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         user_id: int = payload.get("sub")
#         if user_id is None:
#             raise credentials_exception
#     except JWTError:
#         raise credentials_exception
    
#     user = db.query(User).filter(User.id == user_id).first()
#     if user is None:
#         raise credentials_exception
#     return user

# # Role-based access control
# def require_role(roles: list):
#     def role_checker(user: User = Depends(get_current_user)):
#         if user.role not in roles:
#             raise HTTPException(status_code=403, detail="Not enough permissions")
#         return user
#     return role_checker
