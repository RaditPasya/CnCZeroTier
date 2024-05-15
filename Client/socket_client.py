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
            cls._instance.self_ip = str(os.getenv('SELF_IP'))
            cls._instance.server_address = (cls._instance.server_ip, 12345)
            cls._instance.client_socket = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
            cls._instance.stop_event = threading.Event()  # Initialize stop_event
            cls._instance.receive_thread = None  # Initialize receive_thread
            cls._instance.is_idle = True

        return cls._instance

    def start(self):
        print("Socket started")
        self.client_socket.connect(self.server_address)

        self.receive_thread = threading.Thread(
            target=self.receive_messages, args=(self.client_socket,))
        self.receive_thread.start()

    def send_message_all(self):
        message = input("Enter your message: ")
        self.client_socket.sendall(message.encode())

    def send_message_to(self, message):
        self.client_socket.sendto(
            message.encode(), self._instance.server_address)

    def receive_messages(self, client_socket):
        while not self.stop_event.is_set():
            try:
                message = client_socket.recv(1024).decode('utf-8')
                if message:
                    print(f"Message from server: {message}")
                    self.process_command(message)
                else:
                    break
            except OSError:  # Catch socket errors
                break

    def stop(self):
        self.stop_event.set()  # Set the stop flag
        self.client_socket.close()  # Close the socket
        if self.receive_thread:
            self.receive_thread.join()  # Wait for the thread to finish
        print("Socket stopped")

    def process_command(self, command):
        command = command.lower()
        if command == "check idle":
            self.checking_idle()
        elif command == "scan wifi":
            self.scan_wifi()
        elif command == "crack pin":
            self.crack_pin()
        elif command == "stop client":
            self.stop()
        elif command == "start process":
            self._instance.is_idle = False
        elif command == "end process":
            self._instance.is_idle = True
        else:
            print("Invalid command.")

    def checking_idle(self):
        print("Checking idle...")
        status = "IDLE" if self._instance.is_idle else "NOT IDLE"
        self.send_message_to(f'{self._instance.self_ip} is {status}')
        # Implement the function to check idle

    def scan_wifi(self):
        print("Scanning WiFi...")
        # Implement the function to scan WiFi

    def crack_pin(self):
        print("Cracking PIN...")
        # Implement the function to crack PIN
