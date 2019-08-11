#import evdev
from evdev import InputDevice, categorize, ecodes, KeyEvent

#importing Regular expressions
#import re
#creates object 'gamepad' to store the data
gamepad = InputDevice('/dev/input/event2')

#prints out device info at start
#print(gamepad)
#patternA = r".BTN_A.up."

#evdev takes care of polling the controller in a loop
for event in gamepad.read_loop():
	if event.type == ecodes.EV_KEY:
		keyevent = categorize(event)
		if keyevent.keystate == KeyEvent.key_down:
			if keyevent.keycode[0] == "BTN_A":
				print "Button A Pressed"
			elif keyevent.keycode[0] == "BTN_B":
				print "Button B Pressed"
			elif keyevent.keycode[0] == "BTN_WEST":
				print "Button Y Pressed"
			elif keyevent.keycode[0] == "BTN_NORTH":
				print "Button X Pressed"
		if keyevent.keystate == KeyEvent.key_up:
                        if keyevent.keycode[0] == "BTN_A":
                                print "Button A Released"
                        elif keyevent.keycode[0] == "BTN_B":
                                print "Button B Released"
                        elif keyevent.keycode[0] == "BTN_WEST":
                                print "Button Y Released"
                        elif keyevent.keycode[0] == "BTN_NORTH":
                                print "Button X Released"



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

