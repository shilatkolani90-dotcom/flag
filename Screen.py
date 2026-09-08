import pygame
from pygame.locals import*
img = pygame.image.load('cloudsrtgtgdg.bmp')
def background():
   screen = pygame.display.set_mode([800,600])
   screen.fill((69, 139, 0))
   pygame.display.update()

def bushs():
 pass


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()