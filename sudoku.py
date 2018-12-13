import random


def cross(A,B):
    #cross product function, used to get every cell in sudoku board (a1, a2, ...)
    return [a+b for a in A for b in B]


def assign_val(value, cell):
    grid_vals[cell] = value
    neighbors = []
    for n in related_cells[cell]:
        for i in range(0,9):
            neighbors.append(n[i])

    neighbors = sorted(set(neighbors))
    #print(cell,neighbors)
    for n in neighbors:
        #print(n, grid_vals[n], str(value))
        if len(grid_vals[n]) > 1 and value in grid_vals[n] :
            # print(n)
            # print(grid_vals['C5'])
            # print(len(grid_vals[n]))
            print("neighbor",n)
            print("GRID VALS",grid_vals[n])
            #print("VALUE", value)
            grid_vals[n] = grid_vals[n].replace(value,'')
            print("after",grid_vals[n])

        # if n != cell and len(grid_vals[n] == 1 and grid_vals[n][0] == value):
        #     return False


# def assign_val(grid_vals, cell, value):
#     print(value)
#     other_vals = grid_vals[cell].remove(value)
#     if all(eliminate(grid_vals, cell, val_2) for val_2 in other_vals):
#         return grid_vals
#     else:
#         return False
#
#
# def eliminate(grid_vals, cell, val):
#     if val not in grid_vals[cell]:
#         return grid_vals
#     grid_vals[cell] - grid_vals[cell].remove(val)
#
#     if len(grid_vals[cell]) == 0:
#         return False
#
#     elif len(grid_vals[cell]) == 1:
#         val2 = grid_vals[cell]
#         if not all(eliminate(grid_vals, cell2, val2) for cell2 in neighbors[cell]):
#             return False
#
#
#     ######
#     for r in related_cells[cell]:
#         cell_location = [cell for cell in r if val in grid_vals[cell]]
#         if len(cell_location) == 0:
#             return False
#         elif len(cell_location) == 1:
#             if not assign_val(grid_vals, cell_location[0], val):
#                 return False
#     return grid_vals
#

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

neighbors = {}

for cell in cells:
    to_add = []
    for n in related_cells[cell]:
        for c in n:
            if c == cell:
                continue
            else:
                to_add.append(c)

    to_add = sorted(set(to_add))
    neighbors[cell] = to_add





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
    if len(line) != 81:
        continue
    boards.append(line)


num_boards = len(boards)

ind = random.randint(1, num_boards-1)

game_board1 = boards[9]
game_board = '2...8.3...6..7..84.3.5..2.9...1.54.8.........4.27.6...3.1..7.4.72..4..6...4.1...3'
# print(game_board1)
# print(game_board)
#init board with given values
for i in range(81):
    if game_board[i] != '.' and game_board[i] != 0:
        grid_vals[cells[i]] = str(game_board[i])


print(grid_vals)



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

### getting all possible values fo
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
            #print(grid_vals[cell])
        # else:
        #     #print("HELLO")
        #     print("HALDFLDSA",grid_vals[cell], cell)
        #     assign_val(str(grid_vals[cell]), cell)


for cell, poss_vals in grid_vals.items():
    if len(poss_vals) == 1:
        assign_val(poss_vals[0], cell)


# def init_solver(grid_vals):
#     for c, val in grid_vals.items():
#         print(c,val)
#         if val != '.' and not assign_val(grid_vals, c, val):
#             return False
#     return grid_vals
#
# init_solver(grid_vals)


#getting most constrained variables -> choose a random one from here to solve
# min_len = float('inf')
# most_constrained = []
# for key, val in grid_vals.items():
#     if len(val) < min_len and len(val) != 1:
#         most_constrained = []
#         min_len = len(val)
#         most_constrained.append(key)
#     elif len(val) == min_len:
#         most_constrained.append(key)
# print("MC", most_constrained)
# #print(most_constrained)
# if len(most_constrained) == 1:
#     assign_val(grid_vals[most_constrained[0]], most_constrained[0], grid_vals, related_cells)
# else:
#     i = random.randint(0,len(most_constrained)-1)
#     #print(most_constrained[i])
#     #print(grid_vals[most_constrained[i]])
#     #display_grid(grid_vals)
#     print(most_constrained[i])
#     possible = grid_vals[most_constrained[i]]
#     choice_ind = random.randint(0,len(possible)-1)
#     assignment = grid_vals[most_constrained[i]][choice_ind]
#     print(assignment)






#assign_val(assignment, most_constrained[i], grid_vals, related_cells)
# copy = grid_vals.copy()
# display_grid(copy)


for row in rows:
    seen = {}
    for r in row:
        if len(grid_vals[r]) > 1:
            for val in grid_vals[r]:
                if val not in seen:
                    seen[val] = [1, r]
                else:
                    seen[val][0] = seen[val][0] + 1
                    seen[val].append(r)
    for key, val in seen.items():
        if val[0] == 1:
            #print(grid_vals[val[1]])
            assign_val(key, val[1])

print("COL")
for col in cols:
    seen = {}
    for c in col:
        if len(grid_vals[c]) > 1:
            for val in grid_vals[c]:
                if val not in seen:
                    seen[val] = [1, c]
                else:
                    seen[val][0] = seen[val][0] + 1
                    seen[val].append(c)
    for key, val in seen.items():
        if val[0] == 1:
            print(grid_vals[val[1]])
            print(key,val)

            assign_val(key, val[1])


# for row in rows:
#     seen = {}
#     for r in row:
#         if r == "C3":
#             print("ROW")
#         if len(grid_vals[r]) > 1:
#             for val in grid_vals[r]:
#                 if val not in seen:
#                     seen[val] = [1, r]
#                 else:
#                     seen[val][0] = seen[val][0] + 1
#                     seen[val].append(r)
#     for key, val in seen.items():
#         if val[0] == 1:
#             print(key,val)
#             #print(grid_vals[val[1]])
#             assign_val(key, val[1])
# #
# # for col in cols:
# #     seen = {}
# #     for c in col:
# #         if len(grid_vals[c]) > 1:
# #             for val in grid_vals[c]:
# #                 if val not in seen:
# #                     seen[val] = [1, c]
# #                 else:
# #                     seen[val][0] = seen[val][0] + 1
# #                     seen[val].append(c)
# #     for key, val in seen.items():
# #         if val[0] == 1:
# #             print(grid_vals[val[1]])
# #             print(key,val)
# #
# #             assign_val(key, val[1])
# # print(grid_vals)
# #
# for quad in quads:
#     seen = {}
#     for q in quad:
#         #print(q)
#         #print(grid_vals['A8'])
#         if len(grid_vals[q]) > 1:
#             for val in grid_vals[q]:
#                 #print(seen)
#                 if val not in seen:
#                     seen[val] = [1, q]
#                 else:
#                     seen[val][0] = seen[val][0] + 1
#                     seen[val].append(q)
#     for key, val in seen.items():
#         if val[0] == 1:
#             #print(key,val)
#             #print(grid_vals[val[1]])
#             assign_val(key, val[1])
#
# # for cell, poss_vals in grid_vals.items():
# #     if len(poss_vals) == 1:
# #         assign_val(poss_vals[0], cell)
#
# print('here',grid_vals)
# # for row in rows:
# #     seen = {}
# #     for r in row:
# #         if len(grid_vals[r]) > 1:
# #             for val in grid_vals[r]:
# #                 if val not in seen:
# #                     seen[val] = [1, r]
# #                 else:
# #                     seen[val][0] = seen[val][0] + 1
# #                     seen[val].append(r)
# #     for key, val in seen.items():
# #         if val[0] == 1:
# #             print(grid_vals[val[1]])
# #             print(key,val)
# #
# #             assign_val(key, val[1])
# print(grid_vals)
# copy = grid_vals.copy()
# display_grid(copy)

# def elim(grid_vals, cell, val):
#     for r in related_cells[cell]:
#         digits = [cell for cell in r if val in grid_vals[cell]]
#         if len(digits) == 0:
#             return False
#         elif len(digits) == 1:
#             assign_val(val, cell)
#     return grid_vals
#
#
# for cell in cells:
#     for v in grid_vals[cell]:
#         elim(grid_vals, cell, v)
#
display_grid(grid_vals)