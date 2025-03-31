import sys

import pygame

from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.level import Level
from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                player_score = [0, 0]  # [Player1, Player2]
                level = Level(self.window, 'lvl1', menu_return)
                menu_return = menu.run()

            elif menu_return == MENU_OPTION[3]:  # Se for a opção 'Sair'
                pygame.quit()  # Fecha a janela
                quit()  # Termina o jogo
            else:
                pygame.quit()
                sys.exit()
