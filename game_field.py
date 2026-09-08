import random
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
    main_bomb()

    return BOARD_GAME


def soldier ():
    for i in range(consts.SOLDIER_ROWS):
        for j in range(consts.SOLDIER_COLS):
            BOARD_GAME[i][j] = consts.SOLDIER


def add_soldier ():
    for i in range(consts.FLAG_ROWS):
        for j in range(consts.FLAG_COLS):
            BOARD_GAME[i][j] = consts.FLAG




def flag():
    for i in range(consts.BOARD_ROWS):
        BOARD_GAME[i].reverse()
    BOARD_GAME.reverse()
    add_soldier()
    for i in range(consts.BOARD_ROWS):
        BOARD_GAME[i].reverse()
    BOARD_GAME.reverse()






def main_bomb ():
    x=0
    y=0
    randon_place=[]
    for i in range(consts.MINES_COUNT):
        y=random.randint(0, 24)
        x=random.randint(0,49)
        while [x,y] in randon_place and (BOARD_GAME[y][x] == "SOLDIER" or BOARD_GAME[y][x] == "FLAG") :
            y = random.randint(0,24)
            x = random.randint(0,49)
        BOARD_GAME[y][x] = "MAIN"
        BOARD_GAME[y][x+1] = "MAIN"
        BOARD_GAME[y][x+2] = "MAIN"





def soldier_place():
    for i in range(consts.BOARD_ROWS):
        for j in range(consts.BOARD_COLS):
            if BOARD_GAME[i][j] == "SOLDIER":
                return ((i*20,j*20))
    return ((0,0))

##

def flag_place():
    for i in range(consts.BOARD_ROWS):
        for j in range(consts.BOARD_COLS):
            if BOARD_GAME[i][j] == "FLAG":
                return ((i*20,j*20))
    return ((0,0))