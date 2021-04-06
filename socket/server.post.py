import socket
import subprocess
import os

address = ('127.0.0.1', 9999)
sk = socket.socket()
sk.bind(address)
sk.listen(3)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print('BASE_DIR: ', BASE_DIR)
print('Waiting...')


while True:
    conn, addr = sk.accept()
    while True:
        file_info = conn.recv(2014)
        cmd, file_name, file_size_str = str(file_info, 'utf8').split('|')
        print('cmd:\t', cmd)
        print('file_name:\t', file_name)
        print('file_size:\t', file_size_str)
        full_path = os.path.join(BASE_DIR, 'send_and_receive', file_name)
        file_size_int = int(file_size_str)

        has_receive = 0
        with open(full_path, 'wb') as f:
            while has_receive != file_size_int:
                data = conn.recv(1024)
                f.write(data)
                has_receive += len(data)
            f.close()
            print('Post finished')

sk.close()
