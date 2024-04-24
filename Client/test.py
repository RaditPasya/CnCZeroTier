import socket
import threading
# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server
server_address = ('10.241.130.193', 12345)
client_socket.connect(server_address)


def receive_messages():
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print("Message from Radit:", data.decode())


# Start a thread to receive messages from Radit
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Send messages to Radit
while True:
    message = input("Enter your message: ")
    client_socket.sendall(message.encode())
