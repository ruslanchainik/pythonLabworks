import pygame
from pygame.locals import *

class GameOfLife:
    def __init____(self, width = 640, height = 480, cell_size = 10, speed = 10):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.screen_size = width, height

        self.screen = pygame.display.set_mode(self.screen_size)