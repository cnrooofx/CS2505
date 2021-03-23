import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4, TCP

port = 12002

sock.bind(("", port))
sock.listen(1)

while True:
    print("*** Waiting for Connection ***")

    connection, addr = sock.accept()
    print("Connection from", addr)
    try:
        request = connection.recv(1024).decode()
        filename = request.split()[1]

        with open(filename[1:], "r") as f:
            outputdata = f.read()

        connection.send("HTTP/1.1 200 OK\r\n\r\n".encode())

        for i in range(len(outputdata)):
            connection.send(outputdata[i].encode())
        connection.send("\r\n".encode())

        connection.close()
    except IOError:
        connection.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connection.send("""<html>\n    <head></head>\n    <body>
        <h1>404 Not Found</h1>\n    </body>\n</html>\r\n""".encode())

        connection.close()

sock.close()  
