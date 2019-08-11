import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
#GPIO.setup(13, GPIO.OUT)


pwm = GPIO.PWM(12, 50)
# pwm = GPIO.PWM(13, 50)
pwm.start(5.5)
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
                        x = (xaxis)/65535*1000+1000
			xOutput = round(x, 2)
			print xaxis
			print xOutput
#                        pwm.ChangeDutyCycle(xOutput)

#                if ecodes.bytype[adam.event.type][adam.event.code] == "ABS_RZ":
#                        yaxis = float(adam.event.value)
#                        y = xaxis/65535*14
#			yOutput = round(x, 2)
#			print y
#                        pwm.ChangeDutyCycle(yOutput)

#                        if xaxis > 32767.5:
#                                pwm.ChangeDutyCycle(1)
