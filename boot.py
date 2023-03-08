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


def water():
    heart(wifi_suc, 0.001, 5)
    time.sleep(1)
    wifi_suc.duty(100)
    relay.on()


def connection(a, b):
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(a, b)
    while station.isconnected() == False:
        heart(wifi_con, 0.001, 5)
        pass
    if station.isconnected() == True:
        heart(wifi_suc, 0.0015, 2)
        heart(wifi_suc, 0.001, 5)
        wifi_suc.duty(100)
    print('\n')
    print("Your IP ADDRESS IS THIS:", station.ifconfig()[0])


# def water_lev():
#     val = sensor(trigger_pin=ultra_trig, echo_pin=ultra_echo)
#     return int(val.distance_cm())

#--------------------------------------------------- button
button_on = Pin(12, Pin.IN)  #d6 button on
stop = Pin(13, Pin.IN)  #d7 13 button stop
#-------------------------------------------------------- led
wifi_con = PWM(Pin(14, Pin.OUT), 5000)  #red led d5
wifi_suc = PWM(Pin(4, Pin.OUT), 5000)  #green led d2
wifi_suc.duty(0)
wifi_con.duty(0)
soil = ADC(0)
relay = Pin(5, Pin.OUT)  #d1
relay.off()
buzzer = PWM(Pin(3, Pin.OUT), )
# ultra_trig = Pin(16, Pin.OUT)
# ultra_echo = Pin(0, Pin.IN)
# wifi_dis = PWM(Pin(0, Pin.OUT), 5000)  #orange led d3
# wifi_dis.duty(0)
#---------------------------------------------------------- connect to internet
ssid = 'ANTI-VIRUS'
password = 'rakshasi@2028'
# ssid = "pratham"
# password = 'hello123456'
connection(ssid, password)

# ---------------------------- -------------------set time
settime()
offset = 19800
# -----------------------------------------------
