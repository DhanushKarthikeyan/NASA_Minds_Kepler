#!/usr/bin/env python3

import socket
import time
import ftplib
import sys

# relay - 103

def rovercomm_send(filename, destination_name, ftp_user = 'rovercomm', ftp_pass = 'rovercomm', tcp_port = 5005, ftp_subdir = 'incoming'):
    if destination_name == 'A':
        ip = '192.168.0.106'
    elif destination_name == 'B':
        ip = '192.168.0.102'
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

filename = sys.argv[1]
rovercomm_send(filename)