#!/usr/bin/env python3

# TCP (source: https://wiki.python.org/moin/TcpCommunication)

from ftplib import FTP
import socket
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
FTP_INCOMING_DIR = '/srv/ftp/incoming/'

if __name__ == '__main__':
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((TCP_IP, TCP_PORT))
        s.listen(1)

        conn, addr = s.accept() # blocking to accept
        print(f'Connection address: {addr}')
        
        while 1:
            data = conn.recv(BUFFER_SIZE).decode()
            if data:
                print(f"received file name: {data}")
                try:
                    with open(FTP_INCOMING_DIR+data,'r') as file:
                        print(file.read())
                        # driver
                        # verify file
                        # parse through json
                            # mecanum
                except OSError as e:
                    print(str(e))
                print(f"closing connection")
                conn.close()
                conn, addr = s.accept()
                print(f'Connection address: {addr}')
    except KeyboardInterrupt:
        print("Keyboard interrupt, exiting") 
    finally:
        conn.close()
