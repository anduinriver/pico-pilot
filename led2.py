from machine import Pin
import utime


led=Pin("LED",Pin.OUT)

while True:
    led.on()
    utime.sleep(0.5)
    led.off()
    utime.sleep(0.5)