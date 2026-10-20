import socket, threading

DISCONNECT_MESSAGE = ["/leave", "/quit", "/bye", "/part", "/exit"]
FORMAT = 'utf-8'
HEADER = 64
PORT = 5050
SERVER = "192.168.1."
ADDR = (SERVER, PORT)

def check_for_messages():
    while True:
        print(client.recv(2048).decode(FORMAT))

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

if __name__ == "__main__":
    SERVERSUB_IDENT = input("Enter Subnet: ")
    while True:
        if len(SERVERSUB_IDENT) > 3:
            SERVERSUB_IDENT = input("Enter Subnet: ")
        else:
            SERVER = SERVER + SERVERSUB_IDENT
            ADDR = (SERVER, PORT)
            try:
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.connect(ADDR)
            
            except ConnectionRefusedError:
                print("Not a valid Subnet\n")
                SERVERSUB_IDENT = input("Enter Subnet: ")
            
            except OSError:
                print("Not a valid Subnet\n")
                SERVERSUB_IDENT = input("Enter Subnet: ")

            else:
                break
    while True:
        thread = threading.Thread(target=check_for_messages)
        thread.start()
        message = input(">")

        if message in DISCONNECT_MESSAGE:
            send(message)
            exit()
        
        else:
            send(message)
            print(client.recv(2048).decode(FORMAT))
