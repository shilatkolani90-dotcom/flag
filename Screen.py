import pygame
import random
import consts
import game_field
from pygame.locals import*
img= pygame.image.load('grass.png')

screen = pygame.display.set_mode([1000,500])
def background():
   screen.fill((69, 139, 0))

def bushs():

     for i in range(consts.BUSHS):
      row = random.randint(0, (consts.BOARD_ROWS - 1)*16)
      col = random.randint(0, (consts.BOARD_COLS - 1)*16)
      screen.blit(pygame.transform.scale(img, (100, 60)), (row,col ))

def game():
    game_field.draw(screen)


