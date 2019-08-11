import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)


pwm = GPIO.PWM(11, 50)

#while True:
pwm.start(5.5)
#	sleep(2)
#	pwm.ChangeDutyCycle(12)
#	sleep(2)
#	pwm.ChangeDutyCycle(1)





#import evdev
from evdev import InputDevice, categorize, ecodes, KeyEvent, AbsEvent

#creates object 'gamepad' to store the data
#you can call it whatever you like
gamepad = InputDevice('/dev/input/event2')

#prints out device info at start
print(gamepad)

#evdev takes care of polling the controller in a loop
for event in gamepad.read_loop():
        if event.type == ecodes.EV_ABS:
                adam = categorize(event)
                if ecodes.bytype[adam.event.type][adam.event.code] == "ABS_Z":
                        xaxis = adam.event.value
                        if xaxis < 32767.5:
                                pwm.ChangeDutyCycle(14)
                        if xaxis > 32767.5:
                                pwm.ChangeDutyCycle(1)
