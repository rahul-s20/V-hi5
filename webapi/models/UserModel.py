from mongoengine import Document, StringField, EnumField
from enum import Enum

class Gender(Enum):
    Male = "male"
    Female = "female"
    Other = "other"

class Users(Document):
    fullName = StringField(required=True)
    username = StringField(required=True, unique=True)
    password = StringField(required=True, min_length=6)
    gender = EnumField(Gender, required=True)
    profilePic = StringField(default="")
    createdAt = StringField(required=True)
    updatedAt = StringField(required=True)