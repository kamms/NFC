import socket
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep

def Main():

    client_ip = '192.168.1.204'
    client_port = 4000
    use_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    use_socket.bind((client_ip,client_port))

    server_ip = '192.168.1.205'
    server_port = 4500
    server = (server_ip, server_port)
    reader = SimpleMFRC522()

    try:
        previous_id = None
        while True:
            id = reader.read_no_block()[0]
            if id is None:
               id = reader.read_no_block()[0]
            if id != None:
                if id != previous_id:
                    print('sending')
                    use_socket.sendto(str(id).encode('utf-8'), server)
            else:
                if previous_id != None:
                    print('sent stop')
                    use_socket.sendto('stop'.encode('utf-8'), server)
            previous_id = id
    finally:
        print('Socket closed')
        use_socket.close()
        GPIO.cleanup()

if __name__=='__main__':
    Main()
