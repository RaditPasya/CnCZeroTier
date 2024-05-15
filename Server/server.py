import os
from dotenv import load_dotenv
import socket
import threading
from client_handler import handle_client
from server_actions import listen_for_input, client_names

# Load environment variables from .env file
load_dotenv()

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_address = (os.getenv('RADIT_IP'), 12345)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(5)

clients = []

print('Radit server is listening...')

# Flag to control the server loop
running = True

def server_shutdown():
    global running
    running = False
    for client_socket in clients:
        client_socket.close()
    server_socket.close()

try:
    # Start the input listener in a separate thread
    input_thread = threading.Thread(target=listen_for_input, args=(server_socket, clients, client_names, server_shutdown))
    input_thread.start()

    while running:
        try:
            # Wait for a connection
            client_socket, client_address = server_socket.accept()
            client_name = client_names.get(client_address[0], 'Unknown')
            print(f"Connection from {client_name}")
            
            # Add the client socket to the list of clients
            clients.append(client_socket)
            
            # Create a thread to handle the client
            client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address, clients))
            client_thread.start()
        except OSError:
            # This will catch the error when the socket is closed
            break

except KeyboardInterrupt:
    print("\nServer interrupted. Closing...")
    server_shutdown()

# Ensure the input thread finishes before exiting
input_thread.join()
print("Server has shut down.")
