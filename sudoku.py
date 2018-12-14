import random
import argparse

parser = argparse.ArgumentParser(description="Run Sudoku solver")
parser.add_argument('--show_init_board', action='store_true')
parser.add_argument('--show_steps', action='store_true')

args = parser.parse_args()


def cross(A, B):
    # cross product function, used to get every cell in sudoku board (a1, a2, ...)
    return [a + b for a in A for b in B]


def assign_val(value, cell):
    grid_vals[cell] = value
    update(grid_vals)


def update(grid_vals):
    for cell in cells:
        for n in peers[cell]:
            if (len(grid_vals[cell]) == 1) and grid_vals[cell] in grid_vals[n] and len(grid_vals[n]) != 1:
                grid_vals[n] = grid_vals[n].replace(grid_vals[cell], '')


def get_poss_vals():
    for cell in cells:
        possible_vals = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        connected_cells = []
        neighbors = related_cells[cell]
        # narrow dor each cellwn what cells we are dealing with here (removing repeats)
        for n in neighbors:
            for i in range(0, 9):
                connected_cells.append(n[i])
        connected_cells = sorted(set(connected_cells))
        taken = []
        # print(connected_cells)
        for ind in connected_cells:
            # print(type(grid_vals[ind]))
            # if length is 1, this means that value has been assigned already
            if len(grid_vals[ind]) == 1 and grid_vals[ind] != '.':
                assigned_val = str(grid_vals[ind][0])
                taken.append(assigned_val)
        if grid_vals[cell] == '.' or grid_vals[cell] == [] or grid_vals[cell] == '':
            possible_vals = sorted(list(set(possible_vals) - set(taken)))
            # possibility that there is only one value possible for the cell, if so, go ahead and assign it now
            if len(possible_vals) != 0:
                st = ''
                for i in possible_vals:
                    st += i
                grid_vals[cell] = st


def solver():
    for cell, poss_vals in grid_vals.items():
        if len(poss_vals) == 1:
            assign_val(poss_vals[0], cell)

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

    def is_complete(grid_vals):
        for cell in cells:
            if len(grid_vals[cell]) > 1:
                return False
        return True

    counter = 0
    game = is_complete(grid_vals)
    while game == False:
        update(grid_vals)
        counter += 1
        if counter > 19:
            break
        game = is_complete(grid_vals)


col_labels = '123456789'
row_labels = 'ABCDEFGHI'

cells = cross(row_labels, col_labels)

cols = [cross(row_labels, c) for c in col_labels]
rows = [cross(row, col_labels) for row in row_labels]
quads = [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')]

related_cells = {}
for cell in cells:
    related_cells[cell] = []

for cell in cells:
    for i in range(0, 9):
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

# set up dict to store gameboard values
grid_vals = {}
for cell in cells:
    grid_vals[cell] = ''

# Initialize game board that is going to be used

boards = []
file = open("games.txt", "r")
for line in file:
    # boards.append(line)
    boards.append(line)

num_boards = len(boards)

ind = random.randint(1, num_boards - 1)

game_board = boards[ind]
# init board with given values
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
    # show_grid = grid.copy()
    if grid is None or grid is False:
        return None
    all_rows = 'ABCDEFGHI'
    all_cols = '123456789'
    width = max([3, max([len(grid[pos]) for pos in grid]) + 1])
    width = 3
    display = ''
    row_counter = 0
    col_counter = 0
    for row in all_rows:
        row_counter += 1
        for col in all_cols:
            col_counter += 1
            # if grid[row + col] in null_chars:
            if len(grid[row + col]) == 0 or len(grid[row + col]) > 1:
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


#display_grid(grid_vals)
if args.show_init_board:
    print("Starting Board:\n")
    display_grid(grid_vals)

get_poss_vals()
solver()
if args.show_init_board:
    print("Solution:\n")
display_grid(grid_vals)
