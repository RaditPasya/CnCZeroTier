from server_actions import client_names

def handle_client(client_socket, client_address, clients):
    client_name = client_names.get(client_address[0], 'Unknown')  # Get the name corresponding to the client's IP address
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"\n\nMessage from [ {client_name} ]: {data.decode()}")
            # Broadcast the message to other clients
            # for client in clients:
            #     if client != client_socket:
            #         client.sendall(data)
        except ConnectionResetError:
            break

    print(f"{client_name} has disconnected")
    clients.remove(client_socket)
    client_socket.close()

    # Remove the client from client_names
    if client_address[0] in client_names:
        del client_names[client_address[0]]

    print("Current connected clients:")
    for client_socket in clients:
         client_address = client_socket.getpeername()
         client_name = client_names.get(client_address[0], 'Unknown')
         print(f"{client_name} ({client_address})")
