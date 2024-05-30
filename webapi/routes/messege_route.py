from fastapi import APIRouter, Depends
from utils.helper import auth_wrapper
from api_schemas.messege_schema import MessegeSchema
from controllers.messege_controller import send_messege, get_messegs

messege_app = APIRouter(prefix='/api/messages')

@messege_app.post('/send/{id}')
async def send_messege_route(id: str, data: MessegeSchema, uid=Depends(auth_wrapper)):
    res = await send_messege(receiver_id=id, data=data, user_id=uid['sub'])
    return res

@messege_app.get('/{id}')
async def get_messegs_route(id: str, uid=Depends(auth_wrapper)):
    res = await get_messegs(id, uid['sub'])
    return res