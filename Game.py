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
        if self.character1 == "bride1" or self.character2 == "bride1":
            self.bride1 = pygame.image.load('./valentine_pics/bride1_copy.png').convert_alpha() #for pixel transparency
            self.bride1 = pygame.transform.scale(self.bride1, (225,404))
            if self.character1 == "bride1":
                self.char1 = self.bride1
            elif self.character2 == "bride1":
                self.char2 = self.bride1

        if self.character1 == "bride2" or self.character2 == "bride2":
            self.bride2 = pygame.image.load('./valentine_pics/bride2_copy.png').convert_alpha() #for pixel transparency
            self.bride2 = pygame.transform.scale(self.bride2, (250,347))
            if self.character1 == "bride2":
                self.char1 = self.bride2
            elif self.character2 == "bride2":
                self.char2 = self.bride2

        if self.character1 == "groom1" or self.character2 == "groom1":
            self.groom1 = pygame.image.load('./valentine_pics/groom1_copy.png').convert_alpha() #for pixel transparency
            self.groom1 = pygame.transform.scale(self.groom1, (200,325))
            if self.character1 == "groom1":
                self.char1 = self.groom1
            elif self.character2 == "groom1":
                self.char2 = self.groom1

        if self.character1 == "groom2" or self.character2 == "groom2":
            self.groom2 = pygame.image.load('./valentine_pics/groom2_copy.png').convert_alpha() #for pixel transparency
            self.groom2 = pygame.transform.scale(self.groom2, (200,300))
            if self.character1 == "groom2":
                self.char1 = self.groom2
            elif self.character2 == "groom2":
                self.char2 = self.groom2

        self.chef = pygame.image.load('./valentine_pics/chefnpc_copy.png').convert_alpha() #for pixel transparency
        self.girl = pygame.image.load('./valentine_pics/happygirl_copy.png').convert_alpha() #for pixel transparency
        self.randomnpc = pygame.image.load('./valentine_pics/randomnpc_copy.png').convert_alpha() #for pixel transparency
        self.weddinghallnpc = pygame.image.load('./valentine_pics/weddinghalnpc_copy.png').convert_alpha() #for pixel transparency
        self.phonenpc = pygame.image.load('./valentine_pics/phoneNPCwithphone_copy.png') #for pixel transparency
        self.nophonenpc = pygame.image.load('./valentine_pics/phoneNPCnophone_copy.png') #for pixel transparency
        self.friendnpc = pygame.image.load('./valentine_pics/friend_copy.png') #for pixel transparency
        self.cryinggirl = pygame.image.load('./valentine_pics/cryinggirl_copy.png') #for pixel transparency
        
        #loading miscellaneous
        self.weddingarc = pygame.image.load('./valentine_pics/weddingarch1.png').convert_alpha()#for pixel transparency
        self.arrowright = pygame.image.load('./valentine_pics/arrow_right.png').convert_alpha()#for pixel transparency
        self.arrowdown = pygame.image.load('./valentine_pics/arrow_down.png').convert_alpha()#for pixel transparency
        self.arrowleft = pygame.image.load('./valentine_pics/arrow_left.png').convert_alpha()#for pixel transparency
        self.door = pygame.image.load('./valentine_pics/door1.png').convert_alpha()#for pixel transparency
        self.poster = pygame.image.load('./valentine_pics/poster2.png').convert_alpha()#for pixel transparency
        self.flower = pygame.image.load('./valentine_pics/flower.png').convert_alpha()#for pixel transparency

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
        self.flower = pygame.transform.scale(self.flower, (125, 125))

        #adjusting characters
        self.chef = pygame.transform.scale(self.chef, (125, 450))
        self.phonenpc = pygame.transform.scale(self.phonenpc, (125, 275))
        self.nophonenpc = pygame.transform.scale(self.nophonenpc, (125, 290))
        self.friendnpc = pygame.transform.scale(self.friendnpc, (125,270))
        self.cryinggirl = pygame.transform.scale(self.cryinggirl, (125,270))
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
        self.font_small = pygame.font.SysFont("Verdana", 20)

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

        self.display.blit(self.phonenpc, (805,275))
        pygame.display.update()

        self.display.blit(self.friendnpc, (925,280))
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
                    elif self.click[0] == 1 and self.mouse[0] in range(615,800) and self.mouse[1] in range (145, 515):
                        self.status = [6,True]
                        done = True
                    elif self.click[0] == 1 and self.mouse[0] in range(1055,1255) and self.mouse[1] in range (145, 515):
                        self.status = [2,True]
                        done = True
                    elif self.click[0] == 1 and self.mouse[0] in range(801,920) and self.mouse[1] in range (301, 515):
                        pygame.draw.rect(self.display, (255,255,255), [100,650, 1100, 150])
                        text = self.font_small.render('Please go away. I’m busy on the phone right now.', False, (0,0,0))
                        self.display.blit(text, (125,675))
                        pygame.display.flip()
                        self.status = [1,True]
                    elif self.click[0] == 1 and self.mouse[0] in range(925,1050) and self.mouse[1] in range (301, 515):
                        pygame.draw.rect(self.display, (255,255,255), [100,650, 1100, 150])
                        text = self.font_small.render(' I lost my tie when I was chasing the dog. I have no clue where it can be and the wedding starts in an hour', False, (0,0,0))
                        self.display.blit(text, (115,675))
                        pygame.display.flip()
                        self.status = [1,True]
                    elif self.click[0] == 1 and self.mouse[0] in range(125,270) and self.mouse[1] in range (301, 515):
                        pygame.draw.rect(self.display, (255,255,255), [100,650, 1100, 150])
                        text1 = self.font_small.render('I hear barking behind the door but the door is locked. The poster has a locksmith’s number, but we don’t', False, (0,0,0))
                        text2 = self.font_small.render('have a phone to use....', False, (0,0,0))
                        self.display.blit(text1, (110,675))
                        self.display.blit(text2, (110,700))
                        pygame.display.flip()
                        self.status = [1,True]
        
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
        got = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    self.status = [1,False]
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse = pygame.mouse.get_pos()
                    print(pygame.mouse.get_pos())
                    self.click = pygame.mouse.get_pressed()
                    
                    if self.click[0] == 1 and self.mouse[0] in range(656,705) and self.mouse[1] in range (725, 775):
                        self.status = [3,True]
                        done = True

                    elif self.click[0] == 1 and self.mouse[0] in range(600,655) and self.mouse[1] in range (725, 775):
                        self.status = [1,True]
                        done = True
                        
                    elif self.click[0] == 1 and self.mouse[0] in range(510,530) and self.mouse[1] in range (220, 585):
                        if not got:
                            pygame.draw.rect(self.display, (255,255,255), [100,650, 1100, 150])
                            self.status = [2,True]
                            self.display.blit(self.flower, (1375,25))
                            pygame.display.update()
                            text = self.font_small.render('Oh there is a rose on the arch, maybe this will be useful.', False, (0,0,0))
                            self.display.blit(text, (115,675))
                            pygame.display.flip()
                            self.display.blit(self.arrowright, (655,725))
                            pygame.display.update()
                            self.display.blit(self.arrowdown, (600,725))
                            pygame.display.update()
                            got = True

                        else:
                            pygame.draw.rect(self.display, (255,255,255), [100,650, 1100, 150])
                            text = self.font_small.render('Hmm.. probably shouldn’t take anymore flowers or the arch would look too barren.', False, (0,0,0))
                            self.display.blit(text, (115,675))
                            pygame.display.flip()
                            self.display.blit(self.arrowright, (655,725))
                            pygame.display.update()
                            self.display.blit(self.arrowdown, (600,725))
                            pygame.display.update()
                            self.status = [2,True]                        

                    elif self.click[0] == 1 and self.mouse[0] in range(775,800) and self.mouse[1] in range (220, 585):
                        if not got:
                            pygame.draw.rect(self.display, (255,255,255), [100,650, 1100, 150])
                            self.status = [2,True]
                            self.display.blit(self.flower, (1375,25))
                            pygame.display.update()
                            text = self.font_small.render('Oh there is a rose on the arch, maybe this will be useful.', False, (0,0,0))
                            self.display.blit(text, (115,675))
                            pygame.display.flip()
                            self.display.blit(self.arrowright, (655,725))
                            pygame.display.update()
                            self.display.blit(self.arrowdown, (600,725))
                            pygame.display.update()
                            got = True

                        else:
                            pygame.draw.rect(self.display, (255,255,255), [100,650, 1100, 150])
                            text = self.font_small.render('Hmm.. probably shouldn’t take anymore flowers or the arch would look too barren.', False, (0,0,0))
                            self.display.blit(text, (115,675))
                            pygame.display.flip()
                            self.display.blit(self.arrowright, (655,725))
                            pygame.display.update()
                            self.display.blit(self.arrowdown, (600,725))
                            pygame.display.update()
                            self.status = [2,True]

                    elif self.click[0] == 1 and self.mouse[0] in range(510,700) and self.mouse[1] in range (125, 219):
                        if not got:
                            pygame.draw.rect(self.display, (255,255,255), [100,650, 1100, 150])
                            self.status = [2,True]
                            self.display.blit(self.flower, (1375,25))
                            pygame.display.update()
                            text = self.font_small.render('Oh there is a rose on the arch, maybe this will be useful.', False, (0,0,0))
                            self.display.blit(text, (115,675))
                            pygame.display.flip()
                            self.display.blit(self.arrowright, (655,725))
                            pygame.display.update()
                            self.display.blit(self.arrowdown, (600,725))
                            pygame.display.update()
                            got = True

                        else:
                            pygame.draw.rect(self.display, (255,255,255), [100,650, 1100, 150])
                            text = self.font_small.render('Hmm.. probably shouldn’t take anymore flowers or the arch would look too barren.', False, (0,0,0))
                            self.display.blit(text, (115,675))
                            pygame.display.flip()
                            self.display.blit(self.arrowright, (655,725))
                            pygame.display.update()
                            self.display.blit(self.arrowdown, (600,725))
                            pygame.display.update()
                            self.status = [2,True]
        
    def reception(self):
        self.display.blit(self.reception, (0,0))
        pygame.display.update()

        self.display.blit(self.cryinggirl, (600,300))
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
                    print(pygame.mouse.get_pos())
                    self.click = pygame.mouse.get_pressed()
                    
                    if self.click[0] == 1 and self.mouse[0] in range(656,705) and self.mouse[1] in range (725, 775):
                        self.status = [4,True]
                        done = True

                    elif self.click[0] == 1 and self.mouse[0] in range(600,655) and self.mouse[1] in range (725, 775):
                        self.status = [2,True]
                        done = True

                    elif self.click[0] == 1 and self.mouse[0] in range(625,700) and self.mouse[1] in range (315, 560):
                        pygame.draw.rect(self.display, (255,255,255), [100,650, 1100, 150])
                        text = self.font_small.render('', False, (0,0,0))
                        self.display.blit(text, (125,675))
                        pygame.display.flip()
                        self.display.blit(self.arrowright, (655,725))
                        pygame.display.update()
                        self.display.blit(self.arrowleft, (600,725))
                        pygame.display.update()
                        self.status = [3,True]
        
    def kitchen(self):
        self.display.blit(self.kitchen, (0,0))
        pygame.display.update()

        self.display.blit(self.chef, (1150, 250))
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
                    print(pygame.mouse.get_pos())
                    self.click = pygame.mouse.get_pressed()

                    if self.click[0] == 1 and self.mouse[0] in range(600,655) and self.mouse[1] in range (725, 775):
                        self.status = [3,True]
                        done = True
                        
                    elif self.click[0] == 1 and self.mouse[0] in range(1175,1230) and self.mouse[1] in range (450, 690):
                        pygame.draw.rect(self.display, (255,255,255), [100,650, 1100, 150])
                        text = self.font_small.render('Ohh nooo!! I lost track of the wedding toppers. Where could they have gone?', False, (0,0,0))
                        self.display.blit(text, (125,675))
                        pygame.display.flip()
                        self.display.blit(self.arrowleft, (600,725))
                        pygame.display.update()
                        self.status = [4,True]

        
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
                        
                    elif self.click[0] == 1 and self.mouse[0] in range(805,870) and self.mouse[1] in range (320, 615):
                        pygame.draw.rect(self.display, (255,255,255), [100,650, 1100, 150])
                        if self.character1 == "bride1":
                            text1 = self.font_small.render('It’s all ruined. Could this day get any worse? Is this one of them? I found it on the floor over ', False, (0,0,0))
                            text2 = self.font_small.render('there and I took it to try to comfort myself.', False, (0,0,0))
                            self.display.blit(text1, (125,675))
                            self.display.blit(text2, (125,700))
                            pygame.display.flip()
                            
                        elif self.character1 == "bride2":
                            text1 = self.font_small.render('You better fix this or I will make sure your career is finished here! Huh... the wedding toppers?', False, (0,0,0))
                            text2 = self.font_small.render('Oh yes,  I found one of them over there. Here take it, you’re lucky I dont fire you for your incompetence.', False, (0,0,0))
                            self.display.blit(text1, (125,675))
                            self.display.blit(text2, (125,700))
                            pygame.display.flip()
                            
                        elif self.character1 == "groom1":
                            text1 = self.font_small.render('What do we do now? Is there any way to fix this? Is this a sign? Should we not get married?', False, (0,0,0))
                            text2 = self.font_small.render ('Wedding toppers? We are missing those too? Wait, could this be one of them? I put it in a drawer ', False, (0,0,0))
                            text3 = self.font_small.render ('since I thought it is bad luck to see your partner before the wedding even if it is just a replica of them.' , False, (0,0,0))
                            self.display.blit(text1, (125,675))
                            self.display.blit(text2, (125,700))
                            self.display.blit(text3, (125,730))
                            pygame.display.flip()
                            
                        elif self.character1 == "groom2":
                            text1 = self.font_small.render('My partner is overreacting, I’m sure everything will work out in the end. Oh.. you’re looking ', False, (0,0,0))
                            text2 = self.font_small.render('for the wedding toppers? Here you go. It looked so good that I took it to look at it in more detail.', False, (0,0,0))
                            self.display.blit(text1, (125,675))
                            self.display.blit(text2, (125,700))
                            pygame.display.flip()
                        self.status =[5,True]
        
    def change2(self):
        self.display.blit(self.change2, (0,0))
        pygame.display.update()

        self.display.blit(self.char2, (925,350))
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

                    if self.click[0] == 1 and self.mouse[0] in range(925,1100) and self.mouse[1] in range (350, 615):
                        pygame.draw.rect(self.display, (255,255,255), [100,650, 1100, 150])
                        if self.character2 == "bride1":
                            text1 = self.font_small.render('It’s all ruined. Could this day get any worse? My wedding is over! The code to my phone …. It’s today', False, (0,0,0))
                            self.display.blit(text1, (125,675))
                            pygame.display.flip()
                            
                        elif self.character2 == "bride2":
                            text1 = self.font_small.render('You better fix this or I will make sure your career is finished here. The code to my phone … ', False, (0,0,0))
                            text2 = self.font_small.render('Why do you need it? Anyways it’s today.', False, (0,0,0))
                            self.display.blit(text1, (125,675))
                            self.display.blit(text2, (125,700))
                            pygame.display.flip()
                            
                        elif self.character2 == "groom1":
                            text1 = self.font_small.render('What do we do now? Is there any way to fix this? Is this a sign? Should we not get married?', False, (0,0,0))
                            text2 = self.font_small.render ('My phone password? Why? Isn’t it too late to fix things? Its today’s date. I think?', False, (0,0,0))
                            self.display.blit(text1, (125,675))
                            self.display.blit(text2, (125,700))
                            pygame.display.flip()
                            
                        elif self.character2 == "groom2":
                            text1 = self.font_small.render('My partner is overreacting, I’m sure everything will work out in the end.', False, (0,0,0))
                            text2 = self.font_small.render('Oh you want my phone password? Sure thing, no problem, it’s the date.', False, (0,0,0))
                            self.display.blit(text1, (125,675))
                            self.display.blit(text2, (125,700))
                            pygame.display.flip()
                        self.status = [6,True]
        
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

        self.display.blit(self.phonenpc, (805,275))
        pygame.display.update()

        self.display.blit(self.friendnpc, (925,280))
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
        
Game("groom1", "groom2")
