#import evdev and Time and RPIO
from evdev import InputDevice, categorize, ecodes, KeyEvent
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)


gamepad = InputDevice('/dev/input/event2')


#evdev takes care of polling the controller in a loop
for event in gamepad.read_loop():
	if event.type == ecodes.EV_KEY:
		keyevent = categorize(event)
		if keyevent.keystate == KeyEvent.key_down:
			if keyevent.keycode[0] == "BTN_A":
				print "Button A Pressed"
				GPIO.output (8, GPIO.HIGH)
			elif keyevent.keycode[0] == "BTN_B":
				print "Button B Pressed"
				GPIO.output (7, GPIO.HIGH)
			elif keyevent.keycode[0] == "BTN_WEST":
				print "Button Y Pressed"
				GPIO.output (11, GPIO.HIGH)
			elif keyevent.keycode[0] == "BTN_NORTH":
				print "Button X Pressed"
				GPIO.output (12, GPIO.HIGH)
		if keyevent.keystate == KeyEvent.key_up:
                        if keyevent.keycode[0] == "BTN_A":
                                print "Button A Released"
				GPIO.output (8, GPIO.LOW)
                        elif keyevent.keycode[0] == "BTN_B":
                                print "Button B Released"
				GPIO.output (7, GPIO.LOW)
                        elif keyevent.keycode[0] == "BTN_WEST":
                                print "Button Y Released"
				GPIO.output (11, GPIO.LOW)
                        elif keyevent.keycode[0] == "BTN_NORTH":
                                print "Button X Released"
				GPIO.output (12, GPIO.LOW)



#	output = str(categorize(event))



# ATTEMPT1
#	if "BTN_A" in output:
#	if re.search("*BTN_A\s+?\S+?down", output):
#		print ("Button A Pressed Down!")
	
#	else:
#		print ("NO BUTTON A")


#APPEMT 2

#if re.match(patternA, output):  
#		print("Button A")
#else:
#	print ("not button A")

