

import socket
import os

def Main():
    port = 4500
    host = '192.168.1.205'

    use_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    use_socket.bind((host, port))

    print("Server Started")
    try:
        while True:
            data, addr = use_socket.recvfrom(1024)
            data = data.decode('utf-8')
            #print("Message from: " + str(addr))
            #print("From connected user: " + data)
            if data == 'stop':
                print('stop')
                os.system('clementine -s')
            else:
                msg = '/usr/bin/clementine -l "/mounts/vault/Media/Kinda nice music/Amoc/Various/Amoc - Kolle aksu.mp3"'
                print(msg)
                os.system(msg)
    finally:
        use_socket.close()
        print('Socket closed.')

if __name__=='__main__':
    Main()
