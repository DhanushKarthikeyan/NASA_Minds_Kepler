import subprocess as sproc
from mecanum import mecanum 
import json

LMS_BIN_PATH = '/usr/bin/lms'
LMS_KEY_PATH = '/home/pi/rover1'
FTP_INCM_PATH = '/srv/rovercomm/incoming/'

def mecanum_handler(js):
    print(js)
    if js['type'] == 'waypoints':
        angle, radius = zip(*js['payload'])
        for m in range(len(angle)):
            mecanum(radius[m], angle[m])

def driver(filename):
    if (verify(filename)):
        # open JSON file
        print('verified')
        with open(FTP_INCM_PATH+filename) as json_file:
            data = json.load(json_file)
            mecanum_handler(data)

def verify(filename, key_path = LMS_KEY_PATH):
    print('verifying')
    lmsproc = sproc.run([LMS_BIN_PATH, 'verify', key_path, FTP_INCM_PATH+filename], capture_output=True)
    #print(lmsproc.stdout)
    return lmsproc.stdout.decode().find('Signature verified') != -1