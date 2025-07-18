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
            self.cell_list()
            self.draw_cell_list(grid)
            grid = self.update_cell_list(grid)
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
    
    def draw_cell_list(self, rects):
        for row in range(self.cell_height):
            for col in range(self.cell_width):
                color = pygame.Color('green') if rects[row][col] else pygame.Color('white')
                rect = (
                    col * self.cell_size,
                     row * self.cell_size,
                    self.cell_size,
                    self.cell_size
                        )
                pygame.draw.rect(self.screen, color, rect)

    def get_neighbours(self, cell):
        neighbours = []
        row, col = cell[0], cell[1]
        for i in range(3):
            if 0 <= row - 1 + i < self.cell_height:
                for k in range(3):
                    if 0 <= col-1 + k < self.cell_width and ((i, k) != (1, 1)):
                        neighbours.append((row - 1 + i, col-1 + k))

        return neighbours
    
    def update_cell_list(self, cell_list):
        rows = len(cell_list)
        cols = len(cell_list[0])
        new_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(len(cell_list)):
            for k in range(len(cell_list[i])):
                count = 0
                sosedi = self.get_neighbours((i, k))
                for z in range(len(sosedi)):
                    if cell_list[sosedi[z][0]][sosedi[z][1]] == 1:
                        count +=1
                if (cell_list[i][k] == 1 and (count == 3 or count == 2)) or (cell_list[i][k] == 0 and (count == 3)):
                    new_matrix[i][k] = 1

        return new_matrix




if __name__ == '__main__':
    game = GameOfLife(320, 240, 20)
    game.run()


