import RPi.GPIO as gpio
import time

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(17, gpio.OUT)
    gpio.setup(18, gpio.OUT)
   

def forward(tf):
    init()
    gpio.output(17, True)
    gpio.output(18, True)
    time.sleep(tf)
    gpio.cleanup()
    
def reverse(tf):
    init()
    gpio.output(17, False)
    gpio.output(18, False)
  
    time.sleep(tf)
    gpio.cleanup()

def turn_left(tf):
    init()
    gpio.output(17, False)
    gpio.output(18, True)
    time.sleep(tf)
    gpio.cleanup()

def turn_right(tf):
    init()
    gpio.output(17, True)
    gpio.output(18, False)
    time.sleep(tf)
    gpio.cleanup()
	
	
forward(1)
reverse(1)	
turn_left(1)
turn_right(1)
	