from machine import Pin,I2C


i2c=I2C(0,scl=Pin(21),sda=Pin(20),freq=100000)

from ssd1306 import SSD1306_I2C
oled=SSD1306_I2C(128,32,i2c)

oled.text("Hello Raspberry Pi.",0,12)
oled.show()
