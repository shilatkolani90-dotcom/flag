import pygame
import random
import consts
import game_field
from pygame.locals import*
img= pygame.image.load('grass.png')
img_flag= pygame.image.load('flag.png')
pygame.init()
my_font = pygame.font.SysFont('comic Sans', 32)


#קשור לשורות טורים ומשבצות
screen = pygame.display.set_mode((1000,500))

def background():

   text = my_font.render('Welcome to The Flag Game\n have fun!', True,(5, 5, 5) )
   screen.blit(text, (70, 50))
   screen.fill((69, 139, 0))

def flag_display():
    small_img = pygame.transform.scale(img_flag, (100, 100))
    screen.blit(small_img, game_field.flag_place())


def bushs():

     for i in range(consts.BUSHS):
      row = random.randint(0, 1000)
      col = random.randint(0, 500)
      screen.blit(pygame.transform.scale(img, (100, 60)), (row,col ))

def game():
    game_field.draw(screen)


