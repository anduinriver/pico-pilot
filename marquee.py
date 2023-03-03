import ws2812b
import random
import utime


ring_pin=17
numpix=8


strip=ws2812b.ws2812b(numpix,0,ring_pin)
strip.fill(0,0,0)
strip.show()

while True:
    for i in range(numpix):
        strip.fill(0,0,0,)
        r=random.randint(0,256)
        g=random.randint(0,256)
        b=random.randint(0,256)
        
        j=(i+2)%8
        k=(i+4)%8
        l=(i+6)%8
        
        strip.set_pixel(i,r,g,b)
        strip.set_pixel(j,r,g,b)
        strip.set_pixel(k,r,g,b)
        strip.set_pixel(l,r,g,b)
        
        strip.show()
        utime.sleep(0.4)
        