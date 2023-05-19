#sprite
from random import random
import pygame
import numpy as np

FPS = 50 #(15)
HIGHT = 1100
WIDTH = 600
LIGHTGRAY = (211,211,211)
BIG = (150,210,245)
GREEN = (20,25,18)
SMART = (130,190,230)
GOD = (110,170,215)
ABC = (100,155,200)
RED = (200,100,130)


#遊戲初始化 and 創建視窗
pygame.init()
screen = pygame.display.set_mode((HIGHT,WIDTH))
pygame.display.set_caption("GAME")
clock = pygame.time.Clock()
ori_x = 0
ori_y = 0

class Rock(pygame.sprite.Sprite):
    speed1 = 1
    speed2 = 1
   
    
    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = ori_x #np.random.randint(0, WIDTH - self.rect.width)
        self.rect.y = ori_y #np.random.randint(30, 600)
        self.speed2 = np.random.randint(2,10)
        self.speed1 = np.random.randint(1,4)
   
        
    def update(self):
        
        self.rect.y += self.speed1
        self.rect.x += self.speed2
      
            
            
            
        
  #      if self.rect.top > HIGHT:
             #self.rect.x = np.random.randint(0, WIDTH - self.rect.width)
             #self.rect.y = np.random.randint(30, 40)
            # self.rect.x = np.random.randint(24,40)
           #  self.rect.y = np.random.randint(40,30)


            
class Player(pygame.sprite.Sprite):
    speed = 1
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((15,9))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = 550
        self.rect.y = 300 
              
    def update(self):
        key_pressed = pygame.key.get_pressed()
        if self.rect.x <= 1000:
            if key_pressed[pygame.K_RIGHT]:
                self.rect.x += self.speed
        if self.rect.x >= 50:
            if key_pressed[pygame.K_LEFT]:
                self.rect.x -= self.speed
                
        if self.rect.y <= 500:
            if key_pressed[pygame.K_DOWN]:
                self.rect.y += self.speed
        if self.rect.y >= 50:
            if key_pressed[pygame.K_UP]:
                self.rect.y -= self.speed

class Player1(pygame.sprite.Sprite):
    speed1 =1
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((2000,700))
        self.image.fill(BIG)
        self.rect = self.image.get_rect()
        self.rect.center = (200,200) 
    def update(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            self.rect.x -= self.speed1
        if key_pressed[pygame.K_LEFT]:
            self.rect.x += self.speed1
        if key_pressed[pygame.K_DOWN]:
            self.rect.y -= self.speed1
        if key_pressed[pygame.K_UP]:
            self.rect.y += self.speed1
            
class Player2(pygame.sprite.Sprite):
    speed1 =1
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5000,700))
        self.image.fill(SMART)
        self.rect = self.image.get_rect()
        self.rect.center = (0,800) 
    def update(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            self.rect.x -= self.speed1
        if key_pressed[pygame.K_LEFT]:
            self.rect.x += self.speed1
        if key_pressed[pygame.K_DOWN]:
            self.rect.y -= self.speed1
        if key_pressed[pygame.K_UP]:
            self.rect.y += self.speed1
            
class Player3(pygame.sprite.Sprite):
    speed1 =1
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5000,700))
        self.image.fill(GOD)
        self.rect = self.image.get_rect()
        self.rect.center = (0,1500) 
    def update(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            self.rect.x -= self.speed1
        if key_pressed[pygame.K_LEFT]:
            self.rect.x += self.speed1
        if key_pressed[pygame.K_DOWN]:
            self.rect.y -= self.speed1
        if key_pressed[pygame.K_UP]:
            self.rect.y += self.speed1
            

class Player4(pygame.sprite.Sprite):
    speed1 =1
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5000,700))
        self.image.fill(ABC)
        self.rect = self.image.get_rect()
        self.rect.center = (0,2100)
    def update(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            self.rect.x -= self.speed1
        if key_pressed[pygame.K_LEFT]:
            self.rect.x += self.speed1
        if key_pressed[pygame.K_UP]:
            self.rect.y += self.speed1 
        if key_pressed[pygame.K_DOWN]:
            self.rect.y -= self.speed1
        
        
    
all_sprites = pygame.sprite.Group()


 
player = Player()
player1 = Player1()
player2 = Player2()
player3 = Player3()
player4 = Player4()
rock = Rock()

all_sprites.add(player3)
all_sprites.add(player4)
all_sprites.add(player1)
all_sprites.add(player2)
all_sprites.add(player)
all_sprites.add(rock)

    





#game 迴圈
running = True


while running:
    for i in range(30):
        r = Rock()
    all_sprites.add(r)
    clock.tick(FPS)
    
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_RIGHT]:
        ori_x -= 1
    elif key_pressed[pygame.K_LEFT]:  
        ori_x += 1  
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
#更新遊戲
    all_sprites.update()

    if player.rect.y  >= 500:
        player1.speed1 = 10
        player2.speed1 = 10
        player3.speed1 = 10
        player4.speed1 = 10
    elif player.rect.y <=50:
        player1.speed1 = 10
        player2.speed1 = 10
        player3.speed1 = 10
        player4.speed1 = 10
    else:
        player1.speed1 = 1
        player2.speed1 = 1
        player4.speed1 = 1
        player3.speed1 = 1
    all_sprites.update()
    if player.rect.x >= 1000:
        player1.speed1 = 10
        player4.speed1 = 10
        player2.speed1 = 10
        player4.speed1 = 10
    elif player.rect.x <= 50:
        player1.speed1 = 10
        player2.speed1 = 10
        player4.speed1 = 10
        player3.speed1 = 10
    else:
        player1.speed1 = 1
        player2.speed1 = 1
        player4.speed1 = 1
        player3.speed1 = 1
          

#畫面顯示
    screen.fill((LIGHTGRAY))
    all_sprites.draw(screen)
    pygame.display.update()

pygame.quit()