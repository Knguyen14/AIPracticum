import random


def cross(A,B):
    #cross product function, used to get every cell in sudoku board (a1, a2, ...)
    return [a+b for a in A for b in B]
    

col_labels = '123456789'
row_labels = 'ABCDEFGHI'

cells = cross(row_labels,col_labels)

# unitlist = ([cross(row_labels, c) for c in col_labels] +
#             [cross(r, col_labels) for r in row_labels] +
#             [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])
            
            
cols = [cross(row_labels, c) for c in col_labels]
rows = [cross(row, col_labels) for row in row_labels]
quads = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]

related_cells = {}
for cell in cells:
    related_cells[cell] = []

for cell in cells:
    for i in range(0,9):
        if cell in cols[i]:
            related_cells[cell].append(cols[i])
        if cell in rows[i]:
            related_cells[cell].append(rows[i])
        if cell in quads[i]:
            related_cells[cell].append(quads[i])



#set up dict to store gameboard values
grid_vals = {}
for cell in cells:
    grid_vals[cell] = []

#Initialize game board that is going to be used

boards = []
file = open("games.txt", "r")
for line in file:
    #boards.append(line)
    line = str(line)
    line = line.strip()
    boards.append(line)

num_boards = len(boards)

ind = random.randint(1, num_boards-1)

game_board = boards[ind]


#init board with given values
for i in range(81):
    if game_board[i] != '.':
        grid_vals[cells[i]] = game_board[i]



# #function to print the board
# def print_board(board):
#     #put board into 9 arrays
#     row1 = []
#     row2 = []
#     row3 = []
#     row4 = []
#     row5 = []
#     row6 = []
#     row7 = []
#     row8 = []
#     row9 = []
#     for i in range(0,81):
#         if i in range(0,9):
#             row1.append(board[i])
#         elif i in range(9,18):
#             row2.append(board[i])
#         elif i in range(18,27):
#             row3.append(board[i])
#         elif i in range(36,45):
#             row4.append(board[i])
#         elif i in range(45,54):
#             row5.append(board[i])
#         elif i in range(54,63):
#             row6.append(board[i])
#         elif i in range(63,72):
#             row7.append(board[i])
#         elif i in range(72,81):
#             row8.append(board[i])
#     print(row1,'\n', row2, '\n', row3)



def display(values):
    "Display these values as a 2-D grid."
    width = 1+max(len(values[s]) for s in cells)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print (''.join(values[r+c].center(width)+('|' if c in '36' else ''))
                      for c in cols)
        if r in 'CF': print (line)
    #print

display(game_board)
