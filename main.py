import game_field
import Screen
import pygame
import soldier

def main ():
    board_game = game_field.empty_board()
    print(board_game)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        Screen.background()
        # bushs()
        soldier.Soldier()
        pygame.display.update()



main()