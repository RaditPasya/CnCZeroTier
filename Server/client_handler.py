from server_actions import client_names

def handle_client(client_socket, client_address, clients):
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
            clients.remove(client_socket)
            print(f"Current connected clients :  {list(client_names.values())}")
            break
