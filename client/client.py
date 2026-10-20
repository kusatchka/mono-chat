import socket

DISCONNECT_MESSAGE = "!DISCONNECT"
FORMAT = 'utf-8'
HEADER = 64
PORT = 5050
SERVER = "192.168.1."
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

if __name__ == "__main__":
    SERVERSUB_IDENT = input("Enter Identifier: ")
    while True:
        if len(SERVERSUB_IDENT) > 3:
            SERVERSUB_IDENT = input("Enter Identifier: ")
        else:
            SERVER = SERVER + SERVERSUB_IDENT
            ADDR = (SERVER, PORT)
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(ADDR)
            break
        
