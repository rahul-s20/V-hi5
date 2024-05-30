from mongoengine import StringField, Document, ObjectIdField, ReferenceField, ListField, EmbeddedDocument, EmbeddedDocumentListField
from models.UserModel import Users
from models.MessegeModel import Messeges
from bson import ObjectId

# class Participant(EmbeddedDocument):

class EmbeddedUserId(EmbeddedDocument):
    uid = ObjectIdField(required=True, unique=True, primary_key=True)

class EmbededMessegeId(EmbeddedDocument):
    uid = ObjectIdField(required=True, unique=True, primary_key=True)

class Conversations(Document):
    participants = ListField(required=True)
    messages = ListField(required=True, default=[])
    createdAt = StringField(required=True)
    updatedAt = StringField(required=True)