# Getting Started with Raspberry Pi Ch 4 Example 6

import pygame
from pygame.locals import *
import RPi.GPIO as GPIO
import time

def setup_leds():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23, GPIO.OUT)
    GPIO.setup(24, GPIO.OUT)
    GPIO.setup(25, GPIO.OUT)

def output_to_led(value,leds):

    #simple 3 LED case
    #Option: generalise this!

    bucket=value % (2**leds)

    binary_string=bin(bucket)[2:].zfill(3)

    led0=int(binary_string[2])
    led1=int(binary_string[1])
    led2=int(binary_string[0])
    print value, bucket, led2, led1, led0

    # Output our led bit values to real LEDS
    if led0: #This means if led value is not zero
        GPIO.output(23, GPIO.HIGH)
    if led1: #This means if led value is not zero
        GPIO.output(24, GPIO.HIGH)
    if led2: #This means if led value is not zero
        GPIO.output(25, GPIO.HIGH)

    #Hold the LEDs up for 0.7 seconds        
    time.sleep(0.2)
    #Now drop all the LEDs and hold for 0.5s and then we should loop back here after hold
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)
    GPIO.output(25, GPIO.LOW)
    time.sleep(0.1)

        
def fetch_and_display_mouse_input():
    width, height = 320, 320
    radius = 0
    mouseX, mouseY = 0, 0

    pygame.init()
    window = pygame.display.set_mode((width, height))
    window.fill(pygame.Color(255, 255, 255))

    fps = pygame.time.Clock()

    myloop=True
    myloopctr=0
    while myloop:
        for event in pygame.event.get():
            if event.type == MOUSEMOTION:
                mouseX, mouseY = event.pos
                output_to_led(mouseX+mouseY,3)
        pygame.display.update()
        fps.tick(30)
        myloopctr+=1
        if myloopctr > 100:
            myloop=False

#####MAIN ######

setup_leds()
fetch_and_display_mouse_input()
