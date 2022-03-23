
import fabric

ugv = fabric.Connection("192.168.3.151", port=22, user="pi", connect_kwargs={'password': 'raspberry'})
result = ugv.run('uname -s')