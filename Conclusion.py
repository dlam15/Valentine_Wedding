#Imports
import pygame, sys, time
import time
from pygame.locals import *
import random, time

#Other Variables for use in the program
SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 800

class Conclusion:
    def __init__ (self):
        print("init end")
        #Initialzing
        pygame.init()

        #Setting up Fonts
        self.font = pygame.font.SysFont("Verdana", 30)

        #Display end pic
        self.display = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.image = pygame.image.load('./valentine_pics/wedding_hall.png').convert_alpha()#change/get from derrick
        self.image = pygame.transform.scale(self.image,(SCREEN_WIDTH,SCREEN_HEIGHT))
        self.display.blit(self.image,(0,0))

        pygame.draw.rect(self.display, (220,220,220),(0, SCREEN_HEIGHT-100, SCREEN_WIDTH, 100))
        text = self.font.render('I saved the day and now the wedding can go on its way.', False, (0,0,0))
        self.display.blit(text, (0,SCREEN_HEIGHT-100))

        pygame.display.update()

        #wait 7 sec then exit
        time.sleep(7)
        pygame.quit()
        sys.exit()
