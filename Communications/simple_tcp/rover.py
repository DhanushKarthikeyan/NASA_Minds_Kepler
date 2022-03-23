#!/usr/bin/env python
import RPi.GPIO as gpio
import time

# TCP (source: https://wiki.python.org/moin/TcpCommunication)
import socket
TCP_IP = ''
TCP_PORT = 5005
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

# gpio pin alias
back_left_forward = 6
back_left_backward = 13
back_right_forward = 0
back_right_backward = 5
front_left_forward = 7
front_left_backward = 1
front_right_forward = 25
front_right_backward = 8


def gpio_init():
    gpio.cleanup()
    gpio.setmode(gpio.BCM)
    for e in [0,5,6,13,1,7,8,25]:
        gpio.setup(e, gpio.OUT)

def forward():
    print('moving forward')
    gpio.output(front_right_forward, gpio.HIGH)
    gpio.output(front_left_forward, gpio.HIGH)
    gpio.output(back_left_forward, gpio.HIGH)
    gpio.output(back_right_forward, gpio.HIGH)
    time.sleep(0.1)
    gpio.output(front_right_forward, gpio.LOW)
    gpio.output(front_left_forward, gpio.LOW)
    gpio.output(back_left_forward, gpio.LOW)
    gpio.output(back_right_forward, gpio.LOW)


def backward():
    print('moving backward')
    gpio.output(front_right_backward, gpio.HIGH)
    gpio.output(front_left_backward, gpio.HIGH)
    gpio.output(back_left_backward, gpio.HIGH)
    gpio.output(back_right_backward, gpio.HIGH)
    time.sleep(0.1)
    gpio.output(front_right_backward, gpio.LOW)
    gpio.output(front_left_backward, gpio.LOW)
    gpio.output(back_left_backward, gpio.LOW)
    gpio.output(back_right_backward, gpio.LOW)

def right():
    print('moving sideway to the right')
    gpio.output(front_right_backward, gpio.HIGH)
    gpio.output(front_left_forward, gpio.HIGH)
    gpio.output(back_left_backward, gpio.HIGH)
    gpio.output(back_right_forward, gpio.HIGH)
    time.sleep(0.1)
    gpio.output(front_right_backward, gpio.LOW)
    gpio.output(front_left_forward, gpio.LOW)
    gpio.output(back_left_backward, gpio.LOW)
    gpio.output(back_right_forward, gpio.LOW)

def left():
    print('moving sideway to the left')
    gpio.output(front_right_forward, gpio.HIGH)
    gpio.output(front_left_backward, gpio.HIGH)
    gpio.output(back_left_forward, gpio.HIGH)
    gpio.output(back_right_backward, gpio.HIGH)
    time.sleep(0.1)
    gpio.output(front_right_forward, gpio.LOW)
    gpio.output(front_left_backward, gpio.LOW)
    gpio.output(back_left_forward, gpio.LOW)
    gpio.output(back_right_backward, gpio.LOW)

if __name__ == '__main__':
    try:
        gpio_init()

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((TCP_IP, TCP_PORT))
        s.listen(1)

        conn, addr = s.accept()
        print(f'Connection address: {addr}')
        
        while 1:
            data = conn.recv(BUFFER_SIZE).decode()
            if data:
                print(f"received data: {data}")
            if data == 'x':
                print(f"closing connection")
                conn.close()
                conn, addr = s.accept()
            elif data == 'w':
                forward()
            elif data == 'a':
                left()
            elif data == 's':
                backward()
            elif data == 'd':
                right()
            if not data == 'x':
                conn.send(data.encode())  # echo
    except KeyboardInterrupt:
        print("Keyboard interrupt, exiting") 
    finally:
        conn.close()
        gpio.cleanup()