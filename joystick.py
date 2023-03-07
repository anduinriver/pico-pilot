from machine import Pin,ADC
import utime


rocker_x=ADC(27)
rocker_y=ADC(26)
button=Pin(28,Pin.IN,Pin.PULL_UP)


def read_x():
    value=int(rocker_x.read_u16()*256/65536)
    return value


def read_y():
    value=int(rocker_y.read_u16()*256/65536)
    return value


def btn_state():
    press=False
    if button.value()==0:
        press=True
    return press

while True:
    value_x=read_x()
    value_y=read_y()
    state=btn_state()
    print("x:{},y:{},press:{}".format(value_x,value_y,state))
    utime.sleep(0.5)