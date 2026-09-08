import pygame
import random
import consts
import game_field
from pygame.locals import*
import Screen
img=pygame.image.load('soldier.png')

def Soldier():
    small_img=pygame.transform.scale(img,(120,120))
    Screen.screen.blit(small_img,game_field.soldier_place())
