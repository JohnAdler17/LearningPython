matrix = [[1, 3, 5], [2, 4, 6], [3, 6, 9]]
matrix2 = [[5, 2, 8, 4], [-9, 0, 4, 1], [5, 6, 4, 8]]

def add_diagonal(grid):
    total = 0
    for i in range(len(grid)):
        total += grid[i][i]
    return total

def mult5(grid):
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] % 2 == 0:
                grid[r][c] *= 5
    return grid

def mult2even(grid):
    for r in range(len(grid)):
        if (r % 2 == 0):
            

            
