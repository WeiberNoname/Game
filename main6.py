from Crypto.Hash import MD5,SHA512
from random import random 
from pygame.locals import QUIT
from datetime import datetime
import pygame
import os 
import sys
import numpy as np

pygame.init()
screen = pygame.display.set_mode((1100,600))
pygame.display.set_caption("cryptography")
clock = pygame.time.Clock()


class player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20,20))
        self.image.fill((10,50,50))
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 200
    def update(self):
        
        if WWW == 0 :
            
            hash_md5 = MD5.new()
            hash_md5.update(b'hamegg')
            hash_md5.hexdigest()
            head_font = pygame.font.SysFont(None,30)
            text_font = "Passworld_{}___{}".format(end_time,hash_md5)
            text_surface = head_font.render(text_font,False,(0,0,0))
            screen.blit(text_surface,(50,50))


all_sprites = pygame.sprite.Group()
Player = player()
all_sprites.add(Player)
running = True
count_time = 50
end_time = 50
WWW = 1
Word = ""
while running:
    clock.tick(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.update()
    
    screen.fill((200,200,200))
    all_sprites.draw(screen)
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_1]:
        WWW = 0
        hash_md5 = MD5.new()
        hash_md5.update(b'hamegg')
        hash_md5.hexdigest()
        head_font = pygame.font.SysFont(None,30)
        text_font = "Passworld_{}___{}".format(end_time,hash_md5)
        text_surface = head_font.render(text_font,False,(0,0,0))
        screen.blit(text_surface,(50,50))

    
    count_time = count_time - 1
    if count_time == 0 :
        end_time = end_time - 1
        count_time = 50
        if end_time == 0 :
            #os.system("shutdown  /s /t 30")  
            running = False
    pygame.display.update()
pygame.quit()