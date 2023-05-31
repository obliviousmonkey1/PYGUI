import os 

import pygame
from pygame.locals import *

from ui.ui import UImanager, Widget, Label, ScrollBar, Tab

pygame.init()

SCREEN_WIDTH = 795
SCREEN_HEIGHT = 721

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption('UI TEST')

screen1 = UImanager(screen, debug=False)

# 1
widget1 = Widget(screen1, (100,100), isVisible=True,)
label1 = Label( '!', (255,0,0), parent=widget1, identifier='!')
label2 = Label('World', (255,0,0), parent=label1, identifier='World')
Label('Hello', (255,0,0), parent=label2, identifier='Hello')
ScrollBar(widget1, bgColour=(255,250,250), objectSize=(5,10))
Widget(screen1, parent=widget1, objectSize=(10,10), objectPosition=(150,150), bgColour=(255,0,0))

# 2
widget2 = Widget(screen1, isMoveable=False, objectPosition=(400,100))
label4 = Label( '!', (255,0,0), parent=widget2, identifier='!')
label5 = Label('World', (255,0,0), parent=label4, identifier='World')
label6 = Label('Hello', (255,0,0), parent=label5, identifier='Hello')
ScrollBar(widget2, bgColour=(255,250,250), objectSize=(5,10))






run = True
while run:
    screen.fill((0,0,0))

    pygame.display.set_caption(f'UI TEST FPS({round(clock.get_fps())}) Parent Objects({screen1.numbParentObjs}) Child Objects({screen1.numbChildObjs})')

    screen1.threaded_cycle()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            run = False
    
        if event.type == pygame.KEYDOWN:
            pass
            
    pygame.display.flip()
    clock.tick(60)

pygame.quit()