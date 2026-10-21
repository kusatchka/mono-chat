import socket, threading

DISCONNECT_MESSAGE = ["/leave", "/quit", "/bye", "/part", "/exit"]
FORMAT = 'utf-8'
HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
connections = []
usernames = {}


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[{addr}] has joined.")

    connected = True
    first_message = True

    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT) #Checks the length of the message with HEADER
        
        if msg_length:    
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            
            if first_message:
                first_message = False
                username = msg
                usernames.update({addr: username})
                for connection in connections:
                        connection.send(f"[{usernames[addr]}] has joined".encode(FORMAT))
            else: 

                if msg in DISCONNECT_MESSAGE:
                    print(f"[{usernames[addr]}] has left")
                    connections.remove(conn)
                    usernames.pop(addr)
                    connected = False
                
                else:
                    print(f"[{addr}]: {msg}")
                    #conn.send(f"[{addr}]: {msg}".encode(FORMAT))
                    for connection in connections:
                        connection.send(f"[{usernames[addr]}]: {msg}".encode(FORMAT))
            
    
    conn.close()

def start():
    server.listen()
    print(f"[SERVER] is up and is on {ADDR}")
    print(f"[PEOPLE ONLINE: {threading.active_count() - 1}]")
    try:
        while True:
            conn, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            connections.append(conn)
            print(connections)
            thread.start()
            print(f"[PEOPLE ONLINE: {threading.active_count() - 1}]")
    except KeyboardInterrupt:
        server.close()    
        

print("Starting Server...")
start()
