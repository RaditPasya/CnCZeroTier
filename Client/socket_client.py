import socket
import threading
import os
import signal
from dotenv import load_dotenv
import scan_wifi
from randomizer import Randomizer


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
            cls._instance.on_cracking = False
            cls._instance.randomizer = Randomizer()
            cls._instance.total_numbers_generated = 0
            cls._instance.total_numbers_to_generate = 0

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
        elif command == "end process":
            self._instance.is_idle = True
            self._instance.on_cracking = False
            self.randomizer.reset()
            print("process ended")
        else:
            if self._instance.is_idle:
                if command == "scan wifi":
                    self.scan_wifi()
                elif command.startswith("start cracking"):
                    print("process started")
                    self._instance.is_idle = False
                    text = command.split()
                    if len(text) >= 6:
                        try:
                            start_num = int(text[3])
                            end_num = int(text[5])
                            self._instance.total_numbers_to_generate = end_num - start_num
                            self.crack_pin(start_num, end_num)
                        except ValueError:
                            print(
                                "Invalid numbers provided for cracking range.")
                    else:
                        print("Invalid start cracking command format.")
                elif command == "stop client":
                    self.stop()
                # elif command == "start process":
                #     self._instance.is_idle = False
                else:
                    print("Invalid command.")
            else:
                print("busy")

    def checking_idle(self):
        print("Checking idle...")
        status = "IDLE" if self._instance.is_idle else "NOT IDLE"
        self.send_message_to(f'{status}')
        # Implement the function to check idle

    def scan_wifi(self):
        print("Scanning WiFi...")
        result = scan_wifi.scan_wifi()
        message = f'{self.self_ip} consists of {" and ".join(result)}'
        self.send_message_to(message)

        # Implement the function to scan WiFi

    def crack_pin(self, start_num, end_num):
        print("Cracking PIN...")
        print(f'randomize from {start_num} to {end_num}')
        self._instance.on_cracking = True
        while (self._instance.total_numbers_generated < self._instance.total_numbers_to_generate and self._instance.on_cracking):
            numbers = self.randomizer.randomize(start_num, end_num)
            print(numbers[0])
            self.send_message_to(f'crack {numbers[0]}\n')
            self._instance.total_numbers_generated += 1
        self._instance.total_numbers_generated = 0
        self._instance.total_numbers_to_generate = 0
        # Implement the function to crack PIN
