import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4, TCP

port = 12002
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)

print("Connecting to {} {} on port {}".format(host_name, host_ip, port))

server_address = (host_name, port)
# server_address = ('localhost', port)

sock.connect(server_address)

try:
    message = input("Type message to send: ")
    print('sending "%s"' % message)
    sock.sendall(message.encode())

    amount_received = 0
    amount_expected = len(message)

    while True:
        data = sock.recv(16).decode()
        if data != "":
            print('received "%s"' % data)
        else:
            print('no more data')
            break

finally:
    print('closing socket')
    sock.close()
