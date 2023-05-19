
from xml.sax import SAXNotSupportedException
import pygame
import os 
import sys
import numpy as np
from pygame.locals import QUIT
from random import random
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((1100,600))
pygame.display.set_caption("god")
clock = pygame.time.Clock()

##ip_img = pygame.image.load(os.path.join("python","p.png"))
i_img = pygame.image.load(os.path.join("python","A_png.png"))
o_img = pygame.image.load(os.path.join("python","wer.png"))
i_image = pygame.image.load(os.path.join("python","you.png"))

class hooo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = np.random.randint(100,900)
        self.rect.y = np.random.randint(100,300)
        self.speedx = np.random.randint(-3,3)
        self.speedy = np.random.randint(-3,3)
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
         
        if  self.rect.x < 100 :
            self.speedx = np.random.randint(1,3)
        if self.rect.x > 1000 :
            self.speedx = np.random.randint(-3,-1)
        if self.rect.top > 550 :
            self.speedy = np.random.randint(-3,-1)
        if self.rect.bottom < 100 :
           self.speedy = np.random.randint(1,3)
        if self.speedy == 0 or self.speedx == 0 :
            self.speedx = np.random.randint(-3,3)
            self.speedy = np.random.randint(-3,3)
        if lie >= 9 or lie1 >= 9 :
            self.image.fill((0,0,0))
        if lie <= 3 or lie1 <= 5 :
            self.image.fill((100,190,100))
        if lie <= 8 or lie1 <= 8:
            self.image.fill((50,30,50))

        
        hits = pygame.sprite.spritecollide(Player,hooos,False)


        if hits :
            lie == lie - 0.1
            if lie <= 0 :
                hits = pygame.sprite.spritecollide(Player,hooos,True)
                lie == 10
        hits = pygame.sprite.groupcollide(hooos,stones,False,True)
        if hits :
            stone = Stone()
            stone.kill()
        if life <= 0 :
            self.kill()
    
class gun(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,30))
        self.image.fill((100,90,90))
        self.rect = self.image.get_rect()
        self.rect.center = x
        self.rect.top = y
        self.speedy = -20
    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom <= 0 : 
            self.kill()
        hits = pygame.sprite.groupcollide(guns,hooos,True,True)
        if hits:
            lie == lie - 1
            if lie <= 2 :
                hits = pygame.sprite.groupcollide(guns,hooos,True,True)
                Hooo.kill()
            if lie1 <= 0 :
                        lie == 10
class Stone(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(i_img,(15,30))
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.x = np.random.randint(100,900)
        self.rect.y = np.random.randint(-19,-10)
        self.speedx = np.random.randint(-3,3)
        self.speedy = np.random.randint(1,5)
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top >= 550 or self.rect.left <= 20 or self.rect.right >= 1080 :
            self.rect.x = np.random.randint(100,900)
            self.rect.y = np.random.randint(-19,-10)
            self.speedx = np.random.randint(-3,3)
            self.speedy = np.random.randint(1,5)
        

        if life <= 0 :
            self.kill()
            
class GOD(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((200,10))
        self.image.fill((50,50,50))
        self.rect = self.image.get_rect()
        self.rect.x = np.random.randint(300,800)
        self.rect.y = np.random.randint(200,300)
        self.speedx = np.random.randint(-2,2)
    def update(self):
        self.rect.x += self.speedx
        if self.rect.left <= 50 or self.rect.right >= 1050 :
            self.rect.x = np.random.randint(300,800)
            self.rect.y = np.random.randint(200,300)
            self.speedx = np.random.randint(-2,2)
        if self.speedx == 0 :
            self.speedx = np.random.randint(-2,2)
        if life <= 0 :
            self.kill()
class player(pygame.sprite.Sprite):
    speed = np.random.randint(10,15)
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
  ##      self.image = pygame.transform.scale(ip_img,(70,20))
    ##    self.image.set_colorkey((255,255,255))
        self.image = pygame.Surface((50,50))
        self.image.fill((100,100,100))
        self.rect = self.image.get_rect()
        self.rect.x = np.random.randint(100,800)
        self.rect.y = np.random.randint(100,500)
    def update(self):
        key_pressed = pygame.key.get_pressed()
        if self.rect.x >= 50 :
             if key_pressed[pygame.K_LEFT]:
                 self.rect.x -= self.speed
        if self.rect.x <= 1050 :
            if key_pressed[pygame.K_RIGHT]:
                self.rect.x += self.speed
        if self.rect.y <= 550 :
            if key_pressed[pygame.K_DOWN]:
                self.rect.y += self.speed 
        if self.rect.y >= 50 :
            if key_pressed[pygame.K_UP]:
                self.rect.y -= self.speed

            
    def shoot1(self):
        key_pressed = pygame.key.get_pressed()
    
        
        if key_pressed[pygame.K_1]:

                Gun1 = gun1(self.rect.center,self.rect.top)
                all_sprites.add(Gun1)
                gun1s.add(Gun1)
        if key_pressed[pygame.K_SPACE]:
            Gun = gun(self.rect.center,self.rect.top)
            all_sprites.add(Gun)
            guns.add(Gun)

        

class gun1(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(o_img,(50,100))
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = x
        self.rect.top = y
        self.speedy = -2
    def update(self):
        sss = 10
        key_p = pygame.key.get_pressed()
        self.rect.y += self.speedy
        if self.rect.bottom <= 0 or life <= 0   : 
            self.kill()

        if key_p[pygame.K_3]:
            self.speedy = 0
                
            if rrr == 2 :
                self.image = pygame.transform.scale(i_image,(70,70))
                self.image.set_colorkey((255,255,255))
            if rrr == 1 :
                self.image = pygame.transform.scale(i_image,(200,200))
                self.image.set_colorkey((255,255,255))

            if rrr == 0 :
                    self.kill()
                
        elif key_p[pygame.K_2]:
            self.speedy = 0
            if ddd == 1 :
                self.kill()
        else :
            self.speedy = -2
            self.image = pygame.transform.scale(o_img,(60,100))
            self.image.set_colorkey((255,255,255))
            
                            

            
all_sprites = pygame.sprite.Group()
gun1s = pygame.sprite.Group()
hooos = pygame.sprite.Group()
god = pygame.sprite.Group()
stones = pygame.sprite.Group()
guns = pygame.sprite.Group()
Player = player()
gods = GOD()
Hooo = hooo()
stone = Stone()
hooos.add(Hooo)
all_sprites.add(Player)
all_sprites.add(Hooo)
all_sprites.add(gods)
all_sprites.add(stone)
head_font = pygame.font.SysFont(None,50)
text_font = head_font.render('world',False,(0,0,0))
screen.blit(text_font,(0,0))

now = datetime.now()
count_time = 50
life = 3
gas = 1
lie = 10
fad1 = 3
fad = 50
goo = 50
goo1 = 5
end_time = 200
running = True
xcv = 20
hoo = 3
fff = 1
ddd = 15
rrr = 5
lie = 10
lie1 = 10
ccc= 50
cccd = 50
for i in range(xcv):
    stone = Stone()
    all_sprites.add(stone)
    stones.add(stone)
for i in range(5):
    Hooo = hooo()
    hooos.add(Hooo)
    all_sprites.add(Hooo)



while running :
    clock.tick(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Player.shoot1()
            if event.key == pygame.K_1:
                Player.shoot1()
              
    all_sprites.update()  
    
    screen.fill((190,190,190))
    all_sprites.draw(screen)
    if end_time <= 200 :
        goo = goo - 1
        if goo == 0 :
            goo1 = goo1 - 1
            goo = 50
            if goo1 == 0:
                for i in range(50):
                    stone = Stone()
                    all_sprites.add(stone)
                    stones.add(stone)
                    goo1 = 3
    ccc = ccc - 1
    key_p = pygame.key.get_pressed()
    if key_p[pygame.K_3]:
        if ccc <= 0 :
            rrr = rrr - 1
            ccc = 50
            if rrr == -11:
                fff = fff - 1
                rrr = 6
                
    else :
        rrr = 6
        fff = 1333333333
    cccd = cccd - 1
    if key_p[pygame.K_2]:
        if cccd <= 0 :
            ddd = ddd - 1
            cccd = 50
            if ddd == 0 :
                ddd = 15
    
    
    head = "world,time __{:%H-%M-%S}__{}__{}__{}_".format(now,end_time,life,lie)
    text_surface = head_font.render(head,False,(0,0,0))
    screen.blit(text_surface,(10,10))
    

    name = False
    hits = pygame.sprite.groupcollide(guns,hooos,True,False)
    if hits:
        lie = lie - 1.1
    for hit in hits :

        if lie <= 2 :
                hits = pygame.sprite.groupcollide(guns,hooos,True,True)
                self = hooo()
                self.kill()
        if lie <= 0 :
            lie = 10
                

            
    
    
    hits = pygame.sprite.spritecollide(Player,hooos,False)
    if hits:
        life = life - 0.01
        lie = lie - 0.1
    for hit in hits :
        if lie <= 0 :
            hits = pygame.sprite.spritecollide(Player,hooos,True)
            lie = 10
        if life <= 0 :
            gas = 0
    if gas == 0 :
        
        Player.kill()
        head_1font = pygame.font.SysFont(None,300) 
        head1 = "LOSE {}".format(fad1)
        text1_surface = head_1font.render(head1,False,(0,0,0))
        screen.blit(text1_surface,(200,200))

            
    
    hits = pygame.sprite.groupcollide(hooos,stones,False,True)
    for hit in hits :
        
        if hits:
                life = life + 0
    hits = pygame.sprite.groupcollide(gun1s,stones,name,True)
    for hit in hits :
        if hits:
            life = life + 1
    
    hits = pygame.sprite.spritecollide(gods,stones,True)
    for hit in hits :
        all_sprites.add(gods)
        stone = Stone()
        stones.add(stone)
    
    
    hits = pygame.sprite.groupcollide(guns,stones,True,True)
    
    for hit in hits:
        stone = Stone()
        all_sprites.add(stone)
        stones.add(stone)
        if hits:
            life = life + 0.5
    
    hits = pygame.sprite.spritecollide(Player,stones,True)
    
    for hit in hits :
        stone = Stone()
        all_sprites.add(stone)
        stones.add(stone)
        if hits:
            life = life - 1
            if life <= 0 :
                gas = 0
    if gas == 0 :
        fad = fad - 1
        if fad == 0 :
            fad1 = fad1 - 1
            fad = 50
            if fad1 == 0 :
                
                running = False
    if gas <= 0 :
        Player.kill()
        head_1font = pygame.font.SysFont(None,300) 
        head1 = "LOSE {}".format(fad1)
        text1_surface = head_1font.render(head1,False,(0,0,0))
        screen.blit(text1_surface,(200,200))


    
    
    count_time = count_time - 1
    if count_time == 0 :
        end_time = end_time - 1
        count_time = 50
        if end_time == 0 :
              ##os.system("shutdown /t /s 1")
              running = False  
    
    pygame.display.update()
pygame.quit()
    
        