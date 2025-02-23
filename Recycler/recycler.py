import pgzrun
import pygame
from pygame.locals import *
import random
pygame.init()
pygame.font.init()
import time


screen = pygame.display.set_mode((900, 700))
background = pygame.image.load("images/background.png")
bg = pygame.transform.scale(background, (900, 700))
screen.blit(bg, (0, 0))

class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/bin.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect()

class Recyclable(pygame.sprite.Sprite):
    def __init__(self, img):
        super().__init__()
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (40, 60))
        self.rect = self.image.get_rect()

class Non_recyclable(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/bag.png")
        self.image = pygame.transform.scale(self.image, (40, 60))
        self.rect = self.image.get_rect()

images = ["images/box.png", "images/item1.png", "images/pencil.png"]

all_sprites = pygame.sprite.Group()
non_recyclables = pygame.sprite.Group()
recyclables = pygame.sprite.Group()

for i in range(10):
    recyclable = Recyclable(random.choice(images))
    recyclable.rect.x = random.randint(0,900)
    recyclable.rect.y = random.randint(0, 700)
    all_sprites.add(recyclable)
    recyclables.add(recyclable)

for i in range(15):
    non_recyclable = Non_recyclable()
    non_recyclable.rect.x = random.randint(0, 900)
    non_recyclable.rect.y = random.randint(0, 700)
    all_sprites.add(non_recyclable)
    non_recyclables.add(non_recyclable)

bin = Bin()
all_sprites.add(bin)

score = int(0)
playing = True
clock = pygame.time.Clock()
start_time = time.time()
font = pygame.font.SysFont("Arial", 20)


text = font.render("Score: "+str(score), (True), "red")

while playing:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
    
    time_elapsed = time.time() - start_time
    if time_elapsed >= 60:
        if score > 50:
            text = font.render("You Win", True, "blue")
            #change the background to a winning image
        else:
            #change the background to a losing image
            text = font.render("You Lose", True, "blue")
        screen.blit(text, (300, 300))
    else:
        count_down = font.render("Time Left", str(time_elapsed), True, "blue")
        screen.blit(count_down, (800, 650))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if bin.rect.y>0:
                bin.rect.y -= 5
        if keys[pygame.K_DOWN]:
            if bin.rect.y<700:
                bin.rect.y += 5
        if keys[pygame.K_RIGHT]:
            if bin.rect.x<900:
                bin.rect.x+=5
        if keys[pygame.K_LEFT]:
            if bin.rect.x>0:
                bin.rect.x-=5
        
        hit_list = pygame.sprite.spritecollide(bin, all_sprites, True)

        hit_list_plastic = pygame.sprite.spritecollide(bin, non_recyclables, True)

        for i in hit_list:
            score = score + 1
            text = font.render("Score: ",score, True, "blue")
        
        for plastic in hit_list_plastic:
            score -= 2
            text = font.render("Score: " + str(score), True, "blue")

        screen.blit(text, (500, 500))
        
        all_sprites.draw(screen)
    
    pygame.display.update()

pygame.quit()
            
