#!/usr/bin/env python3

import RPi.GPIO as gpio
from time import sleep
from math import pi, cos, sin

MAX_THR = 240
MIN_THR = 165

# https://www.electronicwings.com/raspberry-pi/raspberry-pi-pwm-generation-using-python-and-c
PWM_FREQ = 3000
GPIO_MODE = gpio.BCM

'''
NEED TO CHANGE THE PIN NUMBER!!!
'''

# PWM gpio pin number
PWM0PIN = 12
PWM1PIN = 13

# front left wheel and back right wheel gpio pin number
FLBR_FWD_PIN = 0 # forward
FLBR_BWD_PIN = 0 # backward

# front right wheel and back left wheel gpio pin number
FRBL_FWD_PIN = 0
FRBL_BWD_PIN = 0

'''
NEED TO CHANGE THE PIN NUMBER!!!
'''

ALL_PINS = {FLBR_FWD_PIN, FLBR_BWD_PIN, FRBL_FWD_PIN, FRBL_BWD_PIN}
FWD_PINS = {FLBR_FWD_PIN, FRBL_FWD_PIN}
BWD_PINS = {FLBR_BWD_PIN, FRBL_BWD_PIN}
LEFT_PINS = {FLBR_BWD_PIN, FRBL_FWD_PIN}
RIGHT_PINS = {FLBR_FWD_PIN, FRBL_BWD_PIN}


INIT_FLAG = False

pwm0 = None
pwm1 = None


def radians(angle):
    return angle*pi/180

def gpio_init():
    global pwm0
    global pwm1
    global INIT_FLAG
    gpio.cleanup()
    gpio.setmode(GPIO_MODE)
    for e in ALL_PINS:
        gpio.setup(e, gpio.OUT)
    pwm0 = gpio.PWM(PWM0PIN, PWM_FREQ)
    pwm0.start(0)
    pwm1 = gpio.PWM(PWM1PIN, PWM_FREQ)
    pwm1.start(0)
    INIT_FLAG = True

def init_check():
    if ((not INIT_FLAG) or (pwm0 is None) or (pwm1 is None)):
        gpio_init()

def on(pins = ALL_PINS, off = False):
    init_check()
    try:
        for e in pins:
            gpio.output(e, gpio.LOW if off else gpio.HIGH)
    except TypeError:
        gpio.output(pins, gpio.LOW if off else gpio.HIGH)

def off(x = ALL_PINS):
    on(x, True)

def forward():
    off()
    on(FWD_PINS)

def backward():
    off()
    on(BWD_PINS)

def left():
    off()
    on(LEFT_PINS)

def right():
    off()
    on(RIGHT_PINS)

def mecanum(angle, duration):
    init_check()
    duty_cycle0 = abs((MAX_THR - MIN_THR)*cos(radians(angle) - 0.79)) + MIN_THR
    duty_cycle1 = abs((MAX_THR - MIN_THR)*sin(radians(angle) - 0.79)) + MIN_THR
    pwm0.ChangeDutyCycle(duty_cycle0)
    pwm1.ChangeDutyCycle(duty_cycle1)

    angle += 45
    angle %= 360
    q = angle*4/360
    if ( q < 1 ):
        right()
    elif ( q < 2 ):
        forward()
    elif ( q < 3 ):
        left()
    elif ( q < 4 ):
        backward()
    else:
        off()
    sleep(duration/1000)
    off()