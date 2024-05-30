from pydantic import BaseModel, Field

class SignupSchema(BaseModel):
    fullName: str = Field(...)
    username: str = Field(...) 
    password: str = Field(...)
    confirmPassword: str = Field(...) 
    gender: str = Field(...)

    class Config:
        json_schema_extra={
            "fullName": "first last name",
            "username": "unique_name",
            "password": "password",
            "confirmPassword": "password",
            "gender": "female"
        }

class LoginSchema(BaseModel):
    username: str = Field(...) 
    password: str = Field(...)

    class Config:
        json_schema_extra={
            "username": "unique_name",
            "password": "password"
        }        