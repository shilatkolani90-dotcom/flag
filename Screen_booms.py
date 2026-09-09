import pygame
import random
import consts
import game_field

img= pygame.image.load('mine.png')
screenB = pygame.display.set_mode((1000,500))
soldier_img = pygame.image.load('soldier_night.png')

def background():

    screenB.fill((0,0,0))
    start_p=[0,0]
    end_p=[consts.BOARD_COLS * 20, 0]

    for i in range(consts.BOARD_ROWS):
         start_p[1]+=consts.CELL_SIZE
         end_p[1]+=consts.CELL_SIZE
         pygame.draw.line(screenB,(0, 139, 0),start_p,
                 end_p, 1)

    start_p=[980,980]
    end_p=[980,0]
    for i in range(consts.BOARD_COLS-1):
         pygame.draw.line(screenB,(0, 139, 0),start_p,
                          end_p, 1)
         start_p[0] -= consts.CELL_SIZE
         end_p[0] -= consts.CELL_SIZE

def booms():

    list_mine=game_field.Main_booms
    for i in range(consts.MINES_COUNT):
        row = list_mine[i][0]
        col = list_mine[i][1]
        screenB.blit(pygame.transform.scale(img,
            ((consts.MINE_COLS*consts.CELL_SIZE),(consts.MINE_ROWS*consts.CELL_SIZE))),
                     (col*20, row*20))

def Soldier_booms(soldier_place):
    small_img=pygame.transform.scale(soldier_img,(consts.SOLDIER_COLS*consts.CELL_SIZE*2,
                                          consts.SOLDIER_ROWS*consts.CELL_SIZE))
    screenB.blit(small_img,soldier_place)