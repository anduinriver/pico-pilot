from machine import Pin
import utime


led=Pin(25,Pin.OUT)
sound=Pin(28,Pin.IN)


def led_on():
    led.value(1)


def led_off():
    led.value(0)
    

def sound_state():
    return sound.value()==0


while True:
    if sound_state():
        print("get sound")
        led_on()
        utime.sleep(0.1)
    else:
        led_off()
