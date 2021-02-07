import pygame, time

WIDTH = 1550
HEIGHT = 800
ROOMWIDTH = 1300

class Game:
    character1 = None
    character2 = None

    
    def __init__ (self, character1, character2):
        pygame.init()
        self.character1 = character1
        self.character2 = character2

        #1 = "Hallway"
        #2 = "Wedding hall"
        #3 = "Reception"
        #4 = "Kitchen"
        #5 = "Changing room 1"
        #6 = "Changing room 2"
        #7 = "Storage room"
        #8 = "Poster"
        #9 = "Phone"
        self.status = [1, True]
        
        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
        self.background = pygame.Surface(self.display.get_size()).convert()

        #loading rooms
        self.hallway = pygame.image.load('./valentine_pics/hallway.png').convert_alpha()#for pixel transparency
        self.wedding = pygame.image.load('./valentine_pics/wedding_hall.png').convert_alpha()#for pixel transparency
        self.reception = pygame.image.load('./valentine_pics/reception_hall.png').convert_alpha()#for pixel transparency
        self.kitchen = pygame.image.load('./valentine_pics/kitchen.png').convert_alpha()#for pixel transparency
        self.change1 = pygame.image.load('./valentine_pics/changing_room1.png').convert_alpha()#for pixel transparency
        self.change2 = pygame.image.load('./valentine_pics/changing_room2.png').convert_alpha()#for pixel transparency
        self.storage = pygame.image.load('./valentine_pics/storageroom1.png').convert_alpha()#for pixel transparency

        #loading characters
        self.char1 = pygame.image.load(self.character1).convert_alpha() #for pixel transparency
        self.char2 = pygame.image.load(self.character2).convert_alpha() #for pixel transparency

        #loading miscellaneous
        self.weddingarc = pygame.image.load('./valentine_pics/weddingarch1.png').convert_alpha()#for pixel transparency
        self.arrowright = pygame.image.load('./valentine_pics/arrow_right.png').convert_alpha()#for pixel transparency
        self.arrowdown = pygame.image.load('./valentine_pics/arrow_down.png').convert_alpha()#for pixel transparency
        self.arrowleft = pygame.image.load('./valentine_pics/arrow_left.png').convert_alpha()#for pixel transparency
        self.door = pygame.image.load('./valentine_pics/door1.png').convert_alpha()#for pixel transparency
        self.poster = pygame.image.load('./valentine_pics/poster2.png').convert_alpha()#for pixel transparency


        #adjusting size of rooms
        self.hallway = pygame.transform.scale(self.hallway,(ROOMWIDTH,HEIGHT))
        self.wedding = pygame.transform.scale(self.wedding,(ROOMWIDTH,HEIGHT))
        self.reception = pygame.transform.scale(self.reception,(ROOMWIDTH,HEIGHT))
        self.kitchen = pygame.transform.scale(self.kitchen,(ROOMWIDTH,HEIGHT))
        self.change1 = pygame.transform.scale(self.change1,(ROOMWIDTH,HEIGHT))
        self.change2 = pygame.transform.scale(self.change2,(ROOMWIDTH,HEIGHT))
        self.storage = pygame.transform.scale(self.storage,(ROOMWIDTH,HEIGHT))

        #adjusting miscellaneous
        self.weddingarc = pygame.transform.scale(self.weddingarc, (500, 600))
        self.arrowright = pygame.transform.scale (self.arrowright, (50,50))
        self.arrowdown = pygame.transform.scale (self.arrowdown, (50,50))
        self.arrowleft = pygame.transform.scale (self.arrowleft, (50,50))
        self.door = pygame.transform.scale(self.door, (275, 500))
        self.poster_resize = pygame.transform.scale(self.poster, (100, 100))

        #adjusting characters
        self.char1 = pygame.transform.scale(self.char1, (250,404))
        self.char2 = pygame.transform.scale(self.char2, (250,325))
        self.char1 = pygame.transform.flip(self.char1, True, False)
        self.char2 = pygame.transform.flip(self.char2, True, False)

        #inventory boxes
        pygame.draw.rect(self.display, (255,0,0), [1300,0, 250, 160],4)
        pygame.draw.rect(self.display, (255,182,193), [1300,161, 250, 160],4)
        pygame.draw.rect(self.display, (255,0,0), [1300,321, 250, 160],4)
        pygame.draw.rect(self.display, (255,182,193), [1300,481, 250, 160],4)
        pygame.draw.rect(self.display, (255,0,0), [1300,641, 250, 160],4)

        #Setting up Fonts
        self.font = pygame.font.SysFont("Verdana", 60)
        self.font_small = pygame.font.SysFont("Verdana", 30)

        while self.status[1]:
            pygame.time.wait(100)
            if self.status[0] == 1:
                Game.hallway(self)
            elif self.status[0] == 2:
                Game.wedding(self)
            elif self.status[0] == 3:
                Game.reception(self)
            elif self.status[0] == 4:
                Game.kitchen(self)
            elif self.status[0] == 5:
                Game.change1(self)
            elif self.status[0] == 6:
                Game.change2(self)
            elif self.status[0] == 7:
                Game.storage(self)
            elif self.status[0] == 8:
                Game.poster(self)
        pygame.quit()

            
    def hallway(self):
        self.display.blit(self.hallway, (0,0))
        pygame.display.update()

        self.display.blit(self.poster_resize, (150,200))
        pygame.display.update()

        pygame.event.clear()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    self.status = [1,False]
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse = pygame.mouse.get_pos()
                    print(pygame.mouse.get_pos())
                    self.click = pygame.mouse.get_pressed()

                    #mouse click
                    if self.click[0] == 1 and self.mouse[0] in range(150,250) and self.mouse[1] in range (200, 300):
                        self.status = [8,True]
                        done = True
                    elif self.click[0] == 1 and self.mouse[0] in range(400,600) and self.mouse[1] in range (145, 515):
                        self.status = [5,True]
                        done = True
                    elif self.click[0] == 1 and self.mouse[0] in range(615,815) and self.mouse[1] in range (145, 515):
                        self.status = [6,True]
                        done = True
                    elif self.click[0] == 1 and self.mouse[0] in range(1055,1255) and self.mouse[1] in range (145, 515):
                        self.status = [2,True]
                        done = True
                    elif self.click[0] == 1 and self.mouse[0] in range(125,270) and self.mouse[1] in range (301, 515):
                        pygame.draw.rect(self.display, (255,255,255), [100,650, 1000, 150])
                        text = self.font_small.render('The door is locked! Use a phone to call the locksmith!', False, (0,0,0))
                        self.display.blit(text, (125,675))
                        pygame.display.flip()
                        #time.sleep(3)
                        self.status = [1,True]
                        #done = True
        
    def wedding(self):
        self.display.blit(self.wedding, (0,0))
        pygame.display.update()
        
        self.display.blit(self.weddingarc, (400,75))
        pygame.display.update()

        self.display.blit(self.arrowright, (655,725))
        pygame.display.update()
        
        self.display.blit(self.arrowdown, (600,725))
        pygame.display.update()

        pygame.event.clear()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    self.status = [1,False]
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse = pygame.mouse.get_pos()
                    self.click = pygame.mouse.get_pressed()
                    
                    if self.click[0] == 1 and self.mouse[0] in range(656,705) and self.mouse[1] in range (725, 775):
                        self.status = [3,True]
                        done = True

                    elif self.click[0] == 1 and self.mouse[0] in range(600,655) and self.mouse[1] in range (725, 775):
                        self.status = [1,True]
                        done = True
        
    def reception(self):
        self.display.blit(self.reception, (0,0))
        pygame.display.update()
        
        self.display.blit(self.arrowright, (655,725))
        pygame.display.update()
        
        self.display.blit(self.arrowleft, (600,725))
        pygame.display.update()

        pygame.event.clear()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    self.status = [1,False]
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse = pygame.mouse.get_pos()
                    self.click = pygame.mouse.get_pressed()
                    
                    if self.click[0] == 1 and self.mouse[0] in range(656,705) and self.mouse[1] in range (725, 775):
                        self.status = [4,True]
                        done = True

                    elif self.click[0] == 1 and self.mouse[0] in range(600,655) and self.mouse[1] in range (725, 775):
                        self.status = [2,True]
                        done = True
        
    def kitchen(self):
        self.display.blit(self.kitchen, (0,0))
        pygame.display.update()
        
        self.display.blit(self.arrowleft, (600,725))
        pygame.display.update()
        
        pygame.event.clear()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    self.status = [1,False]
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse = pygame.mouse.get_pos()
                    self.click = pygame.mouse.get_pressed()

                    if self.click[0] == 1 and self.mouse[0] in range(600,655) and self.mouse[1] in range (725, 775):
                        self.status = [2,True]
                        done = True
        
    def change1(self):
        self.display.blit(self.change1, (0,0))
        pygame.display.update()

        self.display.blit(self.char1, (700,300))
        pygame.display.update()

        pygame.event.clear()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    self.status = [1,False]
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse = pygame.mouse.get_pos()
                    print(pygame.mouse.get_pos())
                    self.click = pygame.mouse.get_pressed()
                    if self.click[0] == 1 and self.mouse[0] in range(1040,1240) and self.mouse[1] in range (145, 515):
                        self.status = [1,True]
                        done = True
        
    def change2(self):
        self.display.blit(self.change2, (0,0))
        pygame.display.update()

        self.display.blit(self.char2, (925,300))
        pygame.display.update()

        pygame.event.clear()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    self.status = [1,False]
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse = pygame.mouse.get_pos()
                    print(pygame.mouse.get_pos())
                    self.click = pygame.mouse.get_pressed()
                    if self.click[0] == 1 and self.mouse[0] in range(50,240) and self.mouse[1] in range (145, 515):
                        self.status = [1,True]
                        done = True
        
    def storage(self):
        self.display.blit(self.storage, (0,0))
        pygame.display.update()

        self.display.blit(self.door, (100,50))
        pygame.display.update()
        
        pygame.event.clear()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    self.status = [1,False]
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse = pygame.mouse.get_pos()
                    self.click = pygame.mouse.get_pressed()
                    if self.click[0] == 1 and self.mouse[0] in range(100,375) and self.mouse[1] in range (50, 550):
                        self.status = [1,True]
                        done = True

    def poster(self):
        self.display.blit(self.hallway, (0,0))
        pygame.display.update()

        self.display.blit(self.poster_resize, (150,200))
        pygame.display.update()
        
        self.display.blit(self.poster, (400,25))
        pygame.display.flip()

        pygame.event.clear()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    self.status = [1,False]
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse = pygame.mouse.get_pos()
                    self.click = pygame.mouse.get_pressed()
                    if self.click[0] == 1 and self.mouse[0] in range(425,1000) and self.mouse[1] in range (25, 650):
                        self.status = [1,True]
                        done = True
        
Game('./valentine_pics/bride1_copy.png', './valentine_pics/bride2_copy.png')
