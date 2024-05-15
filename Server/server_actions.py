import os
from dotenv import load_dotenv
import select
from shared_data import client_response_queue
from shared_data import wifi_list_queue
import time
import random

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

def receive_message_from_client(client_socket, timeout=5):
    try:
        ready = select.select([client_socket], [], [], timeout)
        if ready[0]:
            data = client_socket.recv(1024)
            if data:
                print(f"Received message from {client_socket.getpeername()}: {data.decode()}")
            return data.decode()
        else:
            return None
    except Exception as e:
        print(f"Error receiving message from client: {e}")
        return None

def handle_check_idle(clients):
    send_message_to_clients("Check Idle", clients)
    time.sleep(1)
    
    idle_clients = []
    
    
    # Loop through the queue until it's empty
    while not client_response_queue.empty():
        client_socket, message = client_response_queue.get()
        if message == "IDLE":
            idle_clients.append(client_socket)
    
    return idle_clients


def handle_scan_wifi(idle_clients):
    send_message_to_clients("Scan wifi", idle_clients)
    time.sleep(1)
    
    wifi_lists = []
    
    while not wifi_list_queue.empty():
        client_socket, message = wifi_list_queue.get()
        if message:
            wifi_lists.append(message)
    return wifi_lists

def handle_crack_pin(idle_clients):
    pin = generate_pin()
    total_clients = len(idle_clients)
    intervals = distribute(total_clients)
    send_intervals_to_clients(idle_clients, intervals)
    
def send_intervals_to_clients(idle_clients, intervals):
    for i, client_socket in enumerate(idle_clients):
        if i < len(intervals):
            start, end = intervals[i]
            message = f"Your interval is from {start} to {end}"
            try:
                client_socket.sendall(message.encode())
                print(f"Sent to client[{i}]: {message}")
            except Exception as e:
                print(f"Error sending message to client[{i}]: {e}")
    
def generate_pin():
    random_number = random.randint(0, 998)
    return random_number

def distribute(num_users):
    intervals = []
    if num_users <= 0:
        return intervals

    interval_size = 999 // num_users  # Calculate the size of each interval
    remainder = 999 % num_users  # Calculate the remainder

    start = 0
    for i in range(num_users):
        end = start + interval_size - 1
        if remainder > 0:
            end += 1  # Distribute the remainder
            remainder -= 1
        intervals.append((start, end))
        start = end + 1

    return intervals


def process_client_responses():
    while not client_response_queue.empty():
        client_socket, message = client_response_queue.get()
        # Process client responses here
        print(f"Received response from {client_socket.getpeername()}: {message}")

def listen_for_input(server_socket, clients, client_names, shutdown_callback):
    while True:
        try:
            user_input = input("\n 1 - Send Command\n 2 - Show all connected Clients\n\n 0 - Shutdown\n================================\nEnter your choice: ")
            if user_input == '1':
                secondary_input = input("\n 1 - Scan Wifi\n2 - Crack pin\n 3 - send custom message\n\n 0 - stop client\n================================\nEnter your choice: ")
                if secondary_input == '1':
                    idle_clients = handle_check_idle(clients)
                    print("Idle clients:", [client_names.get(client_socket.getpeername()[0], 'Unknown') for client_socket in idle_clients])
                    
                    if idle_clients:
                        wifi_lists = handle_scan_wifi(idle_clients)
                        print("\n\nWifi lists from idle clients:")
                        for wifi_list in wifi_lists:
                            print(wifi_list)
                    else:
                        print("No idle clients found.")
                        
                        
                elif secondary_input == '2':
                    idle_clients = handle_check_idle(clients)
                    print("Idle clients:", [client_names.get(client_socket.getpeername()[0], 'Unknown') for client_socket in idle_clients])
                    
                    
                    if idle_clients:
                        handle_crack_pin(idle_clients)
                    else:
                        print("No idle clients found.")
                    
                elif secondary_input == '3':
                    custom_message = input("Enter the custom message to send to all clients: ")
                    send_message_to_clients(custom_message, clients)
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
                shutdown_callback()
                break
            else:
                print("Invalid input, please try again.")
            


        except KeyboardInterrupt:
            print("\nServer interrupted. Closing...")
            shutdown_callback()
            break
