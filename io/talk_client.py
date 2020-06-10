import socket

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.connect(('127.0.0.1', 8800))

while True:
    inp = input('>>>')
    sk.sendall(bytes(inp, "utf8"))
    data = sk.recv(1024)
    print(data.decode('utf8'))
