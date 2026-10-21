import socket, threading

DISCONNECT_MESSAGE = ["/leave", "/quit", "/bye", "/part", "/exit"]
COMMANDS = ["/list"]
FORMAT = 'utf-8'
HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
SERVER = SERVER[:-3]
ADDR = (SERVER, PORT)
username = ("kusatchka")

def check_for_messages():
    while True:
        recv_message = client.recv(2048).decode(FORMAT)

        if len(recv_message) != 0:
            print(recv_message)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

if __name__ == "__main__":
    thread = threading.Thread(target=check_for_messages)
    username = input("Enter Your Username: ")
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
                thread.start()
                send(username)
            
            except ConnectionRefusedError:
                print("Not a valid Subnet\n")
                SERVERSUB_IDENT = input("Enter Subnet: ")
            
            except OSError:
                print("Not a valid Subnet\n")
                SERVERSUB_IDENT = input("Enter Subnet: ")

            else:
                break
    while True:
        message = input("")

        if message in DISCONNECT_MESSAGE:
            send(message)
            exit()
        

        else:
            send(message)
