import pygame, sys
import characterSelectScreen

WIDTH = 1550
HEIGHT = 800

class Intro:
    def __init__(self, character1, character2):
        pygame.init()
        self.display = pygame.display.set_mode((WIDTH,HEIGHT))
        self.image1 = pygame.image.load('valentine_pics/intro1.png').convert()
        self.image1 = pygame.transform.scale(self.image1,(WIDTH,HEIGHT))

        #Setting up Fonts
        self.font = pygame.font.SysFont("Verdana", 60)
        self.font_small = pygame.font.SysFont("Verdana", 30)
        
        '''self.character1 = characterSelectScreen.CharacterSelect(300,50,50,character1,character1,0,0)
        self.character2 = characterSelectScreen.CharacterSelect(300,1000,50,character2,character2,0,0)
        self.spriteCharacters = pygame.sprite.Group()
        self.spriteCharacters.add(self.character1)
        self.spriteCharacters.add(self.character2)'''
        #self.characters = [self.character1.rect, self.character2.rect]

        self.display.blit(self.image1, (0,0))
        if character1 == 'valentine_pics/bride1.png':
            self.character1 = pygame.image.load(character1).convert_alpha()
            self.character1  = pygame.transform.scale(self.character1, (1100,1500))
            self.display.blit(self.character1, (100,-75))
        elif character1 == 'valentine_pics/bride2.png':
            self.character1 = pygame.image.load(character1).convert_alpha()
            self.character1  = pygame.transform.scale(self.character1, (1000,1300))
            self.display.blit(self.character1, (25,0))
        elif character1 == 'valentine_pics/groom1.png':
            self.character1 = pygame.image.load(character1).convert_alpha()
            self.character1  = pygame.transform.scale(self.character1, (1100,1500))
            self.display.blit(self.character1, (100,-100))
        elif character1 == 'valentine_pics/groom2.png':
            self.character1 = pygame.image.load(character1).convert_alpha()
            self.character1  = pygame.transform.scale(self.character1, (900,1300))
            self.display.blit(self.character1, (175,25))
            
        if character2 == 'valentine_pics/bride1.png':
            self.character2 = pygame.image.load(character2).convert_alpha()
            self.character2 = pygame.transform.flip(self.character2, True, False)
            self.character2  = pygame.transform.scale(self.character2, (1100,1500))
            self.display.blit(self.character2, (375,-75))
        elif character2 == 'valentine_pics/bride2.png':
            self.character2 = pygame.image.load(character2).convert_alpha()
            self.character2 = pygame.transform.flip(self.character2, True, False)
            self.character2  = pygame.transform.scale(self.character2, (1000,1300))
            self.display.blit(self.character2, (550,0))
        elif character2 == 'valentine_pics/groom1.png':
            self.character2 = pygame.image.load(character2).convert_alpha()
            self.character2 = pygame.transform.flip(self.character2, True, False)
            self.character2  = pygame.transform.scale(self.character2, (1100,1500))
            self.display.blit(self.character2, (375,-100))
        elif character2 == 'valentine_pics/groom2.png':
            self.character2 = pygame.image.load(character2).convert_alpha()
            self.character2 = pygame.transform.flip(self.character2, True, False)
            self.character2  = pygame.transform.scale(self.character2, (900,1300))
            self.display.blit(self.character2, (500,25))

        

        #self.background = pygame.Surface(self.display.get_size()).convert()
        #self.display.blit(self.character1, (50,50))
        #self.display.blit(self.character2, (1300,50))
        #self.spriteCharacters.draw(self.display)
        pygame.draw.rect(self.display, (255,255,255), [100,650, 1350, 150])
        text = self.font_small.render('This couple met on Valentine’s Day and have been together for 5 years and have now ', False, (0,0,0))
        text2 = self.font_small.render('selected me to be their wedding planner.', False, (0,0,0))
        self.display.blit(text, (125,675))
        self.display.blit(text2, (125,725))
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
                    

        #pygame.time.wait(2000)
        self.image2 = pygame.image.load('valentine_pics/intro2.png').convert()
        self.image2 = pygame.transform.scale(self.image2,(WIDTH,HEIGHT))
        self.display.blit(self.image2, (0,0))
        pygame.draw.rect(self.display, (255,255,255), [100,275, 1315, 150])
        text = self.font_small.render('Now they have decided to get married, and I as their wedding planner, plan to give ', False, (0,0,0))
        text2 = self.font_small.render('this lovely couple the wedding of their dreams. Everything was perfect, the ', False, (0,0,0))
        text3 = self.font_small.render('wedding hall, the reception, the wedding cake and decorations. It was all perfect.', False, (0,0,0))
        self.display.blit(text, (125,280))
        self.display.blit(text2, (125,330))
        self.display.blit(text3, (125,380))
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
        #pygame.time.wait(2000)
        self.image2 = pygame.image.load('valentine_pics/intro3.png').convert()
        self.image2 = pygame.transform.scale(self.image2,(WIDTH,HEIGHT))
        self.display.blit(self.image2, (0,0))
        pygame.draw.rect(self.display, (255,255,255), [100,650, 1325, 150])
        text = self.font_small.render("But the ring bearer dog has made a mess, scattered things all over the church, and ", False, (0,0,0))
        text2 = self.font_small.render("has gone missing with the rings.This is PAWSitively awful, and it's up to me to save ", False, (0,0,0))
        text3 = self.font_small.render("their wedding.", False, (0,0,0))
        self.display.blit(text, (125,660))
        self.display.blit(text2, (125,710))
        self.display.blit(text3, (125,760))
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

        '''while self.character1.rect.x<300:
            #pygame.time.delay(5)
            self.character1.rect.x += 2
            self.character2.rect.x -= 2
            self.background.blit(self.image1, (0,0))
            self.spriteCharacters.draw(self.background)
            self.display.blit(self.background, (0,0))
            pygame.display.flip()'''

#Intro('valentine_pics/bride2.png','valentine_pics/groom1.png')
