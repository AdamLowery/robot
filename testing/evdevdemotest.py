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
#        print adam.event
        print ecodes.bytype[adam.event.type][adam.event.code], adam.event.value






#        if adam.event == "code 02":
#            print "FSDFSDFSDFSDF"





#        if adam.keystate == KeyEvent.key_down:
#            if adam.keycode[0] == "BTN_A":
#                print "Button A Pressed"
