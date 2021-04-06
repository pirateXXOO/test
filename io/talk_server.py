import select
import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 8800))
sk.listen(3)
inp = [sk, ]

while True:

    inputs, outputs, errors = select.select(inp, [], [], )

    for obj in inputs:
        if obj == sk:
            conn, addr = obj.accept()
            print(conn)
            inp.append(conn)
        else:
            data = obj.recv(1024)
            print(data.decode('utf8'))
            Inputs = input('Answer %s >>>'%inp.index(obj))
            obj.sendall(Inputs.encode('utf8'))
