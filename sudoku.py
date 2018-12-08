import random

"""Gets a tuple of reference objects that are useful for describing the Sudoku grid."""
def cross(str_a, str_b):
    """Cross product (concatenation) of two strings A and B."""
    return [a + b for a in str_a for b in str_b]

all_rows = 'ABCDEFGHI'
all_cols = '123456789'
rows = {'A': [], 'B':[], 'C':[], 'D':[], 'E':[], 'F':[], 'G':[], 'H':[], 'I':[]}
cols = {'1':[], '2':[], '3':[], '4':[], '5':[], '6':[], '7':[], '8':[],'9':[]}

# Build up list of all cell positions on the grid
cells = cross(all_rows, all_cols)
values = {}
for cell in cells:
	values[cell] = 0
    
#~ for cell in cells:
	#~ row = cell[0]
	#~ column = cell[1]
	#~ #want to check row
	#~ good = False
	#~ while good == False:
		#~ num = str(random.randint(1,9))
		#~ if num not in rows[row] and num not in cols[column]:
			#~ good = True
			#~ values[cell] = str(num)
			#~ rows[row].append(num)
			#~ cols[column].append(num)
			#~ print(rows, cols)
			
	




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
    
def sudoku(size):
	import time
	start_time=time.time()

	import sys
	import random as rn
	mydict = {}
	n = 0
	print ('--started calculating--')
	while len(mydict) < 9:
		n += 1
		x = range(1, size+1)
		testlist = rn.sample(x, len(x))

		isgood = True
		for dictid,savedlist in mydict.items():
			if isgood == False:
				break
			for v in savedlist:
				if testlist[savedlist.index(v)] == v:
					isgood = False
					break

		if isgood == True:
			isgoodafterduplicatecheck = True
			mod = len(mydict) % 3
			dsavedlists = {}
			dtestlists = {}
			dcombindedlists = {}
			for a in range(1,mod + 1):
				savedlist = mydict[len(mydict) - a]               
				for v1 in savedlist:
					modsavedlists = (savedlist.index(v1) / 3) % 3
					dsavedlists[len(dsavedlists)] = [modsavedlists,v1]
				for t1 in testlist:
					modtestlists = (testlist.index(t1) / 3) % 3
					dtestlists[len(dtestlists)] = [modtestlists,t1]
				for k,v2 in dsavedlists.items():
					dcombindedlists[len(dcombindedlists)] = v2
					dcombindedlists[len(dcombindedlists)] = dtestlists[k]
			vsave = 0
			lst1 = []
			for k, vx in dcombindedlists.items():
				vnew = vx[0]
				if not vnew == vsave:
					lst1 = []
					lst1.append(vx[1])
				else:
					if vx[1] in lst1:
						isgoodafterduplicatecheck = False
						break
					else:
						lst1.append(vx[1])
				vsave = vnew

			if isgoodafterduplicatecheck == True:

				mydict[len(mydict)] = testlist
				print('success found', len(mydict), 'row')   

	print ('--finished calculating--')
	total_time = time.time()-start_time
	return mydict, n, total_time

return_dict, total_tries, amt_of_time = sudoku(9)
print ('')
print ('--printing output--')
for n,v in return_dict.items():
	print (n,v)
print ('process took',total_tries,'tries in', round(amt_of_time,2), 'secs')
print ('-------------------')

#~ cell_index = 0
#~ for entry in return_dict:
	#~ for ind in range(len(return_dict[entry])):
		#~ values[cells[cell_index]] = str(return_dict[entry][ind])
			
#~ display_grid(values)



