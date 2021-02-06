#Imports
import pygame, sys
import time
from pygame.locals import *
import random, time

#Other Variables for use in the program
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
currControl = ""
P1 = ""
P2 = ""



def startScreenBegin():

    #Initialzing
    pygame.init()

    #Setting up FPS
    FPS = 60
    FramePerSec = pygame.time.Clock()

    #Creating colors
    BLUE  = (0, 0, 255)
    RED   = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)



    #Setting up Fonts
    font = pygame.font.SysFont("Verdana", 60)
    font_small = pygame.font.SysFont("Verdana", 30)

    #Create a white screen
    DISPLAYSURF = pygame.display.set_mode((1000,600))
    DISPLAYSURF.fill(WHITE)
    pygame.display.set_caption("Valentine Wedding")

    #Game Loop
    while True:

        #Cycles through all events occuring
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        textSurf = font.render('Valentine Wedding', False, (0, 0, 0))
        DISPLAYSURF.blit(textSurf,((SCREEN_WIDTH/2)-275,(SCREEN_HEIGHT/2)-200))

        textSurf2 = font_small.render('Play Game', False, (0,0,0))


        pygame.draw.rect(DISPLAYSURF, (255,20,147),((SCREEN_WIDTH/2)-150,SCREEN_HEIGHT-(SCREEN_HEIGHT/4)-25, 300 , 50))

        DISPLAYSURF.blit(textSurf2,((SCREEN_WIDTH/2)-80, (SCREEN_HEIGHT-(SCREEN_HEIGHT/4))-20))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #print(click)
        if (((SCREEN_WIDTH/2)-150)+(300)) > mouse[0] > ((SCREEN_WIDTH/2)-150) and ((SCREEN_HEIGHT-(SCREEN_HEIGHT/4)-25)+50) > mouse[1] > (SCREEN_HEIGHT-(SCREEN_HEIGHT/4)-25):
            #pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
            if click[0] == 1:
                return True

        pygame.display.update()
        FramePerSec.tick(FPS)
