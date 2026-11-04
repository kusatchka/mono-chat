import socket, threading, sys
from textual.app import App, ComposeResult
from textual.widgets import Footer, Header 

DISCONNECT_MESSAGE = ["/leave", "/quit", "/bye", "/part", "/exit"]
COMMANDS = ["/list"]
FORMAT = 'utf-8'
HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
SERVER = SERVER[:-3]
ADDR = (SERVER, PORT)
base = SERVER

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
    input_thread = threading.Thread(target=check_for_messages, daemon=True)
    def handle_subnet_input():
        SERVERSUB_IDENT = input("Enter Subnet: ")
        while True:
            if len(SERVERSUB_IDENT) > 3:
                SERVERSUB_IDENT = input("Enter Subnet: ")
                handle_subnet_input()
                break
            else:
                global SERVER 
                SERVER = base + SERVERSUB_IDENT
                global ADDR
                ADDR = (SERVER, PORT)
                try:
                    global client
                    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    client.connect(ADDR)
                    input_thread.start()
                    username = input("Enter Your Username: ").strip()
                    send(username)
                
                except ConnectionRefusedError:
                    print("Not a valid Subnet\n")
                    print("Try Again")
                    handle_subnet_input()
                    break
                
                except OSError:
                    print("Not a valid Subnet\n")
                    print("Try Again")
                    handle_subnet_input()
                    break
                
                else:
                    break
    
    handle_subnet_input()
    while True:
        message = input("")

        if message in DISCONNECT_MESSAGE:
            send(message)
            print(f"Disconnected from {ADDR}")
            sys.exit()
            break
        

        else:
            send(message)