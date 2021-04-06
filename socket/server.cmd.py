import socket
import subprocess

address = ('127.0.0.1', 9999)
sk = socket.socket()
sk.bind(address)
sk.listen(3)

print('Waiting...')

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
        len_result = len(cmd_result)
        str_len_result = str(len_result)
        bytes_str_len_result = bytes(str_len_result, 'utf8')

        conn.sendall(bytes_str_len_result)
        conn.recv(1024)
        conn.sendall(cmd_result)

sk.close()
