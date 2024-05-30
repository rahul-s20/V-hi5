import bcrypt
from datetime import datetime
from datetime import timedelta
import jwt
from os import environ as env
from fastapi import HTTPException, status, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer, HTTPBasic
from time import time

def hashing(content: str):
    salt = bcrypt.gensalt(10)
    hashed = bcrypt.hashpw(bytes(content, 'utf-8'), salt)
    return hashed.decode("utf-8")


def check_hash(content: str, hashed_content: str) -> bool:
    return bcrypt.checkpw(bytes(content, 'utf-8'), bytes(hashed_content, 'utf-8'))

def current_date() -> str:
    dt = datetime.now().strftime('%m%d%Y')
    return dt


def current_date_time() -> str:
    dt = datetime.now().strftime('%m%d%Y_%H%M%S')
    return dt

def encode_token(user_id):
    payload = {
        'exp': datetime.now() + timedelta(days=7, minutes=5),
        'iat': time(),
        'sub': user_id
    }

    options = {
        'expires': f"{datetime.now() + timedelta(days=7, minutes=5)}",
        'httpOnly': True,
        'sameSite': 'none',
        'secure': True,
    }
    return jwt.encode(
        payload,
        env['JWT_SECRET'],
        algorithm='HS256'
    ), options


def decode_token(token):
    try:
        return jwt.decode(token, env['JWT_SECRET'], algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Signature has expired')
    except jwt.InvalidTokenError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid token')


security = HTTPBearer()
def auth_wrapper(auth: HTTPAuthorizationCredentials= Security(security)):
     return decode_token(auth.credentials)    