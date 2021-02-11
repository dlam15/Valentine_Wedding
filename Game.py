import pygame, time

WIDTH = 1550
HEIGHT = 800
ROOMWIDTH = 1300

class Game:

    def __init__ (self, character1, character2):
        pygame.init()
        self.character1 = Game.characterName(self, character1)
        self.character2 = Game.characterName(self, character2)

        #1 = "Hallway"
        #2 = "Wedding hall"
        #3 = "Reception"
        #4 = "Kitchen"
        #5 = "Changing room 1"
        #6 = "Changing room 2"
        #7 = "Storage room"
        #8 = "Poster"
        self.status = [1, True]

        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
        self.background = pygame.Surface(self.display.get_size()).convert()

        #loading rooms
        self.hallway = pygame.image.load('./valentine_pics/hallway.png').convert_alpha()
        self.wedding = pygame.image.load('./valentine_pics/wedding_hall.png').convert_alpha()
        self.reception = pygame.image.load('./valentine_pics/reception_hall.png').convert_alpha()
        self.kitchen = pygame.image.load('./valentine_pics/kitchen.png').convert_alpha()
        self.change1 = pygame.image.load('./valentine_pics/changing_room1.png').convert_alpha()
        self.change2 = pygame.image.load('./valentine_pics/changing_room2.0.png').convert_alpha()
        self.change2_noflower = pygame.image.load('./valentine_pics/changing_room2.png').convert_alpha()
        self.storage = pygame.image.load('./valentine_pics/storageroom1.png').convert_alpha()

        #loading characters
        if self.character1 == "bride1" or self.character2 == "bride1":
            self.bride1 = pygame.image.load('./valentine_pics/bride1_copy.png').convert_alpha()
            self.bride1 = pygame.transform.scale(self.bride1, (225,404))
            if self.character1 == "bride1":
                self.char1 = self.bride1
            elif self.character2 == "bride1":
                self.char2 = self.bride1

        if self.character1 == "bride2" or self.character2 == "bride2":
            self.bride2 = pygame.image.load('./valentine_pics/bride2_copy.png').convert_alpha()
            self.bride2 = pygame.transform.scale(self.bride2, (250,347))
            if self.character1 == "bride2":
                self.char1 = self.bride2
            elif self.character2 == "bride2":
                self.char2 = self.bride2

        if self.character1 == "groom1" or self.character2 == "groom1":
            self.groom1 = pygame.image.load('./valentine_pics/groom1_copy.png').convert_alpha()
            self.groom1 = pygame.transform.scale(self.groom1, (200,325))
            if self.character1 == "groom1":
                self.char1 = self.groom1
            elif self.character2 == "groom1":
                self.char2 = self.groom1

        if self.character1 == "groom2" or self.character2 == "groom2":
            self.groom2 = pygame.image.load('./valentine_pics/groom2_copy.png').convert_alpha()
            self.groom2 = pygame.transform.scale(self.groom2, (200,300))
            if self.character1 == "groom2":
                self.char1 = self.groom2
            elif self.character2 == "groom2":
                self.char2 = self.groom2

        #loading NPCs
        self.chef = pygame.image.load('./valentine_pics/chefnpc_copy.png').convert_alpha()
        self.girl = pygame.image.load('./valentine_pics/happygirl_copy.png').convert_alpha()
        self.randomnpc = pygame.image.load('./valentine_pics/randomnpc_copy.png').convert_alpha()
        self.weddinghallnpc = pygame.image.load('./valentine_pics/weddinghalnpc_copy.png').convert_alpha()
        self.phonenpc = pygame.image.load('./valentine_pics/phoneNPCwithphone_copy.png').convert_alpha()
        self.nophonenpc = pygame.image.load('./valentine_pics/phoneNPCnophone_copy.png').convert_alpha()
        self.friendnpc = pygame.image.load('./valentine_pics/friend_copy.png').convert_alpha()
        self.cryinggirl = pygame.image.load('./valentine_pics/cryinggirl_copy.png').convert_alpha()
        self.happygirl = pygame.image.load('./valentine_pics/happygirl_copy.png').convert_alpha()

        #loading miscellaneous
        self.weddingarc = pygame.image.load('./valentine_pics/weddingarch1.png').convert_alpha()
        self.arrowright = pygame.image.load('./valentine_pics/arrow_right.png').convert_alpha()
        self.arrowdown = pygame.image.load('./valentine_pics/arrow_down.png').convert_alpha()
        self.arrowleft = pygame.image.load('./valentine_pics/arrow_left.png').convert_alpha()
        self.door = pygame.image.load('./valentine_pics/door1.png').convert_alpha()
        self.poster = pygame.image.load('./valentine_pics/poster2.png').convert_alpha()
        self.flower = pygame.image.load('./valentine_pics/flower.png').convert_alpha()
        self.tie = pygame.image.load('./valentine_pics/bow_tie_red.png').convert_alpha()
        self.benches = pygame.image.load('./valentine_pics/benches.png').convert_alpha()
        self.onerose = pygame.image.load('./valentine_pics/onerose_copy.png').convert_alpha()
        self.tworose = pygame.image.load('./valentine_pics/tworose_copy.png').convert_alpha()
        self.threerose = pygame.image.load('./valentine_pics/threerose_copy.png').convert_alpha()
        self.fourrose = pygame.image.load('./valentine_pics/fourrose_copy.png').convert_alpha()
        self.fiverose = pygame.image.load('./valentine_pics/fiverose_copy.png').convert_alpha()
        self.phone = pygame.image.load('./valentine_pics/phone_lockscreen.png').convert_alpha()
        self.tie = pygame.image.load('./valentine_pics/bow_tie_red_original.png').convert_alpha()
        self.candy = pygame.image.load('./valentine_pics/chocolatebar_copy.png').convert_alpha()
        self.bone = pygame.image.load('./valentine_pics/dog_bone_small.png').convert_alpha()

        #adjusting size of rooms
        self.hallway = pygame.transform.scale(self.hallway,(ROOMWIDTH,HEIGHT))
        self.wedding = pygame.transform.scale(self.wedding,(ROOMWIDTH,HEIGHT))
        self.reception = pygame.transform.scale(self.reception,(ROOMWIDTH,HEIGHT))
        self.kitchen = pygame.transform.scale(self.kitchen,(ROOMWIDTH,HEIGHT))
        self.change1 = pygame.transform.scale(self.change1,(ROOMWIDTH,HEIGHT))
        self.change2 = pygame.transform.scale(self.change2,(ROOMWIDTH,HEIGHT))
        self.change2_noflower = pygame.transform.scale(self.change2_noflower,(ROOMWIDTH,HEIGHT))
        self.storage = pygame.transform.scale(self.storage,(ROOMWIDTH,HEIGHT))

        #adjusting miscellaneous
        self.weddingarc = pygame.transform.scale(self.weddingarc, (500, 600))
        self.arrowright = pygame.transform.scale (self.arrowright, (50,50))
        self.arrowdown = pygame.transform.scale (self.arrowdown, (50,50))
        self.arrowleft = pygame.transform.scale (self.arrowleft, (50,50))
        self.door = pygame.transform.scale(self.door, (275, 500))
        self.poster_resize = pygame.transform.scale(self.poster, (100, 100))
        self.flower = pygame.transform.scale(self.flower, (125, 125))
        self.tie = pygame.transform.scale(self.tie, (75,60))
        self.onerose = pygame.transform.scale(self.onerose, (125, 125))
        self.tworose = pygame.transform.scale(self.tworose, (125, 125))
        self.threerose = pygame.transform.scale(self.threerose, (125, 125))
        self.fourrose = pygame.transform.scale(self.fourrose, (125, 125))
        self.fiverose = pygame.transform.scale(self.fiverose, (125, 125))
        self.benches = pygame.transform.scale(self.benches, (ROOMWIDTH,HEIGHT))
        self.phone = pygame.transform.scale(self.phone, (50,100))
        self.tie = pygame.transform.scale(self.tie, (100,50))
        self.candy = pygame.transform.scale(self.candy, (100,100))
        self.bone = pygame.transform.scale(self.bone, (100,50))

        #adjusting characters
        self.chef = pygame.transform.scale(self.chef, (125, 450))
        self.phonenpc = pygame.transform.scale(self.phonenpc, (125, 275))
        self.nophonenpc = pygame.transform.scale(self.nophonenpc, (125, 290))
        self.friendnpc = pygame.transform.scale(self.friendnpc, (125,270))
        self.cryinggirl = pygame.transform.scale(self.cryinggirl, (125,270))
        self.happygirl = pygame.transform.scale(self.happygirl, (125, 270))
        self.char1 = pygame.transform.flip(self.char1, True, False)
        self.char2 = pygame.transform.flip(self.char2, True, False)
        self.weddinghallnpc = pygame.transform.scale(self.weddinghallnpc, (125, 270))

        #Setting up Fonts
        self.font = pygame.font.SysFont("Verdana", 60)
        self.font_small = pygame.font.SysFont("Verdana", 20)
        self.font_s = pygame.font.SysFont("Verdana", 40)
        
        #inventory boxes
        pygame.draw.rect(self.display, (255,0,0), [1300,0, 250, 160],4)
        text = self.font_s.render("Inventory", False, (255,182,193))
        self.display.blit(text, (1310,80))
        pygame.draw.rect(self.display, (255,182,193), [1300,161, 250, 160],4) #flower & candy
        pygame.draw.rect(self.display, (255,182,193), [1300,321, 250, 160],4) #toppers
        pygame.draw.rect(self.display, (255,182,193), [1300,481, 250, 160],4) # bone
        pygame.draw.rect(self.display, (255,182,193), [1300,641, 250, 160],4) #phone & tie

        #Setting up Fonts
        self.font = pygame.font.SysFont("Verdana", 60)
        self.font_small = pygame.font.SysFont("Verdana", 20)

        #Setting up lock
        self.lock = True
        self.lockChef = True
        #wedding, reception, kitchen, changing room 1, changing room 2
        self.itemFlowers = [False, False, False, False, False]
        self.flowerCounter = 0
        #changing room, girl
        self.itemToppers = [False, False]
        self.topperCounter = 0
        self.itemTie = False
        self.itemPhone = False
        self.itemBone = False
        self.itemCandy = False

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
        pygame.display.flip()

        if self.itemPhone == False:
            self.display.blit(self.phonenpc, (805,275))
            pygame.display.flip()
        else:
            self.display.blit(self.nophonenpc, (805,275))
            pygame.display.flip()

        self.display.blit(self.friendnpc, (925,280))
        pygame.display.flip()

        self.display.blit(self.poster_resize, (150,200))
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
                        if not self.itemPhone:
                            text1 = self.font_small.render('Man with phone: Please go away. I’m busy on the phone right now.', False, (0,0,0))
                            self.display.blit(text1, (125,675))
                            #pygame.display.flip()
                        else:
                            text1 = self.font_small.render("Man without phone: The phone belonged to one of the people getting married so I don't know what the", False, (0,0,0))
                            text2 = self.font_small.render("password is.", False, (0,0,0))
                            self.display.blit(text1, (125,675))
                            self.display.blit(text2, (125,700))
                        pygame.display.flip()

                        self.status = [1,True]

                    elif self.click[0] == 1 and self.mouse[0] in range(925,1050) and self.mouse[1] in range (301, 515):
                        pygame.draw.rect(self.display, (255,255,255), [100,650, 1100, 150])
                        if not self.itemTie:
                            text1 = self.font_small.render('Friend: I lost my tie when I was chasing the dog. I have no clue where it can be and the wedding starts in', False, (0,0,0))
                            text2 = self.font_small.render('an hour', False, (0,0,0))
                            self.display.blit(text1, (115,675))
                            self.display.blit(text2, (115,700))
                            pygame.display.flip()
                        elif self.itemTie and not self.itemPhone:
                            text1 = self.font_small.render("Friend: You found my tie. Thank you! Hmm? You need a phone? Hey, you stop playing on that phone, it's", False, (0,0,0))
                            text2 = self.font_small.render("        not even yours.", False, (0,0,0))
                            text3 = self.font_small.render("Man with phone: But I am so close to beating this level. Fine here... Opps I accidentally locked it.", False, (0,0,0))
                            text4 = self.font_small.render("        You’ll need to find the owner to get the password.", False, (0,0,0))
                            pygame.draw.rect(self.display, (255,182,193), [1300,641, 250, 160])
                            pygame.draw.rect(self.display, (255,182,193), [1300,641, 250, 160],4)
                            self.display.blit(self.phone, (1375, 650))
                            self.display.blit(text1, (115,675))
                            self.display.blit(text2, (115,700))
                            self.display.blit(text3, (115,725))
                            self.display.blit(text4, (115,750))
                            pygame.display.flip()

                            #wait for user finish reading
                            pygame.time.wait(3500)

                            self.display.blit(self.hallway, (0,0))
                            pygame.display.flip()

                            self.display.blit(self.nophonenpc, (805,275))
                            pygame.display.flip()

                            self.display.blit(self.friendnpc, (925,280))
                            pygame.display.flip()

                            self.display.blit(self.poster_resize, (150,200))
                            pygame.display.flip()

                            #pygame.display.flip()
                            self.itemPhone = True


                        else:
                            text = self.font_small.render('Friend: Now that I got my tie I’m all set for the wedding.', False, (0,0,0))
                            self.display.blit(text, (115,675))
                        pygame.display.flip()

                        self.status = [1,True]

                    elif self.click[0] == 1 and self.mouse[0] in range(125,270) and self.mouse[1] in range (301, 515):
                        if self.lock == True:
                            pygame.draw.rect(self.display, (255,255,255), [100,650, 1100, 150])
                            text1 = self.font_small.render('Me: I hear barking behind the door but the door is locked. The poster has a locksmith’s number, but we', False, (0,0,0))
                            text2 = self.font_small.render('don’t have a phone to use...', False, (0,0,0))
                            self.display.blit(text1, (110,675))
                            self.display.blit(text2, (110,700))
                            pygame.display.flip()
                            self.status = [1,True]
                        else:
                            self.status = [7,True]
                            done = True

    def wedding(self):
        self.display.blit(self.wedding, (0,0))
        pygame.display.flip()

        self.display.blit(self.weddingarc, (400,75))
        pygame.display.flip()

        if not self.itemTie:
            self.display.blit(self.tie, (430, 550))
            self.display.blit(self.benches, (0,0))
            pygame.display.flip()

        self.display.blit(self.weddinghallnpc, (725,415))

        self.display.blit(self.arrowright, (655,725))
        pygame.display.flip()

        self.display.blit(self.arrowdown, (600,725))
        pygame.display.flip()

        pygame.event.clear()
        done = False
        #got = False
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

                    elif self.click[0] == 1 and self.mouse[0] in range(468,501) and self.mouse[1] in range (558, 603):
                        if not self.itemTie:
                            text = self.font_small.render('Is someone missing a tie? We better keep it and find who is missing it.', False, (0,0,0))
                            self.itemTie = True
                            pygame.draw.rect(self.display, (255,182,193), [1300,641, 250, 160])
                            pygame.draw.rect(self.display, (255,182,193), [1300,641, 250, 160],4)
                            self.display.blit(self.tie, (1375, 700))
                            self.display.blit(self.wedding, (0,0))
                            self.display.blit(self.weddingarc, (400,75))
                            self.display.blit(self.weddinghallnpc, (725,415))
                            pygame.draw.rect(self.display, (255,255,255), [100,650, 1100, 150])
                            self.display.blit(text, (115,675))
                            self.display.blit(self.arrowright, (655,725))
                            self.display.blit(self.arrowdown, (600,725))
                            pygame.display.flip()
                            self.status = [2,True]

                    elif self.click[0] == 1 and self.mouse[0] in range(749,821) and self.mouse[1] in range (425, 675):
                        pygame.draw.rect(self.display, (255,255,255), [100,650, 1100, 150])
                        if self.itemFlowers[0] and self.itemFlowers[1] and self.itemFlowers[2] \
                           and self.itemFlowers[3] and self.itemFlowers[4]:
                            if not self.itemCandy:
                                text1 = self.font_small.render('Woman: A bouquet for me? I was planning to catch the bouquet after the wedding but', False, (0,0,0))
                                text2 = self.font_small.render('this is nice too. Thank you so much! Have some chocolate and enjoy the wedding', False, (0,0,0))
                                self.display.blit(text1, (115,675))
                                self.display.blit(text2, (115,700))
                                pygame.draw.rect(self.display, (255,182,193), [1300,161, 250, 160])
                                pygame.draw.rect(self.display, (255,182,193), [1300,161, 250, 160],4)
                                self.display.blit(self.candy, (1375,190))
                                self.itemCandy = True
                            else:
                               text1 = self.font_small.render('Hi there! Did you like the chocolate?', False, (0,0,0))
                               self.display.blit(text1, (115,675))    
                        else:
                            text1 = self.font_small.render('Woman: It’s so incredible that they’re getting married on Valentine’s Day! I plan on getting married on', False, (0,0,0))
                            text2 = self.font_small.render('Valentine’s day too you know. I’m definitely going to get that bouquet during the toss.', False, (0,0,0))
                            self.display.blit(text1, (115,675))
                            self.display.blit(text2, (115,700))

                        self.display.blit(self.arrowright, (655,725))
                        self.display.blit(self.arrowdown, (600,725))
                        pygame.display.flip()
                        self.status = [2,True]



                    elif self.click[0] == 1 and (self.mouse[0] in range(510,530) and self.mouse[1] in range (220, 585))\
                         or (self.mouse[0] in range(775,800) and self.mouse[1] in range (220, 585))\
                         or (self.mouse[0] in range(510,700) and self.mouse[1] in range (125, 219)):
                        if not self.itemFlowers[0]:
                            pygame.draw.rect(self.display, (255,255,255), [100,650, 1100, 150])
                            self.status = [2,True]
                            self.flowerCounter = self.flowerCounter + 1
                            pygame.draw.rect(self.display, (255,182,193), [1300,161, 250, 160])
                            pygame.draw.rect(self.display, (255,182,193), [1300,161, 250, 160],4)
                            if self.flowerCounter == 1:
                                self.display.blit(self.onerose, (1375,190))
                            elif self.flowerCounter == 2:
                                self.display.blit(self.tworose, (1375, 190))
                            elif self.flowerCounter == 3:
                                self.display.blit(self.threerose, (1375, 190))
                            elif self.flowerCounter == 4:
                                self.display.blit(self.fourrose, (1375, 190))
                            elif self.flowerCounter == 5:
                                self.display.blit(self.fiverose, (1375, 190))
                            #pygame.display.update()
                            text = self.font_small.render('Me: Oh there is a rose on the arch, maybe this will be useful.', False, (0,0,0))
                            
                            self.itemFlowers[0] = True

                        else:
                            pygame.draw.rect(self.display, (255,255,255), [100,650, 1100, 150])
                            text = self.font_small.render('Me: Hmm... probably shouldn’t take anymore flowers or the arch would look too barren.', False, (0,0,0))
                        self.display.blit(text, (115,675))
                        #pygame.display.flip()
                        self.display.blit(self.arrowright, (655,725))
                        #pygame.display.flip()
                        self.display.blit(self.arrowdown, (600,725))
                        pygame.display.flip()
                        self.status = [2,True]

                    '''elif self.click[0] == 1 and self.mouse[0] in range(775,800) and self.mouse[1] in range (220, 585):
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
                            self.status = [2,True]'''

    def reception(self):
        self.topper1 = self.char1
        self.topper1 = pygame.transform.scale(self.topper1, (75,75))
        
        self.display.blit(self.reception, (0,0))
        pygame.display.flip()

        if self.itemToppers[1] == True:
            self.display.blit(self.happygirl, (600,300))
            pygame.display.flip()
        else:
            self.display.blit(self.cryinggirl, (600,300))
            pygame.display.flip()

        self.display.blit(self.arrowright, (655,725))
        pygame.display.flip()

        self.display.blit(self.arrowleft, (600,725))
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
                    print(pygame.mouse.get_pos())
                    self.click = pygame.mouse.get_pressed()

                    if self.click[0] == 1 and self.mouse[0] in range(656,705) and self.mouse[1] in range (725, 775):
                        self.status = [4,True]
                        done = True

                    elif self.click[0] == 1 and self.mouse[0] in range(600,655) and self.mouse[1] in range (725, 775):
                        self.status = [2,True]
                        done = True
                        
                    elif self.click[0] == 1 and self.mouse[0] in range(980,1010)and self.mouse[1] in range (395, 450):
                        if not self.itemFlowers[1]:
                            pygame.draw.rect(self.display, (255,255,255), [100,650, 1100, 150])
                            self.itemFlowers[1]= True
                            text = self.font_small.render('Me: Oh there is a rose in the centerpiece of the table, maybe this will be useful.', False, (0,0,0))
                            self.display.blit(text, (125,675))
                            self.flowerCounter = self.flowerCounter + 1
                            pygame.draw.rect(self.display, (255,182,193), [1300,161, 250, 160])
                            pygame.draw.rect(self.display, (255,182,193), [1300,161, 250, 160],4)
                            if self.flowerCounter == 1:
                                self.display.blit(self.onerose, (1375,190))
                            elif self.flowerCounter == 2:
                                self.display.blit(self.tworose, (1375, 190))
                            elif self.flowerCounter == 3:
                                self.display.blit(self.threerose, (1375, 190))
                            elif self.flowerCounter == 4:
                                self.display.blit(self.fourrose, (1375, 190))
                            elif self.flowerCounter == 5:
                                self.display.blit(self.fiverose, (1375, 190))
                        else:
                            pygame.draw.rect(self.display, (255,255,255), [100,650, 1100, 150])
                            self.status = [3,True]
                            text = self.font_small.render('Me: Hmm… probably shouldn’t take anymore flowers or there would be no flowers in the centerpiece.', False, (0,0,0))
                            self.display.blit(text, (125,675))
                        self.display.blit(self.arrowright, (655,725))
                        self.display.blit(self.arrowleft, (600,725))
                        pygame.display.flip()
                        self.status = [3,True]
                            
                    elif self.click[0] == 1 and self.mouse[0] in range(625,700) and self.mouse[1] in range (315, 560):
                        pygame.draw.rect(self.display, (255,255,255), [100,650, 1100, 150])
                        if not self.itemCandy:
                            text = self.font_small.render('Me: That kid is crying pretty loud. Maybe she’ll quiet down if she gets some sweets.', False, (0,0,0))
                            self.display.blit(text, (125,675))
                        elif self.itemCandy and not self.itemToppers[1]:
                            self.display.blit(self.reception, (0,0))

                            self.display.blit(self.happygirl, (600,300))

                            pygame.draw.rect(self.display, (255,255,255), [100,650, 1100, 150])

                            text = self.font_small.render('Kid: Mommy says that I should always say thank you! Here you can have this. I found it on the ground.', False, (0,0,0))
                            text2 = self.font_small.render('It looks just like a person getting married!', False, (0,0,0))
                            self.itemToppers[1] = True
                            self.display.blit(self.topper1, (1375, 375))
                            self.display.blit(text, (125,675))
                            self.display.blit(text2, (125,700))

                            pygame.display.flip()
                        else:
                            text = self.font_small.render('Kid: Mommy says that I should always say thank you!', False, (0,0,0))
                            self.display.blit(text, (125,675))
                        #pygame.display.flip()
                        self.display.blit(self.arrowright, (655,725))
                        #pygame.display.update()
                        self.display.blit(self.arrowleft, (600,725))
                        pygame.display.flip()
                        self.status = [3,True]

    def kitchen(self):
        self.display.blit(self.kitchen, (0,0))
        pygame.display.flip()

        self.display.blit(self.chef, (1150, 250))
        pygame.display.flip()

        self.display.blit(self.arrowleft, (600,725))
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
                    print(pygame.mouse.get_pos())
                    self.click = pygame.mouse.get_pressed()

                    if self.click[0] == 1 and self.mouse[0] in range(600,655) and self.mouse[1] in range (725, 775):
                        self.status = [3,True]
                        done = True

                    elif self.click[0] == 1 and self.mouse[0] in range(1175,1230) and self.mouse[1] in range (450, 690):
                        pygame.draw.rect(self.display, (255,255,255), [100,650, 1100, 150])
                        if not self.itemToppers[0] or not self.itemToppers[1]:
                            text = self.font_small.render('Chef: Ohh nooo!! I lost track of the wedding toppers. Where could they have gone?', False, (0,0,0))
                            self.lockChef = False
                        elif not self.itemBone:
                            text = self.font_small.render('Chef: Oh my gosh you found them! Thank you! Here take this bone I heard there was a dog here somewhere.', False, (0,0,0))
                            self.display.blit(text, (125,675))
                            pygame.draw.rect(self.display, (255,182,193), [1300,481, 250, 160])
                            pygame.draw.rect(self.display, (255,182,193), [1300,481, 250, 160],4)
                            self.display.blit(self.bone, (1375,510))
                            self.itemBone = True
                        else:
                            text = self.font_small.render('Chef: Thanks again for the help but I’m too busy to talk right now.', False, (0,0,0))
                            self.display.blit(self.bone, (1375, 520))
                        self.display.blit(text, (125,675))
                        self.display.blit(self.arrowleft, (600,725))
                        pygame.display.flip()
                        self.status = [4,True]
                        
                    elif self.click[0] == 1 and self.mouse[0] in range(905,920) and self.mouse[1] in range (460, 490):
                        if not self.itemFlowers[2]:
                            pygame.draw.rect(self.display, (255,255,255), [100,650, 1100, 150])
                            self.itemFlowers[2]= True
                            text = self.font_small.render('Me: Oh there is a rose beside the cake, maybe this will be useful.', False, (0,0,0))
                            self.display.blit(text, (125,675))
                            self.flowerCounter = self.flowerCounter + 1
                            pygame.draw.rect(self.display, (255,182,193), [1300,161, 250, 160])
                            pygame.draw.rect(self.display, (255,182,193), [1300,161, 250, 160],4)
                            if self.flowerCounter == 1:
                                self.display.blit(self.onerose, (1375,190))
                            elif self.flowerCounter == 2:
                                self.display.blit(self.tworose, (1375, 190))
                            elif self.flowerCounter == 3:
                                self.display.blit(self.threerose, (1375, 190))
                            elif self.flowerCounter == 4:
                                self.display.blit(self.fourrose, (1375, 190))
                            elif self.flowerCounter == 5:
                                self.display.blit(self.fiverose, (1375, 190))
                        else:
                            pygame.draw.rect(self.display, (255,255,255), [100,650, 1100, 150])
                            text = self.font_small.render('Me: Hmm… probably shouldn’t take anymore flowers or the cake won’t have any more decorations.', False, (0,0,0))
                            self.display.blit(text, (125,675))
                        self.display.blit(self.arrowleft, (600,725))
                        pygame.display.flip()
                        self.status = [4,True]


    def change1(self):
        self.topper2 = self.char2
        self.topper2 = pygame.transform.scale(self.topper2, (75,75))
        
        if self.itemFlowers[3] == True:
            self.display.blit(self.change1, (0,0))
        else:
            self.display.blit(self.change1, (0,0))
            self.flower_resize = pygame.transform.scale(self.flower, (25,25))
            self.display.blit(self.flower_resize, (85, 420))
        pygame.display.flip()

        self.display.blit(self.char1, (700,300))
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
                    print(pygame.mouse.get_pos())
                    self.click = pygame.mouse.get_pressed()
                    if self.click[0] == 1 and self.mouse[0] in range(1040,1240) and self.mouse[1] in range (145, 515):
                        self.status = [1,True]
                        done = True
                    elif self.click[0] == 1 and self.mouse[0] in range(85,100) and self.mouse[1] in range (400, 440):
                        if not self.itemFlowers[3]:
                            self.itemFlowers[3]= True
                            self.display.blit(self.change1, (0,0))
                            self.display.blit(self.char1, (700,300))
                            pygame.draw.rect(self.display, (255,255,255), [100,650, 1100, 150])
                            text = self.font_small.render('Me: Oh there is a rose on the closet, maybe this will be useful.', False, (0,0,0))
                            self.flowerCounter = self.flowerCounter + 1
                            pygame.draw.rect(self.display, (255,182,193), [1300,161, 250, 160])
                            pygame.draw.rect(self.display, (255,182,193), [1300,161, 250, 160],4)
                            if self.flowerCounter == 1:
                                self.display.blit(self.onerose, (1375,190))
                            elif self.flowerCounter == 2:
                                self.display.blit(self.tworose, (1375, 190))
                            elif self.flowerCounter == 3:
                                self.display.blit(self.threerose, (1375, 190))
                            elif self.flowerCounter == 4:
                                self.display.blit(self.fourrose, (1375, 190))
                            elif self.flowerCounter == 5:
                                self.display.blit(self.fiverose, (1375, 190))
                            self.display.blit(text, (125,675))
                            pygame.display.flip()
                            
                    elif self.click[0] == 1 and self.mouse[0] in range(750,870) and self.mouse[1] in range (310, 615):
                        pygame.draw.rect(self.display, (255,255,255), [100,650, 1100, 150])
                        if self.character1 == "bride1":
                            if not self.itemToppers[0] and not self.lockChef:
                                text1 = self.font_small.render("Bride: Hmm... You're looking for the wedding toppers?... Is this one of them? I found it on the floor over", False, (0,0,0))
                                text2 = self.font_small.render("there and I took it to try to comfort myself.", False, (0,0,0))
                                self.display.blit(text1, (125,675))
                                self.display.blit(text2, (125,700))
                                self.display.blit(self.topper2, (1475, 375))
                                pygame.display.flip()
                                self.itemToppers[0] = True
                            else:
                                text1 = self.font_small.render("Bride: It's all ruined. Could this day get any worse?", False, (0,0,0))
                                self.display.blit(text1, (125,675))
                                pygame.display.flip()


                        elif self.character1 == "bride2":
                            if not self.itemToppers[0] and not self.lockChef:
                                text1 = self.font_small.render('Bride: Huh... the wedding toppers? Oh yes,  I found one of them over there. Here take it, you’re lucky I', False, (0,0,0))
                                text2 = self.font_small.render("don't fire you for your incompetence.", False, (0,0,0))
                                self.display.blit(self.topper2, (1475, 375))
                                self.display.blit(text1, (125,675))
                                self.display.blit(text2, (125,700))
                                pygame.display.flip()
                                self.itemToppers[0] = True
                            else:
                                text1 = self.font_small.render('Bride: You better fix this or I will make sure your career is finished here!', False, (0,0,0))
                                self.display.blit(text1, (125,675))
                                pygame.display.flip()

                        elif self.character1 == "groom1":
                            if not self.itemToppers[0] and not self.lockChef:
                                text1 = self.font_small.render ('Groom: Wedding toppers? We are missing those too? Wait, could this be one of them? I put it in a drawer', False, (0,0,0))
                                text2 = self.font_small.render ('since I thought it is bad luck to see your partner before the wedding even if it is just a replica of them.' , False, (0,0,0))
                                self.display.blit(self.topper2, (1475, 375))
                                self.display.blit(text1, (125,675))
                                self.display.blit(text2, (125,700))
                                pygame.display.flip()
                                self.itemToppers[0] = True
                            else:
                                text1 = self.font_small.render('Groom: What do we do now? Is there any way to fix this? Is this a sign? Should we not get married?', False, (0,0,0))
                                self.display.blit(text1, (125,675))
                                pygame.display.flip()

                        elif self.character1 == "groom2":
                            if not self.itemToppers[0] and not self.lockChef:
                                text1 = self.font_small.render('Groom: Oh.. you’re looking for the wedding toppers? Here you go. It looked so good that I took it to look', False, (0,0,0))
                                text2 = self.font_small.render('at it in more detail.', False, (0,0,0))
                                self.display.blit(self.topper2, (1475, 375))
                                self.display.blit(text1, (125,675))
                                self.display.blit(text2, (125,700))
                                pygame.display.flip()
                                self.itemToppers[0] = True
                            else:
                                text1 = self.font_small.render('Groom: My partner is overreacting, I’m sure everything will work out in the end.', False, (0,0,0))
                                self.display.blit(text1, (125,675))
                                pygame.display.flip()

                        self.status =[5,True]

    def change2(self):
        if self.itemFlowers[4] == True:
            self.display.blit(self.change2_noflower, (0,0))
        else:
            self.display.blit(self.change2, (0,0))
        pygame.display.flip()

        self.display.blit(self.char2, (925,350))
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
                    print(pygame.mouse.get_pos())
                    self.click = pygame.mouse.get_pressed()
                    if self.click[0] == 1 and self.mouse[0] in range(50,240) and self.mouse[1] in range (145, 515):
                        self.status = [1,True]
                        done = True
                    elif self.click[0] == 1 and self.mouse[0] in range(425,450) and self.mouse[1] in range (395, 435):
                        if not self.itemFlowers[4]:
                            self.itemFlowers[4]= True
                            
                            self.display.blit(self.change2_noflower, (0,0))
                            self.display.blit(self.char2, (925,350))
                            pygame.draw.rect(self.display, (255,255,255), [100,650, 1100, 150])
                            text = self.font_small.render('Me: Oh there is a rose on the closet, maybe this will be useful.', False, (0,0,0))
                            self.flowerCounter = self.flowerCounter + 1
                            pygame.draw.rect(self.display, (255,182,193), [1300,161, 250, 160])
                            pygame.draw.rect(self.display, (255,182,193), [1300,161, 250, 160],4)
                            if self.flowerCounter == 1:
                                self.display.blit(self.onerose, (1375,190))
                            elif self.flowerCounter == 2:
                                self.display.blit(self.tworose, (1375, 190))
                            elif self.flowerCounter == 3:
                                self.display.blit(self.threerose, (1375, 190))
                            elif self.flowerCounter == 4:
                                self.display.blit(self.fourrose, (1375, 190))
                            elif self.flowerCounter == 5:
                                self.display.blit(self.fiverose, (1375, 190))
                            self.display.blit(text, (125,675))
                            pygame.display.flip()
                            self.status = [6,True]
                            
                    elif self.click[0] == 1 and self.mouse[0] in range(925,1100) and self.mouse[1] in range (350, 615):
                        pygame.draw.rect(self.display, (255,255,255), [100,650, 1100, 150])
                        if self.character2 == "bride1":
                            if not self.itemPhone:
                                text1 = self.font_small.render('Bride: It’s all ruined. Could this day get any worse? ', False, (0,0,0))
                            else:
                                text1 = self.font_small.render('Bride: My wedding is over! Hmm? ... We can use my phone we can call a locksmith. Well here...', False, (0,0,0))
                                self.lock = False
                                #maybe want to fade out here
                            self.display.blit(text1, (125,675))
                            pygame.display.flip()

                        elif self.character2 == "bride2":
                            if not self.itemPhone:
                                text1 = self.font_small.render('Bride: You better fix this or I will make sure your career is finished here. ', False, (0,0,0))
                            else:
                                text1 = self.font_small.render("Bride: My phone password for the locksmith? What's wrong with your phone? ... Fine here.", False, (0,0,0))
                                self.lock = False
                            self.display.blit(text1, (125,675))
                            pygame.display.flip()

                        elif self.character2 == "groom1":
                            if not self.itemPhone:
                                text1 = self.font_small.render('Groom: What do we do now? Is there any way to fix this? Is this a sign? Should we not get married?', False, (0,0,0))
                            else:
                                text1 = self.font_small.render('Groom: Password to my phone? To call a locksmith? Why? Isn’t it too late to fix things?... Here take it.', False, (0,0,0))
                                self.lock = False
                            self.display.blit(text1, (125,675))
                            pygame.display.flip()

                        elif self.character2 == "groom2":
                            if not self.itemPhone:
                                text1 = self.font_small.render('Groom: My partner is overreacting, I’m sure everything will work out in the end.', False, (0,0,0))
                            else:
                                text1 = self.font_small.render('Groom: Oh you want my phone password to call a locksmith? Sure thing, no problem.', False, (0,0,0))
                                self.lock = False
                            self.display.blit(text1, (125,675))
                            pygame.display.flip()
                     
                        self.status = [6,True]

    def storage(self):
        self.display.blit(self.storage, (0,0))
        pygame.display.flip()

        self.display.blit(self.door, (100,50))
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
                    if self.click[0] == 1 and self.mouse[0] in range(100,375) and self.mouse[1] in range (50, 550):
                        self.status = [1,True]
                        done = True
                    elif self.click[0] == 1 and self.mouse[0] in range(870,925) and self.mouse[1] in range (500, 675):
                        if not self.itemBone:
                          pygame.draw.rect(self.display, (255,255,255), [100,650, 1100, 150])
                          text1 = self.font_small.render('Dog: Grrrrr….', False, (0,0,0))
                          text2 = self.font_small.render('Me:  Hmm seems like I won’t be able to get close to it.', False, (0,0,0))
                          self.display.blit(text1, (125,675))
                          self.display.blit(text2, (125,700))
                          pygame.display.flip()
                        else:
                            done = True
                            self.status = [1,False]

    def poster(self):
        self.display.blit(self.hallway, (0,0))
        pygame.display.flip()

        self.display.blit(self.phonenpc, (805,275))
        pygame.display.flip()

        self.display.blit(self.friendnpc, (925,280))
        pygame.display.flip()

        self.display.blit(self.poster_resize, (150,200))
        pygame.display.flip()

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

    def characterName(self, file):
        temp = file.split('/')[1]
        return(temp.split('.')[0])
#Game("groom1", "groom2")
