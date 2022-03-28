#!/usr/bin/env python3
import socket
from time import sleep, time
import ftplib
import sys
import os 
import subprocess as sproc
from random import randint
from multiprocessing import Process
from Branch_UGV.rover import rover_main

LMS_BIN_PATH = '/usr/bin/lms'
LMS_KEY_PATH = '/home/pi/rover1'

ROUNDS = 100

def sign(filename, key_path = LMS_KEY_PATH):
    print('signing')
    lmsproc = sproc.run([LMS_BIN_PATH, 'sign', key_path, filename], capture_output=True)

def rovercomm_send(filename, destination_name, ftp_user = 'rovercomm', ftp_pass = 'rovercomm', tcp_port = 5005, ftp_subdir = 'incoming'):
    if destination_name == 'A':
        ip = '192.168.0.106'
    elif destination_name == 'B':
        ip = '192.168.0.102'
    elif destination_name == 'loop':
        ip = '127.0.0.1'
    ftp = ftplib.FTP(ip, ftp_user, ftp_pass)
    ftp.cwd(ftp_subdir)

    #timestamped_filename = str(int(time.time()*1000)) + '_' + FILE_NAME
    
    file = open(filename,'rb')
    ftp.storbinary('STOR ' + filename, file)
    file.close()
    file = open(filename+'.sig','rb')
    ftp.storbinary('STOR ' + filename+'.sig', file)
    file.close()
    ftp.quit()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, tcp_port))
    s.send(filename.encode())
    s.close()

def logtime(filename):
    with open('end_time.csv', 'a+') as timelog:
        timelog.write(f'{os.path.getsize(f"{os.getcwd()}/{filename}")}, ')
        timelog.write(f'{int(time()*1000)}\n')

def gentestfile():
    filename = f'benchmark_test_{int(time()*1000)}'
    with open(filename, 'wb+') as file:
        file.write(os.urandom(randint(0,10000000)))
    return filename

def runtest():
    testfname = gentestfile()
    logtime(testfname)
    sign(testfname)
    rovercomm_send(testfname, 'loop')
    

if __name__ ==  "__main__":
    p = Process(target=rover_main)
    p.start()
    for i in range(100):
        runtest()
        sleep(5)
    p.terminate()
    p.close()        
