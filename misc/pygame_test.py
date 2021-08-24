import os
print(os.getcwd())

import pygame
import random
from pygame.locals import *
pygame.init() 

# frames
FPS = 30
FramePerSec = pygame.time.Clock()

# colors
red = pygame.Color(255, 0, 0)
blue = (0, 0, 255)

# display
DISPLAYSURF = pygame.display.set_mode((800,1200))
DISPLAYSURF.fill(blue)
pygame.display.set_caption('Game_1')

circle = pygame.draw.circle(DISPLAYSURF, red, (200,50), 30)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('enemy.png')
        self.surf = pygame.Surface((50, 80))
        self.rect = self.surf.get_rect(center = (random.randint(40, 360), 0))

    def move(self):
        self.rect.move_ip(0,10)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370),0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


E1 = Enemy()

# begin game loop
while True:

    # end game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    E1.move()

    DISPLAYSURF.fill(blue)
    E1.draw(DISPLAYSURF)

    pygame.display.update()
    FramePerSec.tick(FPS)