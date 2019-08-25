import RPi.GPIO as GPIO
import time
import sys
import time
import random
import pigpio


ain1=12
ain2=13
ena=6
bin1=20
bin2=21
enb=26

AIN1 = ain1
AIN2 = ain2
BIN1 = bin1
BIN2 = bin2
ENA = ena
ENB = enb
PA  = 25
PB  = 25
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(AIN1,GPIO.OUT)
GPIO.setup(AIN2,GPIO.OUT)
GPIO.setup(BIN1,GPIO.OUT)
GPIO.setup(BIN2,GPIO.OUT)
GPIO.setup(ENA,GPIO.OUT)
GPIO.setup(ENB,GPIO.OUT)
PWMA = GPIO.PWM(ENA,500)
PWMB = GPIO.PWM(ENB,500)
#PWMA.start(PA)
#PWMB.start(PB)
#stop()


pi = pigpio.pi()

from evdev import InputDevice, categorize, ecodes, KeyEvent, AbsEvent

gamepad = InputDevice('/dev/input/event0')

#prints out device info at start
print(gamepad)

#evdev takes care of polling the controller in a loop
for event in gamepad.read_loop():
        if event.type == ecodes.EV_ABS:
                adam = categorize(event)
                if ecodes.bytype[adam.event.type][adam.event.code] == "ABS_RZ":
                        xaxis = float(adam.event.value)
                        x = (xaxis - 60006)/60005*100
			xOutput = round(x, 2)*-1
			print xOutput
                        PA = xOutput
                        PB = xOutput
                        PWMA.start(PA)
                        PWMB.start(PB)
