from machine import Pin,I2C
import time
import utime


i2c=I2C(0,scl=Pin(21),sda=Pin(20),freq=100000)

from ssd1306 import SSD1306_I2C
oled=SSD1306_I2C(128,32,i2c)


while True:
    now=time.localtime()
    print(now)
    t="%d/%d %d:%d:%d" % (now[1],now[2],now[3],now[4],now[5])
    oled.fill(0)
    oled.text(t,0,12)
    oled.show()
    utime.sleep(0.2)


