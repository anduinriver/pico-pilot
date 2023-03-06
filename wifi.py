import network
import rp2
import time
import socket


rp2.country("CN")
wlan=network.WLAN(network.STA_IF)
wlan.active(True)
print(wlan.scan())


ssid="Schubert"
pw="xinxianshuo"
host="10.0.0.1"
port="55551"


def light_onboard_led(led_flag):
    led=machine.Pin("LED",machine.Pin.OUT)
    if led_flag==1:
        led.on()
    elif led_flag==0:
        led.off()

def connect():
    wlan.connect(ssid,pw)
    timeout=10
    while timeout>0:
        if wlan.status()>=3:
            light_onboard_led(1)
            print("conntected to WIFI SSID: Schubert")
            return 0
        timeout -=1
        print("waiting for connction to [Schubert]")
        time.sleep(1)
    light_onboard_led(0)    
    print("connection failed")

connect()

