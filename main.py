import time
start = time.time()
def check_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c]==-1:
                return r,c
    return None,None
def is_valid(puzzle,guess,row,col):
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    col_vals = []
    # for i in range(9):
    #     col_val.append(puzzle[i][col])
    '''or'''
    col_vals =[puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    
    row_start = (row//3)*3
    col_start = (col//3)*3
    for r in range(row_start,row_start+3):
        for c in range(col_start,col_start+3):
            if guess==puzzle[r][c]:
                return False
    else:
        return True

def solve(puzzle):
    row,col = check_empty(puzzle)
    if row is None:
        return True
    for guess in range(1,10):
        if is_valid(puzzle,guess,row,col)==True:
            puzzle[row][col]=guess
            if solve(puzzle)==True:
                return True
        puzzle[row][col]=-1 
    return False

example = [
        [-1, 2, -1,   6, -1, -1,   -1, 5, -1],
        [-1, -1, -1,   4, 9, -1,   -1, -1,-1],
        [-1, -1, 6,   -1, 5, 2,   8, -1, -1],

        [-1, -1, 2,   -1,-1, -1,   -1, 3, 1],
        [-1, 9,5,   -1, -1,-1,   2, 7, -1],
        [3, 6, -1,   -1, -1, -1,   9, -1,-1],

        [-1, -1, 4,   9, 3,-1,   5, -1, -1],
        [-1, -1, -1,   -1,6, 5,   -1, -1, -1],
        [-1, 8, -1,   -1, -1, 4,   -1, 9, -1]
    ]

solve(example)
end = time.time()
print(end-start)
for i in range(9):
    print(example[i])

