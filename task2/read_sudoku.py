import os

def read_sudoku(filename):
    current_dir = os.path.dirname(__file__)  
    filepath = os.path.join(current_dir, filename)

    with open(filepath, 'r', encoding='utf-8') as file:
        lines = [c for c in open(filename).read() if c in '123456789.']
    return lines

grid = read_sudoku('sudoku.txt')


def group(values, n):
    return [values[i:i+n] for i in range(0, len(values), n)]


def get_row(grid, pos):
    return grid[pos[0]]

def get_col(grid, pos):
    col = []
    for i in range(len(grid)):
        col.append(grid[i][pos[1]])
    return col

def get_block(grid, pos):
    row_start = (pos[0] // 3) * 3
    col_start = (pos[1] // 3) * 3
    block = []
    for i in range(row_start, row_start + 3):     
        for k in range(col_start, col_start + 3):  
            block.append(grid[i][k])
    return block

def find_empty_positions(grid):
    for i in range(len(grid)):
        for k in range(len(grid[i])):
            if grid[i][k] =='.':
                return (i, k)
    
    return None
                
                
            
        

        