try:
    import usocket as socket
except:
    import socket
import time, esp, gc, network
from machine import PWM, Pin, ADC
from ntptime import settime

esp.osdebug(None)
gc.collect()


#-------------------------------------------function
def heart(led, a, itt=1):
    for i in range(0, itt):
        for i in range(0, 1024):
            led.duty(i)
            time.sleep(a)
        for i in reversed(range(0, 1024)):
            led.duty(i)
            time.sleep(a)


def revert():
    relay.off()
    wifi_suc.duty(0)
    heart(wifi_con, 0.001, 2)
    wifi_con.duty(0)
    time.sleep(1)
    wifi_suc.duty(100)
    # buzzer in future


def water(a: int):
    i = 0
    relay.on()
    heart(wifi_suc, 0.001, 10)
    wifi_suc.duty(100)
    while i <= a:
        if stop.value() == 1:
            revert()
            break
        else:
            i += 1
            continue


#--------------------------------------------------- button
button_on = Pin(12, Pin.IN)  #d6 button on
stop = Pin(13, Pin.IN)  #d7 13 button stop
#-------------------------------------------------------- led
wifi_con = PWM(Pin(14, Pin.OUT), 5000)  #red led d5
wifi_con.duty(0)
wifi_suc = PWM(Pin(2, Pin.OUT), 5000)  #green led d4
wifi_suc.duty(0)
soil = ADC(0)
relay = Pin(15, Pin.OUT)  #d8
relay.off()
# wifi_dis = PWM(Pin(0, Pin.OUT), 5000)  #orange led d3
# wifi_dis.duty(0)
#---------------------------------------------------------- connect to internet
ssid = 'ANTI-VIRUS'
password = 'rakshasi@2028'

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
    heart(wifi_con, 0.001, 5)
    pass

if station.isconnected() == True and station.ifconfig()[0] == '192.168.1.11':
    heart(wifi_suc, 0.0015, 2)
    heart(wifi_suc, 0.001, 5)
    wifi_suc.duty(100)
else:
    heart(wifi_con, 0.0015, 10)
    wifi_con.duty(1024)
    pass
print('\n')
print("Your IP ADDRESS IS THIS:", station.ifconfig()[0])
# ---------------------------- -------------------set time
settime()
offset = 19800
# -----------------------------------------------
