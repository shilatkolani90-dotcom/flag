import game_field
import Screen
import pygame
import Screen_booms
import soldier

def main ():
    board_game = game_field.empty_board()
    print(board_game)

    # Screen.background()
    # Screen.bushs()
    # soldier.Soldier()
    Screen_booms.background()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()


main()