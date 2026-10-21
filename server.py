import socket, threading

DISCONNECT_MESSAGE = ["/leave", "/quit", "/bye", "/part", "/exit"]
COMMANDS = ["/list"]
FORMAT = 'utf-8'
HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
connections = []
server_usernames = {}
client_usernames = {} #Reversed server_usernames


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
                server_usernames.update({addr: username})
                client_usernames.update({username: addr})
                
                for connection in connections:
                        connection.send(f"[{server_usernames[addr]}] has joined".encode(FORMAT))
            
            else: 

                if msg in DISCONNECT_MESSAGE:
                    connections.remove(conn)
                    for connection in connections:    
                        connection.send(f"[{server_usernames[addr]}] has left".encode(FORMAT))
                    server_usernames.pop(addr)
                    connected = False
                
                elif msg == COMMANDS[0]:
                    conn.send(f"Users that are online: [{client_usernames.keys()}]".encode(FORMAT))
                
                else:
                    print(f"[{addr}]: {msg}")
                    #conn.send(f"[{addr}]: {msg}".encode(FORMAT))
                    for connection in connections:
                        connection.send(f"[{server_usernames[addr]}]: {msg}".encode(FORMAT))
            
    
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
