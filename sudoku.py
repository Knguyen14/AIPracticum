import random

"""Gets a tuple of reference objects that are useful for describing the Sudoku grid."""
def cross(str_a, str_b):
    """Cross product (concatenation) of two strings A and B."""
    return [a + b for a in str_a for b in str_b]

all_rows = 'ABCDEFGHI'
all_cols = '123456789'

# Build up list of all cell positions on the grid
cells = cross(all_rows, all_cols)
values = {}
for cell in cells:
    values[cell] = 0
    
for cell in cells:
    row = cell[0]
    column = cell[1]
    
    #print(row, column)
    values[cell] = str(random.randint(1,9))
    


def display_grid(grid, coords=False):
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
	null_chars = '0.'

	if type(grid) == str:
		grid = parse_puzzle(grid)
	elif type(grid) == list:
		grid = parse_puzzle(''.join([str(el) for el in grid]))

	width = max([3, max([len(grid[pos]) for pos in grid]) + 1])
	display = ''

	if coords:
		display += '   ' + ''.join([all_cols[i].center(width) for i in range(3)]) + '|'
		display += ''.join([all_cols[i].center(width) for i in range(3, 6)]) + '|'
		display += ''.join([all_cols[i].center(width) for i in range(6, 9)]) + '\n   '
		display += '--' + ''.join(['-' for x in range(width * 9)]) + '\n'

	row_counter = 0
	col_counter = 0
	for row in all_rows:
		if coords:
			display += all_rows[row_counter] + ' |'
		row_counter += 1
		for col in all_cols:
			col_counter += 1
			if grid[row + col] in null_chars:
				grid[row + col] = '.'

			display += ('%s' % grid[row + col]).center(width)
			if col_counter % 3 == 0 and col_counter % 9 != 0:
				display += '|'
			if col_counter % 9 == 0:
				display += '\n'
		if row_counter % 3 == 0 and row_counter != 9:
			if coords:
				display += '  |'
			display += '+'.join([''.join(['-' for x in range(width * 3)]) for y in range(3)]) + '\n'

	print(display)
	return display
    
display_grid(values)
