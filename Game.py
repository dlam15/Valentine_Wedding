import pygame

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
        self.storage = pygame.image.load('./valentine_pics/storage_room.png').convert_alpha()#for pixel transparenc

        #adjusting size of rooms
        self.hallway = pygame.transform.scale(self.hallway,(ROOMWIDTH,HEIGHT))
        self.wedding = pygame.transform.scale(self.wedding,(ROOMWIDTH,HEIGHT))
        self.reception = pygame.transform.scale(self.reception,(ROOMWIDTH,HEIGHT))
        self.kitchen = pygame.transform.scale(self.kitchen,(ROOMWIDTH,HEIGHT))
        self.change1 = pygame.transform.scale(self.change1,(ROOMWIDTH,HEIGHT))
        self.change2 = pygame.transform.scale(self.change2,(ROOMWIDTH,HEIGHT))
        self.storage = pygame.transform.scale(self.storage,(ROOMWIDTH,HEIGHT))

 

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
        pygame.quit()

            
    def hallway(self):
        self.display.blit(self.hallway, (0,0))
        pygame.display.update()

        pygame.event.clear()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse = pygame.mouse.get_pos()

        self.status = [2,True]
        
    def wedding(self):
        self.display.blit(self.wedding, (0,0))
        pygame.display.update()

        pygame.event.clear()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse = pygame.mouse.get_pos()
        self.status = [3,True]
        
    def reception(self):
        self.display.blit(self.reception, (0,0))
        pygame.display.update()

        pygame.event.clear()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse = pygame.mouse.get_pos()
        self.status = [4,True]
        
    def kitchen(self):
        self.display.blit(self.kitchen, (0,0))
        pygame.display.update()

        pygame.event.clear()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse = pygame.mouse.get_pos()
        self.status = [5,True]
        
    def change1(self):
        self.display.blit(self.change1, (0,0))
        pygame.display.update()

        pygame.event.clear()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse = pygame.mouse.get_pos()
        self.status = [6,True]
        
    def change2(self):
        self.display.blit(self.change2, (0,0))
        pygame.display.update()

        pygame.event.clear()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse = pygame.mouse.get_pos()
        self.status = [7,True]
        
    def storage(self):
        self.display.blit(self.storage, (0,0))
        pygame.display.update()
        
        pygame.event.clear()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse = pygame.mouse.get_pos()
        self.status = [2,False]
Game("bride1", "bride2")
