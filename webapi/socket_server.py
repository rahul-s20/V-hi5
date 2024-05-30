import socketio
import json

# sio_server = socketio.AsyncServer(
#     async_mode='asgi',
#     cors_allowed_origins=["http://localhost:3000"],
#     cors_allowed_methods=["GET", "POST"],
#     async_handlers=True
# )

sio_server = socketio.AsyncServer(
    async_mode='asgi',
    cors_allowed_origins=["http://localhost:3000"],
    async_handlers=True
)

sio_app = socketio.ASGIApp(
    socketio_server=sio_server,
    socketio_path='sockets'
)

userSocketMap = {}

@sio_server.event
async def connect(sid, environ, auth):
    print(f'{sid}: user connected')
    user_id = environ['QUERY_STRING'].split('&')[0].split('=')[1]
    userSocketMap[user_id] = sid
    await sio_server.emit('getOnlineUsers', json.dumps(list(userSocketMap.keys())))

@sio_server.event
async def disconnect(sid):
    uid = { k:v for k, v in userSocketMap.items() if v==sid}
    del userSocketMap[list(uid.keys())[0]] 
    await sio_server.emit('getOnlineUsers', json.dumps(list(userSocketMap.keys())))
    print(f'{sid}: user disconnected') 

def getReceiverSocketId(receiverId):
	return userSocketMap[receiverId]


