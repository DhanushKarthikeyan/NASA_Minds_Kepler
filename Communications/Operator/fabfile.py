
from fabric import task
from payload.gui import gui_driver
from payload.conversion import convert_mecanum_polar
from payload.json_generator import create_json
from automation.connection import UGV

def connect(ugv_name):
    X = UGV(ugv_name)
    X.connect()
    print('Connected!')
    return X

@task
def makePL(ctx, name):
    # call the GUI
    x, y = gui_driver()
    # call conversion
    ra = convert_mecanum_polar(x, y)
    # save as a json in local
    create_json(name, ra)
    print(f'{name}.json created in local directory')

@task 
def run(ctx, ugv, command): #generic run command
    X = connect(ugv)
    X.run(f'{command}')

@task
def sendPL(ctx, file, ugv): # transmit payload
    X = connect(ugv)
    if 'json' not in file:
        file = file + '.json'
    X.transfer(file, '/home/pi') #change directory here

@task
def send(ctx, file, ugv): # send any file
    X = connect(ugv)
    X.transfer(file, '/home/pi') #change directory here

@task
def check(ctx, ugv): # check directory at UGV
    X = connect(ugv)
    X.run('cd /home/pi && ls')

'''@task
def sendif(ctx, file, ugv):
    X = connect(ugv)
    if 'json' not in file:
        file = file + '.json'
    result = X.run('cd /home/pi/Documents/NASA_Minds && ls') # each run command changes state, so need to execute using boolean
    if file in result.stdout: #does not work
        print('found!!!')
        #X.transfer(file, '/home/pi/Documents/NASA_Minds')'''

@task
def sign(ctx, ugv, filename):
    X = connect(ugv)
    if 'json' not in filename:
        file = filename+'.json'
    print(f'signing {file}')

    X.run(f'cd /home/pi && lms sign rover1 {file}')
    print(f'\n\n{file} signed!\n') 

@task
def verify(ctx, ugv, filename):
    X = connect(ugv)
    file = filename+'.json'
    X.run(f'cd /home/pi && lms verify rover1 {file}') 

@task
def ftp(ctx, ugv, filename):
    X = connect(ugv)
    X.run(f'cd /home/pi && python3 root_client.py {filename}')

@task
def get(ctx):
    pass












