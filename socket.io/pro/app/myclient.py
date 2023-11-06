import socketio

# Create a Socket.IO client instance
sio = socketio.Client()

# Connect to the Socket.IO server
sio.connect('http://127.0.0.1:8000')  # Replace with your server's URL

# Event handler for connecting to the server
@sio.event
def connect():
    print('Connected to the server')

# Event handler for receiving messages from the server
@sio.on('chat message')
def on_message(data):
    print(f'Received message: {data}')

# Event handler for disconnecting from the server
@sio.event
def disconnect():
    print('Disconnected from the server')

# Function to send a message to the server
def send_message(message):
    sio.emit('chat message', message)

if __name__ == "__main__":
    while True:
        message = input("Enter a message (or 'exit' to quit): ")
        if message == 'exit':
            break
        send_message(message)

# Disconnect from the server when done
sio.disconnect()
