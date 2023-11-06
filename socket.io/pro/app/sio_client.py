# # # client.py
# # import socketio
# #
# # sio = socketio.AsyncClient()
# #
# # @sio.event
# # async def connect():
# #     print("Connected to server")
# #
# # @sio.event
# # async def disconnect():
# #     print("Disconnected from server")
# #
# # @sio.on('response')
# # async def response(data):
# #     print(f"Server response: {data}")
# #
# # async def main():
# #     server_url = 'http://127.0.0.1:8000'  # URL of the server
# #     await sio.connect(server_url)
# #
# #     while True:
# #         message = input("Enter a message (or 'exit' to quit): ")
# #         if message == 'exit':
# #             break
# #         await sio.emit('message', message)
# #
# #     await sio.disconnect()
# # if __name__ == "__main__":
# #     import asyncio
# #     asyncio.run(main())
#
# import socketio
# import asyncio,ssl
#
# sio = socketio.AsyncClient()
#
# @sio.event
# async def connect():
#     print("Connected to server")
#
# @sio.event
# async def disconnect():
#     print("Disconnected from server")
#
# @sio.on('response')
# async def response(data):
#     print(f"Server response: {data}")
#
# async def main():
#     server_url = "http://127.0.0.1:8000"  # URL of the server
#     print(await sio.connect(url=server_url))
#     try:
#
#
#
#         message = input("Enter a message (or 'exit' to quit): ")
#         # if message == 'exit':
#             # break
#         await sio.emit('message', message)
#
#     except Exception as e:
#         print(f"An error occurred: {e}")
#
#     finally:
#         await sio.disconnect()
#
# if __name__ == "__main__":
#     asyncio.run(main())
#
#
# #
# # import asyncio
# # import time
# # import socketio
# #
# # loop = asyncio.get_event_loop()
# # sio = socketio.AsyncClient()
# # start_timer = None
# #
# #
# # async def send_ping():
# #     global start_timer
# #     start_timer = time.time()
# #     await sio.emit('ping_from_client')
# #
# #
# # @sio.event
# # async def connect():
# #     print('connected to server')
# #     await send_ping()
# #
# #
# # @sio.event
# # async def pong_from_server():
# #     global start_timer
# #     latency = time.time() - start_timer
# #     print('latency is {0:.2f} ms'.format(latency * 1000))
# #     await sio.sleep(1)
# #     if sio.connected:
# #         await send_ping()
# #
# #
# # async def start_server():
# #     await sio.connect('http://localhost:8000')
# #     await sio.wait()
# #
# #
# # if __name__ == '__main__':
# #     loop.run_until_complete(start_server())

import socketio
import asyncio

sio = socketio.AsyncClient()

@sio.event
async def connect():
    print("Connected to server")

@sio.event
def connect_error(data):
    print("The connection failed!")

@sio.event
async def disconnect():
    print("Disconnected from the server")

@sio.on('response')
async def response(data):
    print(f"Server response: {data}")

async def main():
    # server_url = "http://127.0.0.1:5000"  # URL of the server

    try:
        await sio.connect('http://127.0.0.1:8000')#'http://127.0.0.1:8000'


        while True:
            message = input("Enter a message (or 'exit' to quit): ")
            if message == 'exit':
                break
            await sio.emit('message', message)

    except asyncio.exceptions.TimeoutError:
        print("The operation timed out. Please try again or check the server.")

# except Exception as e:
    #     print(e)

    finally:
        await sio.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
