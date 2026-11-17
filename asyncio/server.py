import socket, threading, sys

DISCONNECT_MESSAGE = ["/leave", "/quit", "/bye", "/part", "/exit"]
COMMANDS = ["/list", "/ban", "/kick", "/ip"]
FORMAT = 'utf-8'
HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

connections = []
server_usernames = {} #ip -> nickname
client_usernames = {} #nickname -> ip
usernames = list()

disconnect = threading.Event()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    client_thread = threading.Thread(target=handle_client, daemon=True, args=(conn, addr))
    print(f"[{addr}] has joined.")

    connected = True
    first_message = True
    disconnect.clear()
    while not disconnect.is_set():
        
        while connected:
            msg_length = conn.recv(HEADER).decode(FORMAT) #Checks the length of the message with HEADER
            
            if msg_length:    
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT)
                
                if first_message:
                    first_message = False
                    username = msg
                    
                    if username in usernames:
                        connection.send(f"The Username: {username} is already taken please choose something different")
                    
                    else:
                        usernames.append(username)
                        server_usernames.update({addr: username})
                        client_usernames.update({username: [addr, conn]})
                        
                        for connection in connections:
                                connection.send(f"{server_usernames[addr]} has joined\n".encode(FORMAT))
                    
                else: 

                    if msg in DISCONNECT_MESSAGE:
                        connections.remove(conn)
                        
                        for connection in connections:    
                            connection.send(f"[{server_usernames[addr]}] has left\n".encode(FORMAT))
                        
                        usernames.remove(username)
                        server_usernames.pop(addr)
                        client_usernames.pop(username)
                        disconnect.set()
                        
                        if threading.active_count() == 0:
                            print("[SERVER]: No Active Connections")
                        
                        else: 
                            print(f"[SERVER] ACTIVE CONNECTIONS: {threading.active_count() - 2}]")
                            disconnect.set()
                    
                    elif msg == COMMANDS[0]: #/list command for clients
                        conn.send(f"Users that are online: {usernames}".encode(FORMAT))
                    
                    else:
                        print(f"[{addr}]: {msg}")
                        #conn.send(f"[{addr}]: {msg}".encode(FORMAT))
                        for connection in connections:
                            connection.send(f"[{server_usernames[addr]}]: {msg}".encode(FORMAT))
            
    conn.close() #closes the connection between the client and the server
    disconnect.clear()
    print(f"[SERVER] ACTIVE CONNECTIONS: {threading.active_count() - 2}]")

def server_input():

    while True:
        message = input()
        
        if message in DISCONNECT_MESSAGE:
            server.close()
            exit()
        
        elif message == COMMANDS[0]:
            print(usernames)
        
        elif message == COMMANDS[2] + (" ") + message.replace("/kick ", ""):
            entered_username = message.replace("/kick ", "")

            if entered_username in client_usernames:
                print(client_usernames[entered_username])
                usernames.remove(entered_username)
                connections.remove(client_usernames[entered_username][1])
                disconnect.set()
                server_usernames.pop(client_usernames[entered_username][0])
                client_usernames.pop(entered_username)
                
            else:
                print("User not found, Try Again")


        elif message == COMMANDS[3] + (" ") + message.replace("/ip ", ""):
            entered_username = message.replace("/ip ", "")

            if entered_username in client_usernames:
                print(f"User Found: {entered_username}")
                print(f"IP: {client_usernames.get(entered_username)[0]}")
                connected_client_handli
            else:
                print("User Not Found, Try Again")


        else:
            print(f"[SERVER]: {message}")
            for connection in connections:
                        connection.send(f"[SERVER]: {message}".encode(FORMAT))

def start():

    server.listen()
    print(f"[SERVER] ONLINE AVAILABLE ON: {ADDR}")
    
    try:
        while True:
            conn, addr = server.accept()
            client_thread = threading.Thread(target=handle_client,daemon=True, args=(conn, addr))
            input_thread = threading.Thread(target=server_input, daemon=True)
            connections.append(conn)
            print(connections)
            input_thread.start()
            client_thread.start()
            print(f"[SERVER] ACTIVE CONNECTIONS: {threading.active_count() - 2}]")

    except KeyboardInterrupt:
        server.close()    
        

            

print("Starting Server...")
start()


async def main():
    pass

async def servers_input():
    
    while True:
        message = input()
        
        if message in DISCONNECT_MESSAGE:
            server.close()
            exit()
        
        elif message == COMMANDS[0]:
            print(usernames)
        
        elif message == COMMANDS[2] + (" ") + message.replace("/kick ", ""):
            entered_username = message.replace("/kick ", "")

            if entered_username in client_usernames:
                print(client_usernames[entered_username])
                usernames.remove(entered_username)
                connections.remove(client_usernames[entered_username][1])
                disconnect.set()
                server_usernames.pop(client_usernames[entered_username][0])
                client_usernames.pop(entered_username)
                
            else:
                print("User not found, Try Again")


        elif message == COMMANDS[3] + (" ") + message.replace("/ip ", ""):
            entered_username = message.replace("/ip ", "")

            if entered_username in client_usernames:
                print(f"User Found: {entered_username}")
                print(f"IP: {client_usernames.get(entered_username)[0]}")
                
            else:
                print("User Not Found, Try Again")


        else:
            print(f"[SERVER]: {message}")
            for connection in connections:
                        connection.send(f"[SERVER]: {message}".encode(FORMAT))

async def connected_client_handling(conn, addr):
    client_thread = threading.Thread(target=handle_client, daemon=True, args=(conn, addr))
    print(f"[{addr}] has joined.")

    connected = True
    first_message = True
    disconnect.clear()
    while not disconnect.is_set():
        
        while connected:
            msg_length = conn.recv(HEADER).decode(FORMAT) #Checks the length of the message with HEADER
            
            if msg_length:    
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT)
                
                if first_message:
                    first_message = False
                    username = msg
                    
                    if username in usernames:
                        connection.send(f"The Username: {username} is already taken please choose something different")
                    
                    else:
                        usernames.append(username)
                        server_usernames.update({addr: username})
                        client_usernames.update({username: [addr, conn]})
                        
                        for connection in connections:
                                connection.send(f"{server_usernames[addr]} has joined\n".encode(FORMAT))
                    
                else: 

                    if msg in DISCONNECT_MESSAGE:
                        connections.remove(conn)
                        
                        for connection in connections:    
                            connection.send(f"[{server_usernames[addr]}] has left\n".encode(FORMAT))
                        
                        usernames.remove(username)
                        server_usernames.pop(addr)
                        client_usernames.pop(username)
                        disconnect.set()
                        
                        if threading.active_count() == 0:
                            print("[SERVER]: No Active Connections")
                        
                        else: 
                            print(f"[SERVER] ACTIVE CONNECTIONS: {threading.active_count() - 2}]")
                            disconnect.set()
                    
                    elif msg == COMMANDS[0]: #/list command for clients
                        conn.send(f"Users that are online: {usernames}".encode(FORMAT))
                    
                    else:
                        print(f"[{addr}]: {msg}")
                        #conn.send(f"[{addr}]: {msg}".encode(FORMAT))
                        for connection in connections:
                            connection.send(f"[{server_usernames[addr]}]: {msg}".encode(FORMAT))
            
    conn.close() #closes the connection between the client and the server
    disconnect.clear()
    print(f"[SERVER] ACTIVE CONNECTIONS: {threading.active_count() - 2}]")

asyncio.start(main())