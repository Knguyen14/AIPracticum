import random


def cross(A,B):
    #cross product function, used to get every cell in sudoku board (a1, a2, ...)
    return [a+b for a in A for b in B]


def assign_val(value, cell):
    grid_vals[cell] = value
    update(grid_vals)
    
def update(grid_vals):
    for cell in cells:
        for n in peers[cell]:
            if(len(grid_vals[cell]) == 1) and grid_vals[cell] in grid_vals[n] and len(grid_vals[n]) != 1:
                grid_vals[n] = grid_vals[n].replace(grid_vals[cell],'')




col_labels = '123456789'
row_labels = 'ABCDEFGHI'

cells = cross(row_labels,col_labels)

            
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


peers = {}

for cell in cells:
    to_add = []
    for n in related_cells[cell]:
        for c in n:
            if c == cell:
                continue
            else:
                to_add.append(c)

    to_add = sorted(set(to_add))
    peers[cell] = to_add







#set up dict to store gameboard values
grid_vals = {}
for cell in cells:
    grid_vals[cell] = ''

#Initialize game board that is going to be used

boards = []
file = open("games.txt", "r")
for line in file:
    #boards.append(line)
    line = str(line)
    line = line.strip()
    if len(line) == 81:
        boards.append(line)

#print(len(boards))
num_boards = len(boards)
# print(num_boards)

ind = random.randint(1, num_boards-1)
print(ind)
game_board = boards[31] 
#game_board = '2...8.3...6..7..84.3.5..2.9...1.54.8.........4.27.6...3.1..7.4.72..4..6...4.1...3'
#game_board = '.4.....5...19436....9...3..6...5...21.3...5.68...2...7..5...2....24367...3.....4.'

#init board with given values
for i in range(81):
    if game_board[i] != '.' and game_board[i] != 0:
        grid_vals[cells[i]] = str(game_board[i])


# print(grid_vals)



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
    #show_grid = grid.copy()
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

### getting all possible values for
for cell in cells:
    possible_vals = ['1','2','3','4','5','6','7','8','9']
    connected_cells = []
    neighbors = related_cells[cell]
    #narrow dor each cellwn what cells we are dealing with here (removing repeats)
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
            assigned_val = str(grid_vals[ind][0])
            taken.append(assigned_val)
    if grid_vals[cell] == '.' or grid_vals[cell] == [] :
        possible_vals = sorted(list(set(possible_vals) - set(taken)))
        #possibility that there is only one value possible for the cell, if so, go ahead and assign it now
        if len(possible_vals) != 0:
            st = ''
            for i in possible_vals:
                st += i
            grid_vals[cell] = st



for cell, poss_vals in grid_vals.items():
    if len(poss_vals) == 1:
        assign_val(poss_vals[0], cell)

# for row in rows:
#     seen = {}
#     for r in row:
#         if len(grid_vals[r]) > 1:
#             for val in grid_vals[r]:
#                 if val not in seen:
#                     seen[val] = [1, r]
#                 else:
#                     seen[val][0] = seen[val][0] + 1
#                     seen[val].append(r)
#     for key, val1 in seen.items():
#         if val1[0] == 1:
#             assign_val(key, val1[1])

# for col in cols:
#     seen = {}
#     for c in col:
#         if len(grid_vals[c]) > 1:
#             for val in grid_vals[c]:
#                 if val not in seen:
#                     seen[val] = [1, c]
#                 else:
#                     seen[val][0] = seen[val][0] + 1
#                     seen[val].append(c)
#     for key, val in seen.items():
#         if val[0] == 1:
#             assign_val(key, val[1])

# for quad in quads:
#     seen = {}
#     for q in quads:
#         if len(grid_vals[c]) > 1:
#             for val in grid_vals[q]:
#                 if val not in seen:
#                     seen[val] = [1, q]
#                 else:
#                     seen[val][0] = seen[val][0] + 1
#                     seen[val].append(q)
#     for key, val in seen.items():
#         if val[0] == 1:
#             assign_val(key, val[1])

for cell in cells:
    seen = {}
    for units in related_cells[cell]:
        for k in units:
            if len(grid_vals[k]) > 1:
                for val in grid_vals[k]:
                    if val not in seen:
                        seen[val] = [1, k]
                    else:
                        seen[val][0] = seen[val][0] + 1
                        seen[val].append(k)
    for key, val in seen.items():
        if val[0] == 1:
            assign_val(key, val[1])
update(grid_vals)

display_grid(grid_vals)
