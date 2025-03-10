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
        self.image = pygame.image.load('bin.jpg').convert_alpha()
        self.image = pygame.transform.scale(self.image,(45,45))
        self.rect = self.image.get_rect()

class Recyclable(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.image = pygame.transform.scale(self.image,(45,45))
        self.rect = self.image.get_rect()

class Non_recyclable(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('apple.jpeg').convert_alpha()
        self.image = pygame.transform.scale(self.image,(45,45))
        self.rect = self.image.get_rect()

images=["pencil.webp","can.jpg","box.jpeg"]

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

WHITE = (255,255,255)
RED = (255,0,0)

playing = True
score = 0
clock = pygame.time.Clock()
start_time = time.time()
font = pygame.font.SysFont("Times New Roman",22)
timingFont = pygame.font.SysFont("Times New Roman",22)
text = font.render("Score : "+ str(0),True,WHITE)

while playing :
    clock.tick(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        
    timeElapsed = time.time()-start_time
    if timeElapsed >= 60:
        if score > 50:
            text = font.render("Bin loot successful",True,WHITE)
            changeBG("win.jpg")
        else:
            text=font.render("Better luck next time",True,WHITE)
            changeBG("lose.avif")
        screen.blit(text,(250,40))
    else:
        changeBG("bg2.jpg")
        countDown=timingFont.render("Time Left:"+str(60-int(timeElapsed)),True,WHITE)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if bin.rect.y > 0:
            bin.rect.y -= 5
    if keys[pygame.K_DOWN]:
        if bin.rect.y < 630:
            bin.rect.y += 5

    if keys[pygame.K_LEFT]:
        if bin.rect.x > 0:
            bin.rect.x -= 5
    if keys[pygame.K_DOWN]:
        if bin.rect.x < 850:
            bin.rect.x += 5

    item_hit_list = pygame.sprite.spritecollide(bin,item_list,True)
    plastic_hit_list = pygame.sprite.spritecollide(bin,apple_list,True)
    
    for item in item_hit_list:
        score += 1
        text=font.render("Score :"+str(score),True,WHITE)
    for apple in plastic_hit_list:
        score -= 5
        text=font.render("Score :"+str(score),True,WHITE)

    screen.blit(text,(20,50))

    allsprites.draw(screen)
    
    pygame.display.update()



pygame.quit()
