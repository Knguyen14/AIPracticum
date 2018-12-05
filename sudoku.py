#initialize board 
sample_board = [[0 for i in range(9)] for j in range(9)]

#prints board in grid form
for x in sample_board:
    print(*x, sep=" ")


def emptySudoku():
    ''' Creates an empty sudoku in row major form. Sets up all of the x, y, and z
        coordinates for the sudoku cells'''
    ans = []
    for x in range(1,10):
        if x in [7,8,9]:
            intz = 7
            z = 7
        if x in [4,5,6]:
            intz = 4
            z = 4
        if x in [1,2,3]:
            intz = 1
            z = 1
        for y in range(1,10):
            z = intz
            if y in [7,8,9]:
                z += 2
            if y in [4,5,6]:
                z += 1
            if y in [1,2,3]:
                z += 0
            c = cell((x,y,z))
            ans.append(c)
    return ans
    
    
print(emptySudoku())
