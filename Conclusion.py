#Imports
import pygame, sys, time
import time
from pygame.locals import *
import random, time

#Other Variables for use in the program
SCREEN_WIDTH = 1550
SCREEN_HEIGHT = 800

class Conclusion:
    def __init__ (self, character1, character2):
        print("init end")
        #Initialzing
        pygame.init()

        #Setting up Fonts
        self.font = pygame.font.SysFont("Verdana", 30)

        #Display end pic
        self.display = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.image1 = pygame.image.load('./valentine_pics/endinghall.png').convert()
        self.image1 = pygame.transform.scale(self.image1,(SCREEN_WIDTH,SCREEN_HEIGHT))
        self.display.blit(self.image1,(0,0))

        if character1 == 'valentine_pics/bride1.png':
            self.character1 = pygame.image.load(character1).convert_alpha()
            self.character1  = pygame.transform.scale(self.character1, (600,800))
            self.display.blit(self.character1, (530,240))
        elif character1 == 'valentine_pics/bride2.png':
            self.character1 = pygame.image.load(character1).convert_alpha()
            self.character1  = pygame.transform.scale(self.character1, (500,700))
            self.display.blit(self.character1, (505,275))
        elif character1 == 'valentine_pics/groom1.png':
            self.character1 = pygame.image.load(character1).convert_alpha()
            self.character1  = pygame.transform.scale(self.character1, (600,800))
            self.display.blit(self.character1, (530,225))
        elif character1 == 'valentine_pics/groom2.png':
            self.character1 = pygame.image.load(character1).convert_alpha()
            self.character1  = pygame.transform.scale(self.character1, (500,700))
            self.display.blit(self.character1, (580,285))
            
        if character2 == 'valentine_pics/bride1.png':
            self.character2 = pygame.image.load(character2).convert_alpha()
            self.character2 = pygame.transform.flip(self.character2, True, False)
            self.character2  = pygame.transform.scale(self.character2, (600,800))
            self.display.blit(self.character2, (430,240))
        elif character2 == 'valentine_pics/bride2.png':
            self.character2 = pygame.image.load(character2).convert_alpha()
            self.character2 = pygame.transform.flip(self.character2, True, False)
            self.character2  = pygame.transform.scale(self.character2, (500,700))
            self.display.blit(self.character2, (555,275))
        elif character2 == 'valentine_pics/groom1.png':
            self.character2 = pygame.image.load(character2).convert_alpha()
            self.character2 = pygame.transform.flip(self.character2, True, False)
            self.character2  = pygame.transform.scale(self.character2, (600,800))
            self.display.blit(self.character2, (430,225))
        elif character2 == 'valentine_pics/groom2.png':
            self.character2 = pygame.image.load(character2).convert_alpha()
            self.character2 = pygame.transform.flip(self.character2, True, False)
            self.character2  = pygame.transform.scale(self.character2, (500,700))
            self.display.blit(self.character2, (490,285))

        self.image2 = pygame.image.load('./valentine_pics/endingbench.png').convert_alpha()
        self.image2 = pygame.transform.scale(self.image2,(SCREEN_WIDTH,SCREEN_HEIGHT))
        self.display.blit(self.image2,(0,0))

        pygame.draw.rect(self.display, (255,255,255), [100,650, 1400, 150])
        text = self.font.render('I saved the day and now the wedding can go on its way.', False, (0,0,0))
        self.display.blit(text, (125,675))



        pygame.display.flip()

        self.cont = False
        while not self.cont:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                click = pygame.mouse.get_pressed()
                if click[0] == 1:
                    self.cont = True

#Conclusion('valentine_pics/groom2.png','valentine_pics/groom2.png')

        
