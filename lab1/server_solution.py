import socket
from datetime import datetime

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4, TCP

port = 12002
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)

print("Server starting on {} {} on port {}".format(host_name, host_ip, port))

server_address = (host_name, port)

sock.bind(server_address)

sock.listen(1)

while True:
    print("*** Waiting for a connection ***")
    connection, client_address = sock.accept()
    try:
        print("connection from", client_address)
        message = ""
        while True:
            data = connection.recv(16).decode()
            if data:
                message += data
                print("received '%s'" % data)
                print("sending data back to the client")
                connection.sendall(data.encode())
            else:
                print("no more data from", client_address)
                break
        with open("log.txt", "a") as log:
            time = datetime.now().strftime("%c")
            log_message = "[{}] {}\n".format(time, message)
            log.write(log_message)

    finally:
        connection.close()

sock.close()
