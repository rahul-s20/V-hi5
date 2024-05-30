from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.auth_route import auth_app
from routes.user_route import user_app
from routes.messege_route import messege_app
from uvicorn import run
from mongoengine import connect
from os import environ as env
from socket_server import sio_app

db = connect(host=env['MONGODB_URI'])

def create_app():
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(auth_app)
    app.include_router(user_app)
    app.include_router(messege_app)
    app.mount('/', app=sio_app)

    return app

app = create_app()

if __name__ == '__main__':
    run(app, reload=True)
