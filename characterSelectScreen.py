#Imports
import pygame, sys
import time
from pygame.locals import *
import random, time

#Other Variables for use in the program
SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 800
DISPLAYSURF = ""
selectedCharacters = []
move_ticker = 0

class CharacterSelect(pygame.sprite.Sprite):
    def __init__(self, multiplier, x, y, image):
        super().__init__()
        self.img = pygame.image.load(image)
        self.backgroundimg = pygame.image.load("valentine_pics/icon_regular.png")
        self.selectedimg = pygame.image.load("valentine_pics/icon_highlight.png")
        self.image = pygame.transform.scale(self.img,(3*multiplier,4*multiplier))#3:4 ratio works decent
        self.background = pygame.transform.scale(self.backgroundimg,(3*multiplier,4*multiplier))
        self.backgroundselected = pygame.transform.scale(self.selectedimg,(3*multiplier,4*multiplier))
        self.frameOne = (x+15, y+15, 200, 325)
        self.frameTwo = (x+20,y+20, 190, 315)
        self.x = x
        self.y = y
        self.selected = False
        self.highlighted = False
        self.prev = "00";

    def draw(self):
        if self.selected == False and self.highlighted == False:
            #regular background
            DISPLAYSURF.blit(self.background,(self.x,self.y))
            DISPLAYSURF.blit(self.image,(self.x,self.y))
            if self.prev != "00":
                redraw()
                self.prev = "00"
        if self.selected == False and self.highlighted == True:
            #highlighted background
            DISPLAYSURF.blit(self.backgroundselected,(self.x,self.y))
            DISPLAYSURF.blit(self.image,(self.x,self.y))
            if self.prev != "01":
                redraw()
                self.prev = "01"
        if self.selected == True and self.highlighted == True:
            #highlighted background, even on move away
            DISPLAYSURF.blit(self.backgroundselected,(self.x,self.y))
            DISPLAYSURF.blit(self.image,(self.x,self.y))
            if self.prev != "11":
                redraw()
                self.prev = "11"

    def checkMousedOver(self, mouse, click):
        global move_ticker
        global selectedCharacters
        if (self.x+15+200) > mouse[0] > (self.x+15) and (self.y+15+325) > mouse[1] > (self.y+15):
            self.highlighted = True
            #redraw()
            if self.selected == False:
                #pygame.draw.rect(DISPLAYSURF, (0,0,0), self.frameOne)#black
                #pygame.draw.rect(DISPLAYSURF, (255,255,255), self.frameTwo)#white
                #DISPLAYSURF.blit(self.backgroundselected,(self.x,self.y))
                #self.draw()#char
                if click[0] == 1 and move_ticker == 0:
                    print("selected")
                    selectedCharacters.append(self.img)
                    self.selected = True
                    #redraw()
                    move_ticker = 30
                    #redraw()
            elif click[0] == 1 and self.selected == True and move_ticker == 0:
                print("unselected")
                selectedCharacters.remove(self.img)
                self.selected = False
                #redraw()
                move_ticker = 30
        else:
            self.highlighted = False
            #redraw()
        #elif self.selected == False:
            #pygame.draw.rect(DISPLAYSURF, (255,255,255), self.frameOne)
            #DISPLAYSURF.blit(self.background,(self.x,self.y))
            #self.draw()




"""
    def checkMousedOver(self, mouse, click):
        global move_ticker
        global selectedCharacters
        if (self.x+15+200) > mouse[0] > (self.x+15) and (self.y+15+325) > mouse[1] > (self.y+15):
            self.highlighted = True
            if self.selected == False:
                #print("almost")
                #pygame.draw.rect(DISPLAYSURF, (0,0,0), self.frameOne)#black
                #pygame.draw.rect(DISPLAYSURF, (255,255,255), self.frameTwo)#white
                DISPLAYSURF.blit(self.backgroundselected,(self.x,self.y))
                self.draw()#char
                if click[0] == 1 and move_ticker == 0:
                    print("selected")
                    selectedCharacters.append(self.img)
                    self.selected = True
                    move_ticker = 30
                    redraw()
            elif click[0] == 1 and self.selected == True and move_ticker == 0:
                print("unselected")
                selectedCharacters.remove(self.img)
                self.selected = False
                move_ticker = 30
        elif self.selected == False:
            pygame.draw.rect(DISPLAYSURF, (255,255,255), self.frameOne)
            DISPLAYSURF.blit(self.background,(self.x,self.y))
            self.draw()
"""

def redraw():
    print("redraw")
    DISPLAYSURF.fill((255,255,255))

def characterSelectScreenBegin():
    global DISPLAYSURF
    print("char Select")
    #Initialzing
    pygame.init()

    #Setting up FPS
    FPS = 60
    FramePerSec = pygame.time.Clock()

    #Setting up Fonts
    font = pygame.font.SysFont("Vivaldi", 60)
    font_small = pygame.font.SysFont("Verdana", 30)

    #Create a white screen
    DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    DISPLAYSURF.fill((255,255,255))


    pygame.display.set_caption("Character Select")

    #mult, pixels acrtoss, pixels down
    c1 = CharacterSelect(150, 150, 75, "valentine_pics/bride2.png")
    c2 = CharacterSelect(150, 800, 75, "valentine_pics/bride1.png")
    c3 = CharacterSelect(150, 150, 425, "valentine_pics/groom1.png")
    c4 = CharacterSelect(150, 800, 425, "valentine_pics/groom2.png")

    characters = pygame.sprite.Group()
    characters.add(c1)
    characters.add(c2)
    characters.add(c3)
    characters.add(c4)

    global move_ticker

    #Game Loop

    while True:

        if move_ticker > 0:
            move_ticker -= 1

        #Cycles through all events occuring
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        textSurf = font.render('Character Select', False, (0, 0, 0))
        DISPLAYSURF.blit(textSurf,((SCREEN_WIDTH/2)-200,25))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        #Moves and Re-draws all Sprites
        for currChar in characters:
            #if currChar.selected == False:
            currChar.draw()
            currChar.checkMousedOver(mouse, click)

        pygame.display.update()
        FramePerSec.tick(FPS)

        if len(selectedCharacters) == 2:
            return selectedCharacters
