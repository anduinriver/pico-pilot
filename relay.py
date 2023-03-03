from machine import Pin
import utime


relay=Pin(4,Pin.OUT)

def relay_on():
    relay(1)
    

def relay_off():
    relay(0)

while True:
    relay_on()
    utime.sleep(0.5)
    
    relay_off()
    utime.sleep(0.5)