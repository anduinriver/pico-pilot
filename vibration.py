from machine import Pin
from utime import sleep,sleep_ms

shake=Pin(12,Pin.OUT)

def shake_on(on_time,delay_time):
    shake.value(1)
    sleep_ms(on_time)
    shake.value(0)
    sleep_ms(delay_time)
    

while True:
    shake_on(100,100)
    shake_on(100,100)
    shake_on(100,100)
    shake_on(500,500)                                                                           