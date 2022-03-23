
import os

#os.system('dir')
#os.system('echo adele')

import subprocess

#subprocess.call("dir", shell = True)

'''process = subprocess.run('dir', check=True, stdout=subprocess.PIPE, universal_newlines=True)
output = process.stdout'''

import subprocess

sshProcess = subprocess.Popen(['ssh', 
                               'pi@192.168.1.132'], #user_name@host
                               stdin=subprocess.PIPE, 
                               stdout = subprocess.PIPE,
                               universal_newlines=True,
                               bufsize=0)
sshProcess.stdin.write("ls .\n")
sshProcess.stdin.write("echo END\n")
sshProcess.stdin.write("uptime\n")
sshProcess.stdin.write("logout\n")
sshProcess.stdin.close()


for line in sshProcess.stdout:
    if line == "END\n":
        break
    print(line,end="")