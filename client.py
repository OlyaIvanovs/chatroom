import socket
import sys
import select


HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# if len(sys.argv) != 3:
#     print("Correct usage: script, IP address, port number")
#     exit()
# IP_address = str(sys.argv[1])
# Port = int(sys.argv[2])

server.connect((HOST, PORT))

while True:
    sockets_list = [sys.stdin, server]

    read_sockets, write_socket, error_socket = select.select(
        sockets_list, [], [])

    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048)
            print(message.decode())
        else:
            message = sys.stdin.readline()
            server.send(message.encode())
            sys.stdout.write("<You>")
            sys.stdout.write(message)
            sys.stdout.flush()

server.close()
