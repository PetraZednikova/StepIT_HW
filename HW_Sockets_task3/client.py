import socket
import threading


def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost", 12347))

    def receive_messages():
        while True:
            try:
                message = client_socket.recv(1024).decode("utf-8")
                print(message)
            except:
                print("Disconnect from server.")
                break
    threading.Thread(target=receive_messages).start()

    while True:
        message = input()
        if message:
            client_socket.send(message.encode("utf-8"))

if __name__ == "__main__":
    start_client()