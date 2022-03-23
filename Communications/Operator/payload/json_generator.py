
import json
    
# Data to be written
commands ={
    "type" : "waypoints",
    "payload" : [(90, 5), (270, 5), (180, 5), (0, 5), (135, 2), (225, 2), (315, 2), (45, 2)]
}

with open("ex1.json", "w") as outfile:
    json.dump(commands, outfile, indent=4, sort_keys=False)