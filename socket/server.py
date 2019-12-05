import socket

address = ('127.0.0.1', 9999)
sk = socket.socket()
sk.bind(address)
sk.listen(3)

print('Waiting...')

####### solution 1 ################
# conn, addr = sk.accept()
# while True:
#     data = conn.recv(1024)
#     str_data = str(data, 'utf8')
#     print(str_data)
#     if str_data == 'exit':
#         conn.close()
#         conn, addr = sk.accept()
#         continue
#     inp = input(">>> ")
#     conn.send(bytes(inp, 'utf8'))
#     if inp == 'exit':
#         conn.close()
#         conn, addr = sk.accept()
#         continue

####### solution 2 ################
while True:
    conn, addr = sk.accept()
    while True:
        data = conn.recv(1024)
        str_data = str(data, 'utf8')
        print(str_data)
        if str_data == 'exit':
            break
        inp = input(">>> ")
        conn.send(bytes(inp, 'utf8'))
        if inp == 'exit':
            break

sk.close()
