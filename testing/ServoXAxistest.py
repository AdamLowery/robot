import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)


pwm = GPIO.PWM(11, 50)

#while True:
pwm.start(7)
#	sleep(2)
#	pwm.ChangeDutyCycle(14)
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
                absevent = categorize(event)
                if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_Z":
			if absevent.event.value == 0:
                servo = "servo0"
                direction = "left"
                send = True
                print("Left")
             elif absevent.event.value == 255:
                servo = "servo0"
                direction = "right"
                send = True
                print("Right")
             elif absevent.event.value == 127:
                send = False



