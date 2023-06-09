import os 

import pygame
from pygame.locals import *

from ui.ui import UImanager, Canvas, Label, Tab, Container, Button

pygame.init()

SCREEN_WIDTH = 795
SCREEN_HEIGHT = 721


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption('UI TEST')

screen1 = UImanager(screen, debug=True, threadedCollisionDetection=True)

# 1 : example of maipulating ui objects using the inbuilt object lookuptable
def positon(canvas2):
    for label in canvas2.attachedObjects['Label']:
        if label.parent:
            label.object.x = label.parent.object.topleft[0]
            label.object.y = label.parent.object.topleft[1] - label.object.h

img = pygame.image.load(f'{os.getcwd()}/testImage.png').convert_alpha()

canvas2 = Canvas(ui=screen1, isMoveable=True, objectPosition=(400,100), isVisible=True)
label4 = Label( '!', (255,0,0), parent=canvas2, identifier='!')
label5 = Label('World', (255,0,0), parent=label4, identifier='World')
label6 = Label('Hello', (255,0,0), parent=label5, identifier='Hello')
# ScrollBar(canvas2, bgColour=(255,250,250), objectSize=(5,10))
positon(canvas2)
####

# 2 : example of using objects to create a new object and ui manipulation [Drop down menu]
def update_canvas_scale(canvas):
    canvas.set_width(0)
    for width in [label.object.w for label in canvas.attachedObjects['Label']]:
        canvas.update_width(width)
    canvas.update_width(10)

    canvas.set_height(0)
    for height in [label.object.h for label in canvas.attachedObjects['Label']]:
        canvas.update_height(height)
    canvas.update_height(len(canvas.attachedObjects['Label'])*5)


c = Container(screen1)
canvas = Canvas(None, parent=c, objectSize=(55,45), objectPosition=(100,105), backgroundImage=img, isMoveable=False)
label1 = Label('I', (255,0,0), parent=canvas, isTextBackgroundVisible=False, objectPosition=(100, 180))
label2 = Label('DO', (255,0,0), parent=label1, objectPosition=(100, 165))
label3 = Label('OR', (255,0,0), parent=label2, isTextBackgroundVisible=False, objectPosition=(100, 150))
label4 = Label('NOTHING', (255,0,0), parent=label3,isTextBackgroundVisible=False, objectPosition=(100, 135))
label5 = Label('DO', (255,0,0), parent=label4, isTextBackgroundVisible=False, objectPosition=(100, 120))
label6 = Label('I', (255,0,0), parent=label5, isTextBackgroundVisible=False, objectPosition=(100, 105))
b = Button(event=None, eventArgs=[], child=canvas, text='Click Me', textColour=(255,0,0), parent=c, objectPosition=(100,90))
update_canvas_scale(canvas)
####


# 3 : project zomboid like inventory example [work in progress]
inventoryContainer = Container(screen1)
canvas = Canvas(ui=None, parent=inventoryContainer, objectSize=(100,45), objectPosition=(100,0), isMoveable=True, identifier='canvas1')
canvas2 = Canvas(ui=None, parent=canvas, objectSize=(100,100), objectPosition=(100,0), isMoveable=True, identifier='canvas2')
buttonOpen = Button(event=None, eventArgs=[], child=canvas2, text='Bobs Inventory', textColour=(255,0,0), parent=canvas, objectPosition=(100,0))
canvas.object.h = buttonOpen.object.h 


run = True
while run:
    screen.fill((0,0,0))

    pygame.display.set_caption(f'UI TEST FPS({round(clock.get_fps())}) Container Objects({screen1.numbContainers}) Parent Objects({screen1.numbParentObjs}) Child Objects({screen1.numbChildObjs})')

    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:  
            run = False
    
        if event.type == pygame.KEYDOWN:

            # DEBUG
            # switches between threaded and non threaded collison detectiono
            if pygame.key.get_pressed()[pygame.K_c]:
                screen1.threadedCollisionDetection = not(screen1.threadedCollisionDetection)
                print(screen1.threadedCollisionDetection )

    screen1.update_ui(events)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()