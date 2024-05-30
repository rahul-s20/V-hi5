from mongoengine import StringField, Document, ObjectIdField, ReferenceField
from models.UserModel import Users



class Messeges(Document):
    senderId = ObjectIdField(required=True)
    receiverId = ObjectIdField(required=True)
    message = StringField(required=True)
    createdAt = StringField(required=True)
    updatedAt = StringField(required=True)
    