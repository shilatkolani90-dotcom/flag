import game_field
import Screen
import pygame
import Screen_booms
import soldier
import consts



stats = {
    "soldier_place" : (0,0),
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

    Screen.background()
    Screen.bushs()
    soldier.Soldier()
    Screen.flag_display()
    # Screen_booms.background()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()


main()