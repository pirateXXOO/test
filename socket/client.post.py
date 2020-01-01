import socket
import os

address = ('127.0.0.1', 9999)
sk = socket.socket()
sk.connect(address)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

while True:
    inp = input(">>> ").strip()
    cmd, path = inp.split('|')
    full_path = os.path.join(BASE_DIR, path)
    filename = os.path.basename(full_path)
    file_size = os.stat(full_path).st_size
    file_info = 'post|%s|%s' % (filename, file_size)

    sk.sendall(bytes(file_info, 'utf8'))

    has_send = 0
    with open(full_path, 'rb') as f:
        while has_send != file_size:
            data = f.read(1024)
            sk.sendall(data)
            has_send += len(data)
        f.close()
        print('Post finished')


sk.close()
