#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

for i in range(50):
    GPIO.output(7,True)
    time.sleep(2)
    GPIO.output(7,False)
    time.sleep(2)

GPIO.cleanup()
