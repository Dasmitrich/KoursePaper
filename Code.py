from machine import *
import time

h_sens = ADC(Pin(26, Pin.IN, Pin.PULL_UP))
pump_pow = Pin(28, Pin.OUT, Pin.PULL_DOWN)
led_R = Pin(19, Pin.OUT, Pin.PULL_DOWN)
led_G = Pin(20, Pin.OUT, Pin.PULL_DOWN)

while True:
    humidity = h_sens.read_u16()/54000
    print(humidity)
    if humidity > 0.9:
        pump_pow.on()
        led_G.off()
        led_R.on()
        time.sleep(0.75)
    else:
        pump_pow.off()
        led_R.off()
        led_G.on()
        time.sleep(1000)
