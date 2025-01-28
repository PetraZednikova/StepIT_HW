import socket
import threading

USERS = {
    "alice": "password123",
    "bob": "secret123",
    "charlie": "mypassword"
}

clients = []


def handle_client(client_socket, username):
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                break
            broadcast(f"{username}: {message}", client_socket)
        except:
            # Pokud nastane chyba, odstraň klienta
            remove_client(client_socket, username)
            broadcast(f"{username} opustil chat.", None)
            break


def broadcast(message, sender_socket):
    for client, _ in clients:
        if client != sender_socket:  # Posíláme zprávu všem kromě odesílatele
            try:
                client.send(message.encode("utf-8"))
            except:
                # Pokud nastane chyba při odeslání, klienta odebereme
                remove_client(client, _)


def remove_client(client_socket, username):
    for client, user in clients:
        if client == client_socket:
            clients.remove((client, user))
            break
    client_socket.close()


def authenticate(client_socket):
    client_socket.send("Zadej své uživatelské jméno: ".encode("utf-8"))
    username = client_socket.recv(1024).decode("utf-8").strip()

    client_socket.send("Zadej své heslo: ".encode("utf-8"))
    password = client_socket.recv(1024).decode("utf-8").strip()

    if username in USERS and USERS[username] == password:
        client_socket.send("Autentizace úspěšná.\n".encode("utf-8"))
        return username
    else:
        client_socket.send("Autentizace selhala. Spojení bude ukončeno.\n".encode("utf-8"))
        client_socket.close()
        return None


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 12347))
    server_socket.listen()

    print("Server čeká na spojení...")
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Připojen klient: {addr}")

        username = authenticate(client_socket)
        if username:
            clients.append((client_socket, username))
            broadcast(f"{username} se připojil k chatu", client_socket)
            client_socket.send("Nyní můžeš začít chatovat.\n".encode("utf-8"))

            thread = threading.Thread(target=handle_client, args=(client_socket, username))
            thread.start()


if __name__ == "__main__":
    start_server()
