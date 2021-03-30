import socket
from datetime import datetime

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4, TCP

port = 12007
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)

print("Server starting on {} {} on port {}".format(host_name, host_ip, port))

sock.bind((host_name, port))
sock.listen(1)

while True:
    print("*** Waiting for a connection ***")
    connection, client_address = sock.accept()
    connection.settimeout(10)
    try:
        print("connection from", client_address)
        message = ""
        data = connection.recv(16, 0)
        while data:
            message += data.decode()
            data = connection.recv(16, 0)
        print("Received '{}'".format(message))

        print("Type reply to send or leave blank to quit.")
        reply = input("--> ")
        if reply == "":
            break
        connection.sendall(reply.encode())
        print("Replying: {}".format(reply))

    finally:
        connection.close()

sock.close()
