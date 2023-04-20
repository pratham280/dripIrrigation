from machine import PWM, Pin
from time import sleep

li = PWM(Pin(4, Pin.OUT), 5000)

while True:
    for i in range(0,1024):
        li.duty(i)
        sleep(0.0001)
    for i in reversed(range(0,1024)):
        li.duty(i)
        sleep(0.0001)
