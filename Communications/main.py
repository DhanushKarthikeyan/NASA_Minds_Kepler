
# initialize setup (code will be run on RPI 4B)

# python code to execute linux commands

# generate payload for UGV
'''
    - JSON with angle, distance
    - payload type
'''

# run cisco code
'''
    - genkey rover (do in advance and share with UGV)
    - sign rover file
'''

# connect SSH to UGV RPI W+
'''
    - send commands to RPI W
    - verify rover file
        - check if signature is verified
        - NOT = failed
            - communicate that payload was not received
        - True = execute
            - run commands
    - send more commands to UGV
    - close session
'''

# auxiliary functions
'''
    - more types
        - CV control
        - manual control
        - LIDAR
    - man in the middle attack?
        - communicate on that port
        - log commands not verified?
'''


