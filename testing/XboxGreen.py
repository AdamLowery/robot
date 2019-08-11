#import evdev
from evdev import InputDevice, categorize, ecodes

#importing Regular expressions
import re
#creates object 'gamepad' to store the data
gamepad = InputDevice('/dev/input/event2')

#prints out device info at start
print(gamepad)
patternA = r".BTN_A.up."

#evdev takes care of polling the controller in a loop
for event in gamepad.read_loop():
	output = str(categorize(event))
#	if "BTN_A" in output:
	if re.search("*BTN_A\s+?\S+?down", output):
		print ("Button A Pressed Down!")
	
#	else:
#		print ("NO BUTTON A")


#if re.match(patternA, output):  
#		print("Button A")
#else:
#	print ("not button A")
