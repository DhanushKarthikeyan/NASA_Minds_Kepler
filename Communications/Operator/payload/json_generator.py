
import json
    
def create_json(payload_name, polar_points):
    # dictionary of commands
    # make type dynamic for other subroutines
    commands = {
        "type" : "waypoints",
        "payload" : polar_points
        #"payload" : [(90, 5), (270, 5), (180, 5), (0, 5), (135, 2), (225, 2), (315, 2), (45, 2)]
    }

    with open(f"{payload_name}.json", "w") as outfile:
        json.dump(commands, outfile, indent=4, sort_keys=False)
