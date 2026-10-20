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
    print(f"[{conn}] has joined.")

    connected = True
    
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        
        if msg_length:    
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            
            if msg in DISCONNECT_MESSAGE:
                print(f"[{addr}] has left")
                connected = False
            
            else:
                print(f"[{addr}] {msg}")
                conn.send(f"\n[{addr}] {msg}".encode(FORMAT))
    
    conn.close()

def start():
    server.listen()
    print(f"[SERVER] is up and is on {ADDR}")
    print(f"[PEOPLE ONLINE: {threading.active_count() - 1}]")
   
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[PEOPLE ONLINE: {threading.active_count() - 1}]")

print("Starting Server...")
start()
