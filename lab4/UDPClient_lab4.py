import socket
import sys

args_list = sys.argv
server_host = args_list[1]
server_ip = socket.gethostbyname(server_host)
print(server_host, server_ip)

port = 6789

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    message = input("Type message here: ")
    sock.sendto(message.encode(), (server_ip, port))

    data = sock.recvfrom(4096)
    response = data[0].decode()
    print(response)

finally:
    sock.close()
