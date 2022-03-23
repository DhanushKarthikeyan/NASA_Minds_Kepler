#!/usr/bin/env python3

import socket
import time
import ftplib
 
IP = '127.0.0.1' # change to other side's ip address
TCP_PORT = 5005
BUFFER_SIZE = 1024
FILE_NAME = "test.json"
FTP_SUBDIR = 'incoming'

# assuming anonymous login with subdirectory FTP_SUBDIR under anonymous root
ftp = ftplib.FTP(IP)
ftp.login()
ftp.cwd(FTP_SUBDIR)
timestamped_filename = str(int(time.time()*1000)) + '_' + FILE_NAME
file = open(FILE_NAME,'rb')
ftp.storbinary('STOR ' + timestamped_filename, file)
file.close()
ftp.quit()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, TCP_PORT))
s.send(timestamped_filename.encode())
s.close()


