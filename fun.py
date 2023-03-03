from machine import Pin,PWM


fan=PWM(Pin(13))
fan.freq(1000)

def my_map(x,in_min,in_max,out_min,out_max):
    return int((x-in_min)*(out_max-out_min)/(in_max-in_min)+out_min)

def pwm_motor(speed):
    if speed>100 or speed<0:
        print("Please enter a limited speed value of 0~100")
        return
    pulse=my_map(speed,0,100,0,65535)
    fan.duty_u16(pulse)
    
    
pwm_motor(100)