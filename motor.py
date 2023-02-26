from machine import Pin
from utime import sleep,sleep_ms


in1=Pin(16,Pin.OUT)
in2=Pin(15,Pin.OUT)
in3=Pin(14,Pin.OUT)
in4=Pin(13,Pin.OUT)

delay=1

ROUND_VALUE=509

STEP_VALUE=[
 [1,0,0,0],
 [1,1,0,0],
 [0,1,0,0],
 [0,1,1,0],
 [0,0,1,0],
 [0,0,1,1],
 [0,0,0,1],
 [1,0,0,1]
]

def reset():
    in1(0)
    in2(0)
    in3(0)
    in4(0)
    

def step_run(count):
    direction=1
    if count<0:
        direction=-1
        count=-count
    for x in range(count):
        for bit in STEP_VALUE[::direction]:
            print(bit)
            in1.value(bit[0])
            in2(bit[1])
            in3(bit[2])
            in4(bit[3])
            
            sleep_ms(delay)
    reset()
    

def step_angle(a):
    step_run(int(ROUND_VALUE*a/360))
    
while True:
    step_run(509)
    step_run(-509)
    #step_angle(360)
    # step_angle(-360)
            