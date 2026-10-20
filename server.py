import socket, threading

DISCONNECT_MESSAGE = ["/leave", "/quit", "/bye", "/part", "/exit"]
FORMAT = 'utf-8'
HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW USER] {addr} joined.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:    
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg in DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
    
    conn.close()

def start():
    server.listen()
    print(f"[SERVER] is up and is on {ADDR}")
    print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

print("Starting Server...")
start()
