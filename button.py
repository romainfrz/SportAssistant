#can be used for button. mech keycap(only button part), touch sensor
from grovepi import *

def initButton(pin):
	pinMode(pin,"INPUT")
	return 1 

def readButton(pin):
	value = digitalRead(pin)
	return value
	
