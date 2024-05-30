from api_schemas.auth_schema import SignupSchema, LoginSchema
from fastapi.responses import JSONResponse
from fastapi import status
from fastapi.encoders import jsonable_encoder
from models.UserModel import Users
from bson import ObjectId

async def get_users_for_sidebar(user_id: str):
    try:
        users = Users.objects(id__ne=ObjectId(user_id))
        _users = [{'id': str(i.id), 'fullName': i.fullName, 'username': i.username, 'gender': i.gender, 'profilePic': i.profilePic} for i in users]
        if users:
            return JSONResponse(content=jsonable_encoder(_users), status_code=status.HTTP_200_OK) 
        else:
            return JSONResponse(content=jsonable_encoder({"error": "User does not exists" }), status_code=status.HTTP_400_BAD_REQUEST)    
    except Exception as er:
        return JSONResponse(content=jsonable_encoder({"error": f"Something went wrong - {er}" }), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)