import os

def read_sudoku(filename):
    current_dir = os.path.dirname(__file__)  
    filepath = os.path.join(current_dir, filename)

    with open(filepath, 'r', encoding='utf-8') as file:
        lines = [c for c in open(filename).read() if c in '123456789.']
    return lines

grid = read_sudoku('sudoku.txt')
print(grid)