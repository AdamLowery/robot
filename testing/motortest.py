import sys
import time
import random
import pigpio

#import evdev and Time and RPIO
from evdev import InputDevice, categorize, ecodes, KeyEvent
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(15, GPIO.OUT, initial=GPIO.LOW)


NUM_GPIO=32

MIN_WIDTH=1000
MAX_WIDTH=2000

step = [0]*NUM_GPIO
width = [0]*NUM_GPIO
used = [False]*NUM_GPIO

pi = pigpio.pi()

from evdev import InputDevice, categorize, ecodes, KeyEvent, AbsEvent

gamepad = InputDevice('/dev/input/event2')

#prints out device info at start
print(gamepad)

#evdev takes care of polling the controller in a loop
for event in gamepad.read_loop():
        if event.type == ecodes.EV_ABS:
                adam = categorize(event)
                if ecodes.bytype[adam.event.type][adam.event.code] == "ABS_Z":
                        xaxis = float(adam.event.value)
                        x = (xaxis - 65536)/65535*100
			xOutput = round(x, 2)*-1
			print xOutput
			pi.set_servo_pulsewidth(6, xOutput)

                if ecodes.bytype[adam.event.type][adam.event.code] == "ABS_RZ":
                        yaxis = float(adam.event.value)
                        y = (yaxis - 65536)/65535*100
			yOutput = round(y, 2)*-1
			print yOutput
			pi.set_servo_pulsewidth(26, yOutput)

	if event.type == ecodes.EV_KEY:
        	keyevent = categorize(event)
        	if keyevent.keystate == KeyEvent.key_down:
        		if keyevent.keycode[0] == "BTN_A":
       	                	print "Button A Pressed"
	                        GPIO.output (15, GPIO.HIGH)
		if keyevent.keystate == KeyEvent.key_up:
                	if keyevent.keycode[0] == "BTN_A":
                                print "Button A Released"
                                GPIO.output (15, GPIO.LOW)


