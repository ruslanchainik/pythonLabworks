import os

def group(values, n):
    return [values[i:i+n] for i in range(0, len(values), n)]

def read_sudoku(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        digits = [c for c in file.read() if c in '123456789.']
    return group(digits, 9)

grid = read_sudoku('sudoku.txt')





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
                
                
def find_possible_values(grid, pos):
    row = get_row(grid, pos)
    col = get_col(grid, pos)
    block = get_block(grid, pos)
    numbers = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
    possible_values = set()
    for i in range(9):
        if numbers[i] not in row and  numbers[i] not in col and  numbers[i] not in block:
            possible_values.add(numbers[i])
    return possible_values

def solve(grid):
    
    pos = find_empty_positions(grid)
    if pos is None:
        return grid  

    values_for_pos = list(find_possible_values(grid, pos))
    row, col = pos

    for val in values_for_pos:
        grid[row][col] = val
        result = solve(grid)
        if result:
            return result
        
        grid[row][col] = '.'

    return None 


        
def display(grid):
    for i in range(9):
        row = grid[i]
        line = ' '.join(row[0:3]) + ' | ' + ' '.join(row[3:6]) + ' | ' + ' '.join(row[6:9])
        print(line)
        if i in [2, 5]:
            print('------+-------+------')


def check_solution(grid):
    correct_set = set('123456789')

    for i in range(9):
        if set(get_row(grid, (i, 0))) != correct_set:
            return False
        if set(get_col(grid, (0, i))) != correct_set:
            return False

    for block_row in [0, 3, 6]:
        for block_col in [0, 3, 6]:
            if set(get_block(grid, (block_row, block_col))) != correct_set:
                return False

    return True
