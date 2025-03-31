import pygame.image
from pygame import Surface, Rect
from pygame.font import Font
from code.const import WIN_WIDTH, WIN_HEIGHT, COLOR_WHITE, MENU_OPTION, COLOR_YELLOW
class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/bg menu.png')
        self.rect = self.surf.get_rect(left=0, top=0)


    def run(self, ):
        pygame.mixer_music.load('./asset/795971__josefpres__piano-loops-185-octave-down-long-loop-120-bpm.wav')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
           # titulo self.menu_text(50,"VAMP", text_color=COLOR_WHITE, text_center_pos=((WIN_WIDTH / 2), 70))

            for i in range(len(MENU_OPTION)):
                self.menu_text(20, MENU_OPTION[i], text_color=COLOR_YELLOW, text_center_pos=((WIN_WIDTH / 2), 270 + 30 * i))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Courier New", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)