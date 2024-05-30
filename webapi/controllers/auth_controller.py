from api_schemas.auth_schema import SignupSchema, LoginSchema
from fastapi.responses import JSONResponse
from fastapi import status
from fastapi.encoders import jsonable_encoder
from models.UserModel import Users
from utils.helper import current_date, hashing, encode_token, check_hash


async def create_profile(data: SignupSchema):
    user_model = Users()
    try:
        if data.password != data.confirmPassword:
            return JSONResponse(content=jsonable_encoder({"error": "Passwords don't match" }), status_code=status.HTTP_400_BAD_REQUEST)
        
        user = Users.objects.filter(username=data.username).first()
        if user:
            return JSONResponse(content=jsonable_encoder({"error": "Username already exists" }), status_code=status.HTTP_400_BAD_REQUEST)
        
        user_model.username = data.username
        user_model.fullName = data.fullName
        user_model.password = hashing(content=data.password)
        user_model.gender = data.gender
        user_model.createdAt = current_date()
        user_model.updatedAt = current_date()
        user_model.save()

        token = encode_token(user_id=str(user_model.id))
        res = JSONResponse(content=jsonable_encoder({"_id": str(user_model.id),
                                                     "fullName": user_model.fullName,
                                                     "username": user_model.username,
                                                     "profilePic": user_model.profilePic,
                                                     "token": token}), status_code=status.HTTP_201_CREATED)


        res.set_cookie(key="jwt", value=token, max_age=15 * 24 * 60 * 60 * 1000)

        return res

    except Exception as er:
        return JSONResponse(content=jsonable_encoder({"error": f"Something went wrong - {er}" }), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
async def signin(data: LoginSchema):
    try:
        user = Users.objects.filter(username=data.username).first()
        if user:
            is_correct_passwd = check_hash(content=data.password, hashed_content=user.password)
            if is_correct_passwd is False:
                return JSONResponse(content=jsonable_encoder({"error": "Invalid password" }), status_code=status.HTTP_400_BAD_REQUEST)
            else:
                token= encode_token(user_id=str(user.id))
                res = JSONResponse(content=jsonable_encoder({"_id": str(user.id),
                                                     "fullName": user.fullName,
                                                     "username": user.username,
                                                     "profilePic": user.profilePic,
                                                     "token": token}), status_code=status.HTTP_200_OK)
                res.set_cookie(key="jwt", value=token, max_age=15 * 24 * 60 * 60 * 1000)
                return res
        else:
            return JSONResponse(content=jsonable_encoder({"error": "User does not exists" }), status_code=status.HTTP_400_BAD_REQUEST)    

    except Exception as er:
        return JSONResponse(content=jsonable_encoder({"error": f"Something went wrong - {er}" }), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    


"""
export const logout = (req, res) => {
	try {
		res.cookie("jwt", "", { maxAge: 0 });
		res.status(200).json({ message: "Logged out successfully" });
	} catch (error) {
		console.log("Error in logout controller", error.message);
		res.status(500).json({ error: "Internal Server Error" });
	}
};
"""

async def signout():
    res = JSONResponse(content=jsonable_encoder({"message": "Logged out successfully"}), status_code=status.HTTP_200_OK)
    res.set_cookie(key="jwt", value="", max_age=0)
    return res
    