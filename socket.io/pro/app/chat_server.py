# import uvicorn
# import socketio
#
# sio = socketio.AsyncServer(async_mode='asgi')
# app = socketio.ASGIApp(sio, static_files={'/': 'chat_client.html', '/static': 'static'})
#
# # Store client usernames and room information
# usernames = {}
#
# @sio.event
# async def connect(sid, environ):
#     print(f"Client {sid} connected")
#
# @sio.on('join')
# async def join(sid, username):
#     usernames[sid] = username
#     await sio.emit('user list', list(usernames.values()))
#     await sio.emit('system message', f"{username} has joined the chat.")
#     print(f"{username} ({sid}) has joined the chat")
#
# @sio.on('chat message')
# async def chat_message(sid, data):
#     username = usernames.get(sid, 'Anonymous')
#     recipient = data['recipient']
#     message = data['message']
#
#     if recipient in usernames.values():
#         # Send the message only to the specified recipient
#         for sid, name in usernames.items():
#             if name == recipient:
#                 await sio.emit('chat message', f"{username}: {message}", room=sid)
#                 break
#     else:
#         await sio.emit('system message', f"User '{recipient}' not found.")
#
# if __name__ == '__main__':
#     uvicorn.run(app, host='127.0.0.1', port=5000)
import uvicorn
import socketio

sio = socketio.AsyncServer(async_mode='asgi')
app = socketio.ASGIApp(sio, static_files={'/': 'chat_client.html', '/static': 'static'})

# Store client usernames and room information
usernames = {}

@sio.event
async def connect(sid, environ):
    print(f"Client {sid} connected")

@sio.on('join')
async def join(sid, username):
    usernames[sid] = username
    await sio.emit('user list', list(usernames.values()))
    await sio.emit('system message', f"{username} has joined the chat.")
    print(f"{username} ({sid}) has joined the chat")

@sio.on('chat message')
async def chat_message(sid, data):
    username = usernames.get(sid, 'Anonymous')
    recipient = data['recipient']
    message = data['message']

    if recipient in usernames.values():
        # Send the message only to the specified recipient
        for sid, name in usernames.items():
            if name == recipient:
                await sio.emit('chat message', f"{username}: {message}", room=sid)
                break
    else:
        await sio.emit('system message', f"User '{recipient}' not found.")

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=5000)
