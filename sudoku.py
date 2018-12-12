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
    if len(line) != 81:
        continue
    boards.append(line)


num_boards = len(boards)

ind = random.randint(1, num_boards-1)

game_board = boards[ind]


#init board with given values
for i in range(81):
    if game_board[i] != '.' and game_board[i] != 0:
        grid_vals[cells[i]] = game_board[i]


def display_grid(grid):
    """
    Displays a 9x9 soduku grid in a nicely formatted way.
    Args:
        grid (str|dict|list): A string representing a Sudoku grid. Valid characters are digits from 1-9 and empty squares are
            specified by 0 or . only. Any other characters are ignored. A `ValueError` will be raised if the input does
            not specify exactly 81 valid grid positions.
            Can accept a dictionary where each key is the position on the board from A1 to I9.
            Can accept a list of strings or integers with empty squares represented by 0.
        coords (bool): Optionally prints the coordinate labels.
    Returns:
        str: Formatted depiction of a 9x9 soduku grid.
    """
    if grid is None or grid is False:
        return None
    all_rows = 'ABCDEFGHI'
    all_cols = '123456789'
    #width = max([3, max([len(grid[pos]) for pos in grid]) + 1])
    width = 3
    display = ''
    row_counter = 0
    col_counter = 0
    for row in all_rows:
        row_counter += 1
        for col in all_cols:
            col_counter += 1
            #if grid[row + col] in null_chars:
            if len(grid[row+col]) == 0 or len(grid[row+col]) > 1:
                grid[row + col] = '.'
            display += ('%s' % grid[row + col]).center(width)
            if col_counter % 3 == 0 and col_counter % 9 != 0:
                display += '|'
            if col_counter % 9 == 0:
                display += '\n'
        if row_counter % 3 == 0 and row_counter != 9:
            display += '+'.join([''.join(['-' for x in range(width * 3)]) for y in range(3)]) + '\n'
    print(display)
    return display

display_grid(grid_vals)
### getting all possible values for each cell
for cell in cells:
    possible_vals = [1,2,3,4,5,6,7,8,9]
    connected_cells = []
    neighbors = related_cells[cell]
    #narrow down what cells we are dealing with here (removing repeats)
    for n in neighbors:
        for i in range(0,9):
            connected_cells.append(n[i])
    connected_cells = sorted(set(connected_cells))
    taken = []
    #print(connected_cells)
    for ind in connected_cells:
        #print(type(grid_vals[ind]))
        #if length is 1, this means that value has been assigned already
        if len(grid_vals[ind]) == 1 and grid_vals[ind] != '.':
            assigned_val = int(grid_vals[ind][0])
            taken.append(assigned_val)
    if grid_vals[cell] == '.' :
        possible_vals = sorted(list(set(possible_vals) - set(taken)))
        #possibility that there is only one value possible for the cell, if so, go ahead and assign it now
        if len(possible_vals) > 1:
            grid_vals[cell] = possible_vals
        else:
            grid_vals[cell] = str(possible_vals)





#getting most constrained variables -> choose a random one from here to solve
min_len = float('inf')
most_constrained = []
for key, val in grid_vals.items():
    if len(val) < min_len and len(val) != 1:
        most_constrained = []
        min_len = len(val)
        most_constrained.append(key)
    elif len(val) == min_len:
        most_constrained.append(key)

print(most_constrained)
print(len(most_constrained))

val_ind = random.randint(0,len(most_constrained)-1)
print(most_constrained[val_ind])
possible = grid_vals[most_constrained[val_ind]]
choice_ind = random.randint(0,len(possible)-1)
assignment = grid_vals[most_constrained[val_ind]][choice_ind]
print(assignment)
#display_grid(grid_vals)
grid_vals[most_constrained[val_ind]] = str(assignment)
#grid_vals[most_constrained[val_ind]].append(str(assignment))
display_grid(grid_vals)
#print(grid_vals)
