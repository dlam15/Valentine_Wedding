#Imports
import pygame, sys
import time
from pygame.locals import *
import random, time

#Other Variables for use in the program
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
DISPLAYSURF = ""
selectedCharacters = []
move_ticker = 0

class CharacterSelect(pygame.sprite.Sprite):
    def __init__(self, multiplier, x, y, image):
        super().__init__()
        self.img = pygame.image.load(image)
        self.image = pygame.transform.scale(self.img,(3*multiplier,4*multiplier))#3:4 ratio works decent
        self.frameOne = (x+15, y+15, 200, 325)
        self.frameTwo = (x+20,y+20, 190, 315)
        self.x = x
        self.y = y
        self.selected = False

    def draw(self):
        DISPLAYSURF.blit(self.image,(self.x,self.y))

    def checkMousedOver(self, mouse, click):
        global move_ticker
        global selectedCharacters
        if (self.x+15+200) > mouse[0] > (self.x+15) and (self.y+15+325) > mouse[1] > (self.y+15):
            if self.selected == False:
                #print("almost")
                pygame.draw.rect(DISPLAYSURF, (0,0,0), self.frameOne)#black
                pygame.draw.rect(DISPLAYSURF, (255,255,255), self.frameTwo)#white
                self.draw()#char
                if click[0] == 1 and move_ticker == 0:
                    print("selected")
                    selectedCharacters.append(self.img)
                    self.selected = True
                    move_ticker = 30
            elif click[0] == 1 and self.selected == True and move_ticker == 0:
                print("unselected")
                selectedCharacters.remove(self.img)
                self.selected = False
                move_ticker = 30
        elif self.selected == False:
            pygame.draw.rect(DISPLAYSURF, (255,255,255), self.frameOne)
            self.draw()


def characterSelectScreenBegin():
    global DISPLAYSURF
    print("char Select")
    #Initialzing
    pygame.init()

    #Setting up FPS
    FPS = 60
    FramePerSec = pygame.time.Clock()

    #Setting up Fonts
    font = pygame.font.SysFont("Verdana", 60)
    font_small = pygame.font.SysFont("Verdana", 30)

    #Create a white screen
    DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    DISPLAYSURF.fill((255,255,255))


    pygame.display.set_caption("Character Select")

    c1 = CharacterSelect(150, 50, 150, "valentine_pics/bride2.png")
    c2 = CharacterSelect(150, 50, 500, "valentine_pics/bride1.png")
    c3 = CharacterSelect(150, 500, 150, "valentine_pics/groom1.png")
    c4 = CharacterSelect(150, 500, 500, "valentine_pics/groom2.png")

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
        DISPLAYSURF.blit(textSurf,((SCREEN_WIDTH/2)-275,50))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        #Moves and Re-draws all Sprites
        for currChar in characters:
            if currChar.selected == False:
                currChar.draw()
            currChar.checkMousedOver(mouse, click)

        pygame.display.update()
        FramePerSec.tick(FPS)

        if len(selectedCharacters) == 2:
            return selectedCharacters
