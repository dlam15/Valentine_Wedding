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
move_ticker = 15

class CharacterSelect(pygame.sprite.Sprite):
    def __init__(self, multiplier, x, y, image, imageFlipped, shiftRight, shiftDown):
        super().__init__()
        self.img = pygame.image.load(image)
        self.pathToImage = image
        self.pathToFlippedImage = imageFlipped
        self.backgroundimg = pygame.image.load("valentine_pics/icon_regular.png")
        self.selectedimg = pygame.image.load("valentine_pics/icon_highlight.png")
        self.image = pygame.transform.scale(self.img,(3*multiplier,4*multiplier))#3:4 ratio works decent
        self.background = pygame.transform.scale(self.backgroundimg,(3*multiplier,4*multiplier))
        self.backgroundselected = pygame.transform.scale(self.selectedimg,(3*(multiplier-20),4*(multiplier-20)))
        self.frameOne = (x+15, y+15, 200, 325)
        self.frameTwo = (x+20,y+20, 190, 315)
        self.x = x
        self.y = y
        self.selected = False
        self.highlighted = False
        self.prev = "00";
        self.shiftRight = shiftRight
        self.shiftDown = shiftDown

    def draw(self):
        if self.selected == False and self.highlighted == False:
            #regular background
            DISPLAYSURF.blit(self.background,(self.x,self.y))
            DISPLAYSURF.blit(self.image,(self.x + self.shiftRight, self.y + self.shiftDown))
            if self.prev != "00":
                self.prev = "00"
        else:
            #highlighted background
            DISPLAYSURF.blit(self.backgroundselected,(self.x+10,self.y+20))
            DISPLAYSURF.blit(self.image,(self.x + self.shiftRight, self.y + self.shiftDown))
            if self.prev != "01":
                self.prev = "01"


    def checkMousedOver(self, mouse, click):
        global move_ticker
        global selectedCharacters
        if (self.x+15+200) > mouse[0] > (self.x+15) and (self.y+15+325) > mouse[1] > (self.y+15):
            self.highlighted = True
            if self.selected == False:
                if click[0] == 1 and move_ticker == 0:
                    print("selected")
                    if len(selectedCharacters) == 1:
                        selectedCharacters.append(self.pathToImage)
                    else:
                        selectedCharacters.append(self.pathToFlippedImage)
                    self.selected = True
                    move_ticker = 15
            elif click[0] == 1 and self.selected == True and move_ticker == 0:
                print("unselected")
                selectedCharacters.remove(self.pathToImage)
                self.selected = False
                move_ticker = 15
        else:
            self.highlighted = False




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

    #Create a white screen
    DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    background = pygame.image.load('./valentine_pics/cupid2.png').convert_alpha()
    backgroundImage = pygame.transform.scale(background,(SCREEN_WIDTH,SCREEN_HEIGHT))
    DISPLAYSURF.blit(backgroundImage,(0,0))


    pygame.display.set_caption("Character Select")

    #mult, pixels acrtoss, pixels down
    #FIX , ADD FLIPPED IMG AS 2nd PARAM
    c1 = CharacterSelect(150, 150, 75, "valentine_pics/bride2.png", "valentine_pics/bride2.png", 0,0)
    c2 = CharacterSelect(150, 800, 75, "valentine_pics/bride1.png","valentine_pics/bride1.png", 50,0)
    c3 = CharacterSelect(150, 150, 425, "valentine_pics/groom1.png","valentine_pics/groom1.png", 30,0)
    c4 = CharacterSelect(150, 800, 425, "valentine_pics/groom2.png","valentine_pics/groom2.png", 40,20)

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
            currChar.draw()
            currChar.checkMousedOver(mouse, click)

        pygame.display.update()
        FramePerSec.tick(FPS)

        #once 2 characters are selected, we can return to the controller
        if len(selectedCharacters) == 2:
            return selectedCharacters
