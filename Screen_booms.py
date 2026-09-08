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

    for i in range(consts.BOARD_ROWS):
         start_p[1]+=consts.CELL_SIZE
         end_p[1]+=consts.CELL_SIZE
         pygame.draw.line(screenB,(0, 139, 0),start_p,
                 end_p, 1)

    start_p=[980,980]
    end_p=[980,0]
    for i in range(consts.BOARD_COLS):
         pygame.draw.line(screenB,(0, 139, 0),start_p,
                          end_p, 1)
         start_p[0] -= consts.CELL_SIZE
         end_p[0] -= consts.CELL_SIZE

# def booms():
#     for i in range(consts.BUSHS):
#         row = random.randint(0, 1000)
#         col = random.randint(0, 500)
#         screen.blit(pygame.transform.scale(img, (100, 60)), (row, col))