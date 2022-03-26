
from traceback import TracebackException
from tracemalloc import Traceback
import fabric

#ugv = fabric.Connection("192.168.1.132", port=22, user="pi", connect_kwargs={'password': 'raspberry'})
#result = ugv.run('uname -s')
#result = ugv.run('ls -l')
#result = ugv.run('pwd')
#print(result)

#class for connections?
class UGV():
    def __init__(self, name):
        self.name = name
        self.connection = None
        self.result = None

    def connect(self):
        if self.name == 'A':
            self.connection = fabric.Connection("192.168.0.106", port=22, user="pi", connect_kwargs={'password': 'raspberry'})
        elif self.name == 'B':
            self.connection = fabric.Connection("192.168.0.102", port=22, user="pi", connect_kwargs={'password': 'raspberry'})
        else:
            print('Name not recognized! ')
        return self.connection

    def run(self, command): #command is string
        try:
            self.connection.run(command)
        except Traceback:
            print('Please try again')
        finally:
            return 0
    
    def transfer(self, file, destination):
        self.result = self.connection.put(file, remote = destination)
        print("Uploaded {0.local} to {0.remote}".format(self.result))
        return self.result

'''X = UGV('A')
X.connect()
X.run('cd /home/pi/Documents/NASA_Minds')
X.run('ls')'''

