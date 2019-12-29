import socket
import subprocess
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
        try:
            data = conn.recv(1024)
        except Exception:
            break
        if not data:
            break
        print('......', str(data, 'utf8'))

        obj = subprocess.Popen(str(data, 'utf8'), shell=True, stdout=subprocess.PIPE)
        cmd_result = obj.stdout.read()
        print(cmd_result)
        print(len(cmd_result))
        # result_len = bytes(str(len(cmd_result), 'utf8'))
        result_len = bytes(cmd_result)

        conn.send(result_len)
        conn.send(cmd_result)

sk.close()
