from random import random

from flag import consts

BOARD_GAME = []
TEMP =[]

#empty board
def empty_board ():
    for i in range(consts.BOARD_ROWS):
        for j in range(consts.BOARD_COLS):
            TEMP.append(consts.EMPTY_PLACE)
        BOARD_GAME.append(TEMP)
        tamp = []
    soldier()
    flag()
    #main_bomb()

    return BOARD_GAME


def soldier ():
    for i in range(consts.SOLDIER_ROWS):
        for j in range(consts.SOLDIER_COLS):
            BOARD_GAME[i][j] = consts.SOLDIER


def flag():
    for i in range(consts.BOARD_ROWS,0):
        for j in range(consts.BOARD_COLS,0):
            BOARD_GAME[i][j]= consts.FLAG


def main_bomb ():
    x=0
    y=0
    randon_place=[]
    for i in range(consts.MINES_COUNT):
        y=random(0,25)
        x=random(0,50)





      """  
        while [x,y] in randon_place or on soldier or on flag:  
            y = random(0, 25)
            x = random(0, 50)
        randon_place.append([x,y])
    
    for i in range(consts.MINES_COUNT):
        for"""


def soldier_place():
    for i in range(consts.BOARD_ROWS):
        for j in range(consts.BOARD_COLS):
            if BOARD_GAME[i][j] == "SOLDIER":
                return ((i,j))
    return ((0,0))

