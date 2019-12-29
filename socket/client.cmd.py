import socket

address = ('127.0.0.1', 9999)
sk = socket.socket()
sk.connect(address)

while True:
    inp = input(">>> ")
    sk.send(bytes(inp, 'utf8'))
    # result_len = int(str(sk.recv(1024), 'utf8'))
    receive_len = sk.recv(1024)
    sk.sendall(bytes('1', 'utf8'))
    print('receive', receive_len)

    int_result_len = int(str(receive_len, 'utf8'))
    print(int_result_len)
    data = bytes()
    while len(data) != int_result_len:
        receive = sk.recv(1024)
        data += receive

    str_data = str(data, 'utf8')
    print(str_data)

sk.close()
