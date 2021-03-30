import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host_name = "localhost"
host_ip = socket.gethostbyname(host_name)

# Get the list of command line arguments
args_list = sys.argv

server_host = args_list[1]
server_port = int(args_list[2])
filename = args_list[3]

conn_str = "Connecting to {} {} on port {}".format(
    host_name, host_ip, server_port)
print(conn_str)

sock.connect((server_host, server_port))

try:
    request = "GET /{} HTTP/1.1\r\nHost: {}:{}\r\n\r\n".format(
        filename, host_ip, server_port)
    sock.sendall(request.encode())

    response = ""
    while True:
        data = sock.recv(16).decode()
        if not data:
            break
        response += data
    print("-" * len(conn_str))
    print(response)

finally:
    print("closing socket")
    sock.close()
