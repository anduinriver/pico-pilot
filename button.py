from machine import Pin
import utime


led=Pin(25, Pin.OUT)
key=Pin(0,Pin.IN,Pin.PULL_UP)

def led_on():
    led.value(1)
    

def led_off():
    led.value(0)
    

def press_state():
    return key.value()==0


while True:
    if press_state():
        print("press")
        led_on()
        utime.sleep(0.5)
    else:
        led_off()
