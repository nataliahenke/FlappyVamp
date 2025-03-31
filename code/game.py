import pygame, sys

from code.menu import Menu


class Game:
    def __init__(self):

        pygame.init()
        self.window = pygame.display.set_mode((600, 480))

    def run(self):

        while True:
            menu = Menu(self.window)
            menu.run()
            pass



            #for event in pygame.event.get():
                #if event.type == pygame.QUIT:
                   # pygame.quit()
                    #quit()

            #pygame.display.update()
            #clock.tick(120)