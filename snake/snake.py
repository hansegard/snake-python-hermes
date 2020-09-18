import pygame
import random
import time


class PySnake:
    _screen = None
    _min_color_value = 0
    _max_color_value = 255
    black = (_min_color_value, _min_color_value, _min_color_value)
    white = (_max_color_value, _max_color_value, _max_color_value)
    red = (_max_color_value, _min_color_value, _min_color_value)
    display_width = 800
    display_height = 600
    clock = pygame.time.Clock()

    def init(self):
        self._setup_screen()

    def run(self):
        print('To exit, press the exit button')
        should_exit = False
        while not should_exit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    should_exit = True
                self._screen.fill(self._get_new_random_rbg_color())
                pygame.display.update()

    def _setup_screen(self):
        self._screen = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption('SNEK')
        self._screen.fill(self.black)
        self.message_display("Welcome to SNEK", 75, 4, (self.display_width / 2), (self.display_height / 2.5))
        self.message_display("Epilepsy warning!", 75, 4, (self.display_width / 2), (self.display_height / 2))
        self.clock.tick(5)

    def _get_new_random_rbg_color(self):
        return random.randint(self._min_color_value, self._max_color_value),\
               random.randint(self._min_color_value, self._max_color_value), \
               random.randint(self._min_color_value, self._max_color_value)

    def text_objects(self, text, font, color):
        text_surface = font.render(text, True, color)
        return text_surface, text_surface.get_rect()

    def message_display(self, text, font_size, duration, x_position, y_position):
        if not pygame.font.get_init():
            pygame.font.init()
        font = pygame.font.SysFont('freesansbold.ttf', font_size)
        text_surf, text_rect = self.text_objects(text, font, self.white)
        text_rect.center = (x_position, y_position)
        self._screen.blit(text_surf, text_rect)

        pygame.display.update()

        time.sleep(duration)
