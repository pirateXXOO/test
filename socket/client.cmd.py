import socket

address = ('127.0.0.1', 9999)
sk = socket.socket()
sk.connect(address)

while True:
    inp = input(">>> ")
    sk.send(bytes(inp, 'utf8'))
    # result_len = int(str(sk.recv(1024), 'utf8'))
    result_len = int(str(sk.recv(1024), 'gbk'))
    print(result_len)
    data = bytes()
    while len(data) != result_len:
        receive = sk.recv(1024)
        data += receive

    print(str(data, 'utf8'))

sk.close()
