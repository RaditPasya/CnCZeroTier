import socket
import threading
import os
import signal
from dotenv import load_dotenv


class Client:
    _instance = None
    load_dotenv()

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.server_ip = str(os.getenv('RADIT_IP'))
            cls._instance.server_address = (cls._instance.server_ip, 12345)
            cls._instance.client_socket = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
        return cls._instance

    def start(self):
        print("socket started")
        self.client_socket.connect(self.server_address)

        receive_thread = threading.Thread(
            target=self.receive_messages, args=(self.client_socket, self.server_address))
        receive_thread.start()

    def send_message(self):
        message = input("Enter your message: ")
        self.client_socket.sendall(message.encode())

    def receive_messages(self, client_socket, client_address):
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Message from {client_address}: {data.decode()}")
            command = data.decode
            self.process_command(command)

    def process_command(self, command):
        # Convert the command to lowercase for case-insensitive comparison
        command = command.lower()
        # Compare the command with the specified phrases
        if command == "check idle":
            self.checking_idle()
        elif command == "scan wifi":
            self.scan_wifi()
        elif command == "crack pin":
            self.crack_pin()
        else:
            print("Invalid command.")

    def checking_idle(self):
        print("Checking idle...")
        # Call function to check idle

    def scan_wifi(self):
        print("Scanning WiFi...")
        # Call function to scan WiFi

    def crack_pin(self):
        print("Cracking PIN...")
        # Call function to crack PIN
