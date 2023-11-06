# import uvicorn
#
# import socketio
#
#
# sio = socketio.AsyncServer(async_mode='asgi')
# app = socketio.ASGIApp(sio, static_files={
#     '/': 'latency.html',
#     '/static': 'static',
# })
# # @sio.event
# # async def ping_from_client(sid):
# #     await sio.emit('pong_from_server', room=sid)
#
# @sio.on("send_name")  # This event is triggered when the client sends its name
# async def receive_name(sid, name):
#     # Process the name on the server (you can save it, manipulate it, etc.)
#     print(f"Received name from client: {name}")
#     print(sid)
#
#     # Send the name back to the client
#     # await sio.emit('receive_name', name, room=sid)
#
import json

import uvicorn
import socketio

sio = socketio.AsyncServer(async_mode='asgi')
app = socketio.ASGIApp(sio, static_files={
    '/': 'latency.html',
    '/static': 'static',
})
addsid = {}
addsid_li = []
@sio.event
async def connect(sid, environ):
    print(f"Client {sid} connected")

@sio.on('join')
async def join(sid, frm):
    print(f"Client {frm}:{sid} connected")
    addsid.update({frm: sid})
    print(addsid)

@sio.on('chat message')
async def chat_message(sid, frm, to, msg):
    print(f"Received message from client {frm}: {msg} :{to}:{addsid[to]}")
    await sio.emit('chat message',msg, room=addsid[to])

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=5000)

#
#
# if __name__ == '__main__':
#     uvicorn.run(app, host='127.0.0.1', port=5000)