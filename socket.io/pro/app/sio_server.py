# # server.py
import socketio
from aiohttp import web
import uvicorn,asyncio

sio = socketio.AsyncServer(cors_allowed_origins="*")
app = web.Application()
# sio = socketio.AsyncServer(async_mode='asgi')
# app = socketio.ASGIApp(sio)
sio.attach(app)


async def app(scope, receive, send):
    pass


# @sio.event
# async def connect(sid, environ):
#     print(f"Client connected: {sid}")

@sio.event
async def connect(sid, environ):
    raise ConnectionRefusedError('authentication failed')


@sio.event
async def disconnect(sid):
    print(f"Client disconnected: {sid}")


@sio.event
async def message(sid, data):
    print(f"Received message from {sid}: {data}")
    await sio.emit('response', f"You said: {data}", room=sid)


async def main():
    config = uvicorn.Config("sio_server:app",host="0.0.0.0", port=8000, log_level="info", timeout_keep_alive=5,access_log=False,reload=True)
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())

# import uvicorn
#
# import socketio
#
# sio = socketio.AsyncServer(async_mode='asgi')
# app = socketio.ASGIApp(sio, static_files={
#     '/': 'latency.html',
#     '/static': 'static',
# })
#
#
# @sio.event
# async def ping_from_client(sid):
#     await sio.emit('pong_from_server', room=sid)
#
#
# if __name__ == '__main__':
#     uvicorn.run(app, host='127.0.0.1', port=8000)
