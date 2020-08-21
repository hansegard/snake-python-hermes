import pygame
import random


class PySnake:
    _screen = None
    _min_color_value = 0
    _max_color_value = 255

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
        self._screen = pygame.display.set_mode((400, 400))
        pygame.display.set_caption('SNEK')

    def _get_new_random_rbg_color(self):
        return random.randint(self._min_color_value, self._max_color_value),\
               random.randint(self._min_color_value, self._max_color_value), \
               random.randint(self._min_color_value, self._max_color_value)
