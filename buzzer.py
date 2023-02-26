from machine import Pin
import utime


buzzer=Pin(15,Pin.OUT)

while True:
    # 500HZ
    for i in range(80):
        buzzer.value(1)
        utime.sleep(0.001)
        buzzer.value(0)
        utime.sleep(0.001)
        
    # 250HZ
    for i in range(100):
        buzzer.value(1)
        utime.sleep(0.002)
        buzzer.value(0)
        utime.sleep(0.002)
        
        