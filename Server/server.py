import os
from dotenv import load_dotenv
import socket
import threading

# Load environment variables from .env file
load_dotenv()

# Dictionary to map IP addresses to names
client_names = {
    os.getenv('FADHIL_IP'): os.getenv('FADHIL_NAME'),
    os.getenv('DYFAN_IP'): os.getenv('DYFAN_NAME'),
    os.getenv('RADIT_IP'): os.getenv('RADIT_NAME'),
    os.getenv('RAIHAN_IP'): os.getenv('RAIHAN_NAME')
}

def handle_client(client_socket, client_address):
    client_name = client_names.get(client_address[0], 'Unknown')  # Get the name corresponding to the client's IP address
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Message from [ {client_name} ]: {data.decode()}")
            # Broadcast the message to other clients
            # for client in clients:
            #     if client != client_socket:
            #         client.sendall(data)
        except ConnectionResetError:
            print(f"{client_name} has disconnected")
            clients.remove(client_name)
            print(f"Current connected clients :  {clients}")
            break

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_address = (os.getenv('RADIT_IP'), 12345)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(5)

clients = []

print('Radit server is listening...')

while True:
    # Wait for a connection
    client_socket, client_address = server_socket.accept()
    client_name = client_names.get(client_address[0], 'Unknown')
    print(f"Connection from {client_name}")
    
    # Add the client name to the list of clients
    clients.append(client_name)
    print(f"Current connected clients :  {clients}")
    
    # Create a thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
