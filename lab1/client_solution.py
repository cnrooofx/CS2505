import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4, TCP

port = 12002

host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)

print("Connecting to {} {} on port {}".format(host_name, host_ip, port))

sock.connect((host_name, port))

try:
    message = input("Type message to send: ")
    print("sending '%s'" % message)
    sock.sendall(message.encode())

    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16).decode()
        amount_received += len(data)
        print("received '%s'" % data)

finally:
    print("closing socket")
    sock.close()
