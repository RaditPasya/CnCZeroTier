import os
from dotenv import load_dotenv
load_dotenv()
# Dictionary to map IP addresses to names
client_names = {
    os.getenv('FADHIL_IP'): os.getenv('FADHIL_NAME'),
    os.getenv('DYFAN_IP'): os.getenv('DYFAN_NAME'),
    os.getenv('RADIT_IP'): os.getenv('RADIT_NAME'),
    os.getenv('RAIHAN_IP'): os.getenv('RAIHAN_NAME')
}

def send_message_to_clients(message, clients):
    for client_socket in clients:
        try:
            client_socket.sendall(message.encode())
        except:
            # Handle any errors that occur during sending
            pass

def listen_for_input(server_socket, clients, client_names):
    while True:
        try:
            user_input = input("Enter 1 to send 'Hello' message to all clients, or 2 to shut down the server: ")
            if user_input == '1':
                send_message_to_clients("Hello", clients)
            elif user_input == '2':
                print("Shutting down the server...")
                server_socket.close()
                break
        except KeyboardInterrupt:
            print("\nServer interrupted. Closing...")
            server_socket.close()
            break
