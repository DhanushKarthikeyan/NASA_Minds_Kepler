from mecanum import mecanum 
import json

def mecanum_handler(js):
    if js['type'] == 'commands':
        angle, radius = zip(*js['payload'])
        for m in range(len(angle)):
            mecanum(radius[m], angle[m])

def driver(filename):
    # verify file
    # use subprocess library
    verified = None

    if verified:
        # open JSON file
        with open(f'{filename}') as json_file:
            data = json.load(json_file)
            mecanum_handler(data)

