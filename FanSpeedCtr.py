#!/usr/bin/env python
import time
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("errror1")

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
fan = GPIO.PWM(12,100)
fan.start(0)
time.sleep(5)
while True:
    tmpFile = open( '/sys/class/thermal/thermal_zone0/temp' )
    cpu_temp_raw = tmpFile.read()
    tmpFile.close()
    cpu_temp = round(float(cpu_temp_raw)/1000, 1)
    #print (cpu_temp)
    if cpu_temp<=36 :
        fan.ChangeDutyCycle(100)
    if 37<=cpu_temp <=39  :
        fan.ChangeDutyCycle(80)
    if 40<=cpu_temp <=42  :
        fan.ChangeDutyCycle(60)
    if 43<=cpu_temp <=45  :
        fan.ChangeDutyCycle(30)
    if 46<=cpu_temp  :
        fan.ChangeDutyCycle(0)     
    time.sleep(10)


