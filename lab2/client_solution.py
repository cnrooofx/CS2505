import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4, TCP

port = 12007
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
server_name = "cs1dev.ucc.ie"

print("Client starting on {} {}".format(host_name, host_ip))
print("-" * 20)
print("Connecting to {} on port {}".format(server_name, port))

sock.connect((server_name, port))

while True:
    print("Type message to send or leave blank to quit.")
    message = input("--> ")
    if message == "":
        break
    sock.sendall(message.encode())
    
    reply = ""
    data = sock.recv(16, 0)
    while data:
        reply += data.decode()
        data = sock.recv(16, 0)
            
    print("Reply: '{}'".format(reply))

print("closing socket")
sock.close()
