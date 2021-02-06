#Imports
import pygame, sys
import time
from pygame.locals import *
import random, time

#Other Variables for use in the program
SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 800
currControl = ""
P1 = ""
P2 = ""

class StartScreen:
    def __init__ (self):
        #Initialzing
        pygame.init()

        #Creating colors
        BLUE  = (0, 0, 255)
        RED   = (255, 0, 0)
        GREEN = (0, 255, 0)
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)

        #Setting up Fonts
        self.font = pygame.font.SysFont("Verdana", 60)
        self.font_small = pygame.font.SysFont("Verdana", 30)

        #Create a white screen
        self.display = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.image = pygame.image.load('./valentine_pics/title_screen.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,(SCREEN_WIDTH,SCREEN_HEIGHT))
        self.display.blit(self.image,(0,0))

        pygame.draw.rect(self.display, (255,20,147),((SCREEN_WIDTH/2)-150,SCREEN_HEIGHT-(SCREEN_HEIGHT/4)-25, 300 , 50))

        textSurf2 = self.font_small.render('Play Game', False, (0,0,0))
        self.display.blit(textSurf2,((SCREEN_WIDTH/2)-80, (SCREEN_HEIGHT-(SCREEN_HEIGHT/4))-20))
        pygame.display.update()
    

    def startScreenBegin(self):

        #Game Loop
        while True:

            #Cycles through all events occuring
            for event in pygame.event.get():

                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

    
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            #print(click)
            if (((SCREEN_WIDTH/2)-150)+(300)) > mouse[0] > ((SCREEN_WIDTH/2)-150) and ((SCREEN_HEIGHT-(SCREEN_HEIGHT/4)-25)+50) > mouse[1] > (SCREEN_HEIGHT-(SCREEN_HEIGHT/4)-25):
                #pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
                if click[0] == 1:
                    return True

