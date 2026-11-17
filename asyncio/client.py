import socket, threading, sys, asyncio
from enum import Enum

DISCONNECT_MESSAGE = ["/leave", "/quit", "/bye", "/part", "/exit"]
COMMANDS = ["/list"]
FORMAT = 'utf-8'
HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
SERVER = SERVER[:-3]
ADDR = (SERVER, PORT)
base = SERVER

async def check_for_messages():
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
                    username = input("Enter Your Username: ").strip()
                    send(username)
                    global print_all_incoming_messages 
                    print_all_incoming_messages = asyncio.create_task(check_for_messages())
                
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

async def main(): #change to async :steam_happy:
    
    handle_subnet_input()

    while True:
        message = input("")

        if message in DISCONNECT_MESSAGE:
            send(message)
            print(f"Disconnected from {ADDR}")
            print_all_incoming_messages.cancel()
            sys.exit()
            break
        

        else:
            send(message)
         

asyncio.run(main())