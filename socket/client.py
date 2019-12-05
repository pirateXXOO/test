import socket

address = ('127.0.0.1', 9999)
sk = socket.socket()
sk.connect(address)

while True:
    inp = input(">>> ")
    sk.send(bytes(inp, 'utf8'))
    if inp == 'exit':
        break
    data = sk.recv(1024)
    str_data = str(data, 'utf8')
    print(str_data)
    if str_data == 'exit':
        break

sk.close()
