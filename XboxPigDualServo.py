import sys
import time
import random
import pigpio

NUM_GPIO=32

MIN_WIDTH=1000
MAX_WIDTH=2000

step = [0]*NUM_GPIO
width = [0]*NUM_GPIO
used = [False]*NUM_GPIO

pi = pigpio.pi()

from evdev import InputDevice, categorize, ecodes, KeyEvent, AbsEvent

gamepad = InputDevice('/dev/input/event0')

#prints out device info at start
print(gamepad)

#evdev takes care of polling the controller in a loop
for event in gamepad.read_loop():
        if event.type == ecodes.EV_ABS:
                adam = categorize(event)
                if ecodes.bytype[adam.event.type][adam.event.code] == "ABS_Z":
                        xaxis = float(adam.event.value)
                        x = (xaxis - 60006)/60005*2000 - 500
			xOutput = round(x, 2)*-1
#			print xOutput
			pi.set_servo_pulsewidth(27, xOutput)

                if ecodes.bytype[adam.event.type][adam.event.code] == "ABS_RZ":
                        yaxis = float(adam.event.value)
                        y = (yaxis - 60006)/60005*2000 - 500
			yOutput = round(y, 2)*-1
			print yOutput
			pi.set_servo_pulsewidth(17, yOutput)
#                        pwm.ChangeDutyCycle(yOutput)

#                        if xaxis > 32767.5:
#                                pwm.ChangeDutyCycle(1)
