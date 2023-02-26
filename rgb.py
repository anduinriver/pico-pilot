from machine import Pin
import utime


red=Pin(1,Pin.OUT)
green=Pin(2,Pin.OUT)
blue=Pin(3,Pin.OUT)

def rgb_act(light,state):
    lgt=None
    if light=="red":
        lgt=red
    elif light=="green":
        lgt=green
    elif light=="blue":
        lgt=blue 
    
    if lgt is not None:
        if state==1:
            lgt.value(1)
        else:
            lgt.value(0)
            

def rgb_off():
    rgb_act("red",0)
    rgb_act("green",0)
    rgb_act("blue",0)
    
    
def rgb_on():
    rgb_act("red",1)
    rgb_act("green",1)
    rgb_act("blue",1)
    

while True:
    rgb_off()
    rgb_act("red",1)
    utime.sleep(1)
    
    rgb_off()
    rgb_act("green",1)
    utime.sleep(1)
    
    rgb_off()
    rgb_act("blue",1)
    utime.sleep(1)
