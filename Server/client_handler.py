from server_actions import client_names, receive_message_from_client
from shared_data import client_response_queue
from shared_data import wifi_list_queue
from shared_data import cracking_queue
import re



def handle_client(client_socket, client_address, clients):
    client_name = client_names.get(client_address[0], 'Unknown')  # Get the name corresponding to the client's IP address
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            message = data.decode()
            #print(f"\n\nMessage from [ {client_name} ]: {message}")

            # Check if the message is related to "Check Idle" or "Scan wifi"
            if message == "IDLE" or message == "NOT IDLE":
                print(">>>>>",client_name, "Is Idle<<<<<")
                client_response_queue.put((client_socket, message))
                
            if "consists of" in message:
                print(f">>>>>{client_name} sent their wifi scan<<<<<")
                wifi_list_queue.put((client_socket, message))
                
            if re.match(r'^crack \d{3}$', message):
                cracking_queue.put((client_socket, message))

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
