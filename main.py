import pygame
import random
from pygame.locals import *
import time

def changeBG(img):
    background = pygame.image.load(img)
    bg = pygame.transform.scale (background,(w,h))
    screen.blit(bg,(0,0))


pygame.init()
pygame.display.set_caption('Recycling_game')
w = 900
h = 700
screen = pygame.display.set_mode([w,h])

class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.imgae.load('bin.jpg').convert_alpha()
        self.image = pygame.transform.scale(self.image,(45,45))
        self.rect = self.image.get_rect()

class Recyclable(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image = pygame.imgae.load(img).convert_alpha()
        self.image = pygame.transform.scale(self.image,(45,45))
        self.rect = self.image.get_rect()

class Non_recyclable(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.imgae.load('apple.jpeg').convert_alpha()
        self.image = pygame.transform.scale(self.image,(45,45))
        self.rect = self.image.get_rect()

images=["pencil.webp","can.jpg","box.jpg"]

item_list = pygame.sprite.Group()
allsprites = pygame.sprite.Group()
apple_list = pygame.sprite.Group()


for i in range(50):
    item = Recyclable(random.choice(images))
    item.rect.x = random.randrange(w)
    item.rect.y = random.randrange(h)
    item_list.add(item)
    allsprites.add(item)

for i in range(50):
    apple = Non_recyclable()
    item.rect.x = random.randrange(w)
    item.rect.y = random.randrange(h)
    apple_list.add(apple)
    allsprites.add(apple)

bin = Bin()
allsprites.add(bin)
