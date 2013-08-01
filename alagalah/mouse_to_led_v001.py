# Getting Started with Raspberry Pi Ch 4 Example 6

import pygame
from pygame.locals import *

def output_to_led(value,leds):

    #simple 3 LED case
    #Option: generalise this!

    bucket=value % (2**leds)

    binary_string=bin(bucket)[2:].zfill(3)

    led0=binary_string[2]
    led1=binary_string[1]
    led2=binary_string[0]
    print value, bucket, led2, led1, led0
    
        
def fetch_mouse_input():
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

fetch_mouse_input()
