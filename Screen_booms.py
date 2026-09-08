import pygame
import random
import consts
import game_field

img= pygame.image.load('mine.png')
screenB = pygame.display.set_mode((1000,500))


def background():

    screenB.fill((0,0,0))
    start_p=[0,0]
    end_p=[consts.BOARD_COLS * 20, 0]

    for i in range(consts.BOARD_COLS):
         start_p[1]+=consts.CELL_SIZE
         end_p[1]+=consts.CELL_SIZE
         pygame.draw.line(screenB,(0, 139, 0),start_p,
                 end_p, 1)

    end_p[1]=consts.BOARD_ROWS*20
    end_p[0]=0
    start_p[0]=0
    start_p[1]=0
    for i in range(consts.BOARD_ROWS):
         start_p[1]+=consts.CELL_SIZE
         end_p[1]+=consts.CELL_SIZE
         pygame.draw.line(screenB,(0, 139, 0),start_p,
                 end_p, 1)