import game_field
import Screen
import pygame
import Screen_booms
import soldier
import consts



stats = {
    "soldier_place_img" : [0,0],
    "soldier_legs_place" : [3*consts.CELL_SIZE,2*consts.CELL_SIZE],
    "soldier_move" : False,
    "flag_plac" : (900,400),
    "if_main" : False,
    "stat" : consts.RUNNING_STAT,
    "is_window_open" : True
}


def print_matrix(matrix):
    for row in matrix:
        for col in row:
            print(col, end=" ")
        print(" ")

def main ():
    board_game = game_field.empty_board()
    print_matrix(board_game)
    #
    Screen.background()
    Screen.bushs()
    soldier.Soldier(stats["soldier_place_img"])
    Screen.flag_display()
    # Screen_booms.background()
    # Screen_booms.Soldier_booms(stats["soldier_place_img"])
    # Screen_booms.booms()

    while stats["is_window_open"]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    stats["soldier_legs_place"][1]-= 1
                    stats["soldier_place_img"][1]-=1
                if event.key == pygame.K_RIGHT:
                    stats["soldier_legs_place"][1]+= 1
                    stats["soldier_place_img"][1]+= 1
                if event.key == pygame.K_UP:
                    stats["soldier_legs_place"][0]-= 1
                    stats["soldier_place_img"][0]-= 1
                if event.key == pygame.K_DOWN:
                    stats["soldier_legs_place"][0]+= 1
                    stats["soldier_place_img"][0]+= 1

        pygame.display.update()


main()