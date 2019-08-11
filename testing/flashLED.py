import RPi.GPIO as GPIO					# Import Raspberry Pi GPIO library
from time import sleep					# Import the sleep function from time module

GPIO.setwarnings(False)					# Ignore warning for now
GPIO.setmode(GPIO.BOARD)				# Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)		# Set ppin 8 to be an output pin and set initial value to low(off)

while True:	# Run forever
	GPIO.output (8, GPIO.HIGH)	# Turn on
	sleep (1)			# sleep for one second
	GPIO.output (8, GPIO.LOW)	# turn off
	sleep (1) 
