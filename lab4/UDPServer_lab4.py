import socket
from datetime import datetime

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

port = 6789
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print(host_name, host_ip)

print("Server Starting")

sock.bind(("", port))

while True:
    print("*** Waiting for message ***")
    message, client_address = sock.recvfrom(4096)
    print("message from", client_address)
    message = message.decode()
    print(message)

    timestamp = "[{}] ".format(datetime.now().strftime("%c"))
    response = timestamp + message.upper()
    sock.sendto(response.encode(), client_address)

    with open("log.txt", "a") as log:
        log.write(response + "\n")

sock.close()
