import pygame
import random
from pygame.locals import *

class GameOfLife:
    def __init____(self, width = 640, height = 480, cell_size = 10, speed = 10):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.screen_size = width, height

        self.screen = pygame.display.set_mode(self.screen_size)
        self.speed = speed 

    def draw_grid(self):
        # http://www.pygame.org/docs/ref/draw.html#pygame.draw.line
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), 
                (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), 
                (0, y), (self.width, y))


    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.draw_grid()
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()
    
    
    def cell_list(self, randomize=False):
        cols = self.cell_width    
        rows = self.cell_height   

        if not randomize:
            
            grid = [[0 for _ in range(cols)] for _ in range(rows)]
        else:
            
             grid = [[random.randint(0, 1) for _ in range(cols)]
                for _ in range(rows)]

        return grid




if __name__ == '__main__':
    game = GameOfLife(320, 240, 20)
    game.run()


