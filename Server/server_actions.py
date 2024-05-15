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
        except Exception as e:
            print(f"Error sending message to client: {e}")

def listen_for_input(server_socket, clients, client_names):
    while True:
        try:
            user_input = input("Enter 1 to send a message to all clients, 2 to show all current connected clients, or 0 to shut down the server: ")
            if user_input == '1':
                secondary_input = input("Enter 1 to send 'check idle' to all clients, or 0 to send 'stop client' to all clients: ")
                if secondary_input == '1':
                    send_message_to_clients("check idle", clients)
                elif secondary_input == '0':
                    send_message_to_clients("stop client", clients)
                else:
                    print("Invalid input, please try again.")
            elif user_input == '2':
                print("Current connected clients:")
                for client_socket in clients:
                    client_address = client_socket.getpeername()
                    client_name = client_names.get(client_address[0], 'Unknown')
                    print(f"{client_name} ({client_address})")
            elif user_input == '0':
                print("Shutting down the server...")
                for client_socket in clients:
                    client_socket.close()
                server_socket.close()
                break
            else:
                print("Invalid input, please try again.")
        except KeyboardInterrupt:
            print("\nServer interrupted. Closing...")
            server_socket.close()
            break

