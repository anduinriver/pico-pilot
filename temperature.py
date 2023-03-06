import machine
import utime
from machine import Pin,I2C
from ssd1306 import SSD1306_I2C


i2c=I2C(0,scl=Pin(21),sda=Pin(20),freq=100000)
oled=SSD1306_I2C(128,32,i2c)


def showText(t):
    oled.fill(0)
    oled.text("T="+str(t),0,12)
    oled.show()


sensor_temperature=machine.ADC(4)
conversion_factor=3.3/65535

while True:
    reading=sensor_temperature.read_u16()*conversion_factor
    temperature= round(27-(reading-0.706)/0.001721,2)
    print(temperature)
    showText(temperature)
    utime.sleep(2)
