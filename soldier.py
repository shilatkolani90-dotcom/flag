import pygame
import random
import consts
import game_field
from pygame.locals import*
import Screen
from flag.game_field import soldier

img=pygame.image.load('soldier.png')
small_img = pygame.transform.scale(img, (consts.SOLDIER_ROWS * consts.CELL_SIZE,
                                         consts.SOLDIER_COLS * consts.CELL_SIZE * 2))
def Soldier(soldier_place):
    Screen.screen.blit(small_img, soldier_place)
    pygame.display.update()
