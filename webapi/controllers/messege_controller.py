from models.ConversationModel import Conversations
from models.MessegeModel import Messeges
from models.MessegeModel import Messeges
# from bson import ObjectId
from bson.objectid import ObjectId
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import status
from utils.helper import current_date_time
from api_schemas.messege_schema import MessegeSchema
from socket_server import sio_server, getReceiverSocketId
import json

async def send_messege(receiver_id: str, data:MessegeSchema, user_id: str):
    cm = Conversations()
    mm = Messeges()
    msg = {}
    try:
        receiver_socket_id = getReceiverSocketId(receiver_id)
        mm.senderId = ObjectId(user_id)
        mm.receiverId = ObjectId(receiver_id)
        mm.message = data.message
        mm.createdAt = current_date_time()
        mm.updatedAt = current_date_time()
        mm.save()
        msg["_id"] = str(mm.id)
        msg["senderId"] = str(mm.senderId)
        msg["receiverId"]= str(mm.receiverId)
        msg["message"] = mm.message
        msg["createdAt"] = mm.createdAt
        msg["updatedAt"] = mm.updatedAt

        conversation = Conversations.objects(participants__all=[ObjectId(user_id), ObjectId(receiver_id)])
        if conversation:
            conversation.update_one(push__messages=ObjectId(str(mm.id)), set__updatedAt=current_date_time())
            # conversation.messages.append(ObjectId(str(mm.id))) 
        else:
            cm.participants = [ObjectId(user_id), ObjectId(receiver_id)]
            cm.messages = []
            cm.createdAt = current_date_time()
            cm.updatedAt = current_date_time()
            cm.messages.append(ObjectId(str(mm.id)))
            cm.save()
        print(msg)    
        await sio_server.emit('newMessage', json.dumps(msg, default=str), to=receiver_socket_id)    
        return JSONResponse(content=jsonable_encoder({
                "id": str(mm.id),
                "senderId": str(mm.senderId),
                "receiverId": str(mm.receiverId),
                "message": mm.message,
                "createdAt": mm.createdAt,
                "updatedAt": mm.updatedAt
            }), status_code=status.HTTP_201_CREATED)
        
    except Exception as er:
        return JSONResponse(content=jsonable_encoder({"error": f"Something went wrong - {er}" }), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)      


async def get_messegs(userToChatId: str, user_id: str):
    try:
        conversation = Conversations.objects(participants__all=[ObjectId(user_id), ObjectId(userToChatId)])
        if conversation:
            msgs = Messeges.objects(id__in=conversation[0].messages)
            all_messeges = [{"id": str(j.id), "senderId": str(j.senderId), "receiverId": str(j.receiverId), "message": j.message, "createdAt": j.createdAt, "updatedAt": j.updatedAt }for j in msgs]
            return JSONResponse(content=jsonable_encoder(all_messeges), status_code=status.HTTP_200_OK)
        else:
            return JSONResponse(content=jsonable_encoder([]), status_code=status.HTTP_200_OK)
    except Exception as er:       
          return JSONResponse(content=jsonable_encoder({"error": f"Something went wrong - {er}" }), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)      
    

