from fastapi import APIRouter, Depends
from api_schemas.auth_schema import SignupSchema, LoginSchema
from controllers.auth_controller import create_profile, signin, signout
from utils.helper import auth_wrapper

auth_app = APIRouter(prefix='/api/auth')

@auth_app.post('/signup')
async def signup_route(data: SignupSchema):
    res = await create_profile(data)
    return res

@auth_app.post('/login') 
async def login_route(data: LoginSchema):
    res = await signin(data=data)
    return res   

@auth_app.post('/logout')
async def logout_route(user_id= Depends(auth_wrapper)):
    res = await signout()
    return res