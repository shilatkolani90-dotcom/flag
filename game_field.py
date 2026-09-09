import random
from flag import consts

BOARD_GAME = []
Main_booms =[]

#empty board

def empty_board ():
    for i in range(consts.BOARD_ROWS):
        row=[]
        for j in range(consts.BOARD_COLS):
            row.append("EMPTY")
        BOARD_GAME.append(row)
    soldier()
    flag()
    global Main_booms
    Main_booms=main_bomb()

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





#x+2 >= len(BOARD_GAME[y])-1
def main_bomb ():
    x=0
    y=0
    random_place=[]
    for i in range(consts.MINES_COUNT):
        x=random.randint(0, (consts.BOARD_ROWS-1))
        y=random.randint(0,(consts.BOARD_COLS-1)-2)
        while [x,y] in random_place or (BOARD_GAME[x][y] == "SOLDIER" or BOARD_GAME[x][y] == "FLAG"):
            x = random.randint(0,(consts.BOARD_ROWS-1))
            y = random.randint(0,(consts.BOARD_COLS-1)-2)
        random_place.append((x,y))
        BOARD_GAME[x][y] = "MAIN"
        BOARD_GAME[x][y+1] = "MAIN"
        BOARD_GAME[x][y+2] = "MAIN"
    return random_place



"""
def soldier_place():
    for i in range(consts.BOARD_ROWS):
        for j in range(consts.BOARD_COLS):
            if BOARD_GAME[i][j] == "SOLDIER":
                return ((i*20,j*20))
    return ((0,0))"""

