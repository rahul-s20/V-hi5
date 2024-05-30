from fastapi import APIRouter, Depends
from api_schemas.auth_schema import SignupSchema, LoginSchema
from controllers.user_controller import get_users_for_sidebar
from utils.helper import auth_wrapper

user_app = APIRouter(prefix='/api/users')

@user_app.get('')
async def get_other_users(user_id = Depends(auth_wrapper)):
    res = await get_users_for_sidebar(user_id=user_id['sub'])
    return res