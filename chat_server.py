import socket
import sys
from _thread import *

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# tells the kernel to reuse a local socket in TIME_WAIT state, without waiting for its natural timeout to expire.
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((HOST, PORT))

# listens for 100 active connections
server.listen(100)

list_of_clients = []


def clientthread(conn, addr):
    conn.send("Welcome to this chatroom!".encode())

    while True:
        try:
            message = conn.recv(2048)
            if message:
                message_to_send = "<" + addr[0] + "> " + message.decode()
                print(message_to_send)
                # broadcast(message_to_send, conn)
            else:
                """message may have no content if the connection 
                    is broken, in this case we remove the connection"""
                remove(conn)

        except:
            continue


def remove(conn):
    if conn in list_of_clients:
        list_of_clients.remove(conn)


def broadcast(message, conn):
    for client in list_of_clients:
        if client != conn:
            try:
                clients.send(message)
            except:
                client.close()

            # if the link is broken, we remove the client
            remove(clients)


while True:
    conn, addr = server.accept()
    list_of_clients.append(conn)

    # prints the address of the user that just connected
    print(addr[0] + "connected")

    start_new_thread(clientthread, (conn, addr))

conn.close()
server.close()
