from machine import ADC
import utime


rp=ADC(28)

def get_value():
    int(rp.read_u16()*101/65536)
    

while True:
    print(rp)
    value=get_value()
    print(value)
    utime.sleep(1)