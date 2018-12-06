import random
#initialize board 


board = [[i for i in range(9)] for j in range(9)]

#prints board in grid form
# for x in board:
#     print(*x, sep=" ")

def getBlocks(board):
    answer = []
    for r in range(3):
        for c in range(3):
            block = []
            for i in range(3):
                for j in range(3):
                    block.append(board[3*r + i][3*c + j])
            answer.append(block)
    return answer


#print(getBlocks(board))

def assign_val(val, x, y,column):
    #print(val, board[x][:], column)
    if val not in board[x][:] and val not in column:
        board[x][y] = num
        return True
    else:
        return False

for ii in range(0,9):
    for jj in range(0,9):
        column = []
        for row in board:
            column.append(row[jj])

        board[ii][jj] = random.randint(0,9)
        #print(row[jj], column)
        #print(board[ii][:])
        # okay = False
        # while not okay:
        #     num = random.randint(1, 10)
        #     if assign_val(num, ii, jj, column) == True:
        #         okay = True


        #if num not in
#prints board in grid form
for x in board:
    print(*x, sep=" ")
