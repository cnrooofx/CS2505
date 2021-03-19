import socket
from datetime import datetime

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4, TCP

port = 12002
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)

print("Server starting on {} {} on port {}".format(host_name, host_ip, port))

sock.bind((host_name, port))
sock.listen(1)

while True:
    print("*** Waiting for a connection ***")
    connection, client_address = sock.accept()
    try:
        print("connection from", client_address)
        time = "[{}] ".format(datetime.now().strftime("%c"))
        # %c is local datetime
        message = ""
        while True:
            data = connection.recv(16).decode()
            if not data:
                print("no more data from", client_address)
                break
            elif message == "":
                connection.sendall(time.encode())
            message += data
            print("received '{}'".format(data))
            print("sending data back to the client")
            connection.sendall(data.encode())

        # Append the current date and time with the message to the logfile
        with open("log.txt", "a") as log:
            log_message = "{}{}\n".format(time, message)
            log.write(log_message)

    finally:
        connection.close()

sock.close()
