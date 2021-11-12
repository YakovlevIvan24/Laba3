import RPi.GPIO as GPIO
import time
import numpy as np
import matplotlib.pyplot as plt


dac = [26, 19, 13, 6, 5, 11, 9, 10]
led = [21, 20, 16, 12, 7, 8, 25, 24]
bits = len(dac)
levels = 2**bits
troyka = 17
comp = 4
napr =[]


GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(led, GPIO.OUT, initial = GPIO.LOW)


def dec2bin (value):
    return [int(bin) for bin in bin(value)[2:].zfill(bits)]

def bin2dac(value):
    signal = dec2bin(value)
    GPIO.output(dac, signal)
    return signal

def adc():
    value = 0
    for i in range(8):
        value = value + 2**(7 - i)
        signal = bin2dac(value)
        time.sleep(0.001)
        compValue = GPIO.input(comp)
        if compValue == 0:
            value = value - 2**(7 - i)
            voltage = value / levels * 3.3
    GPIO.output(led, signal)
    print (value, signal, voltage)
    napr.append(value)