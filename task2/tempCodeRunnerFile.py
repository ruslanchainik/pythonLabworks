import os

def read_sudoku(filename):
    current_dir = os.path.dirname(__file__)  
    filepath = os.path.join(current_dir, filename)

    with open(filepath, 'r', encoding='utf-8') as file:
        lines = [list(line.strip()) for line in file if line.strip()]
    return lines

grid = read_sudoku('sudoku.txt')
for row in grid:
    print(row)