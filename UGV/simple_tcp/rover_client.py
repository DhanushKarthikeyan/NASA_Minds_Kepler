#!/usr/bin/env python3

import socket
import time

TCP_IP = '192.168.0.102'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send('w'.encode())
data = s.recv(BUFFER_SIZE).decode()
print(f"received data: {data}")
time.sleep(1)
s.send('s'.encode())
data = s.recv(BUFFER_SIZE).decode()
print(f"received data: {data}")
time.sleep(1)
s.send('a'.encode())
data = s.recv(BUFFER_SIZE).decode()
print(f"received data: {data}")
time.sleep(1)
s.send('d'.encode())
data = s.recv(BUFFER_SIZE).decode()
print(f"received data: {data}")
time.sleep(1)
s.send('x'.encode())
data = s.recv(BUFFER_SIZE).decode()
print(f"received data: {data}")
s.close()


