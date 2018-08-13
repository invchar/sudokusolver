#!/usr/bin/env python3

# row of placeholders
#pRow = ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p']

# puzzle grid with placeholders
#puzzle = [pRow, pRow, pRow, pRow, pRow, pRow, pRow, pRow, pRow]

#puzzle = [
#	['1', '2', '3', '4', '5', 'p', 'p', 'p', 'p'],
#	['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
#	['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
#	['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
#	['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
#	['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
#	['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
#	['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
#	['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
#]

#for x in range(9):
#	print(puzzle[x])

#for y in range(9):
#	for x in range(9):
#		print(str(x) + ',' + str(y) + '=' + puzzle[y][x])

# solution for below puzzle
# 7 9 3 4 5 8 2 6 1
# 8 6 5 1 3 2 4 7 9
# 4 2 1 6 9 7 5 3 8
# 6 4 9 3 7 1 8 5 2
# 2 5 8 9 4 6 7 1 3
# 1 3 7 2 8 5 9 4 6
# 9 7 4 8 6 3 1 2 5
# 5 1 6 7 2 9 3 8 4
# 3 8 2 5 1 4 6 9 7

puzzle = [
	['7', '9', ' ', '4', '5', ' ', '2', '6', ' '],
	[' ', '6', '5', ' ', ' ', ' ', '4', ' ', ' '],
	[' ', ' ', '1', ' ', '9', '7', ' ', ' ', '8'],
	[' ', ' ', '9', ' ', '7', '1', ' ', '5', ' '],
	[' ', ' ', ' ', '9', '4', '6', ' ', '1', ' '],
	['1', ' ', '7', '2', ' ', ' ', '9', ' ', ' '],
	['9', '7', '4', '8', '6', ' ', '1', '2', '5'],
	['5', ' ', ' ', '7', ' ', ' ', '3', '8', '4'],
	[' ', '8', '2', ' ', '1', '4', '6', '9', ' '],
]
# adding some numbers to test completecolumn
puzzle = [
	['7', '9', ' ', '4', '5', ' ', '2', '6', ' '],
	[' ', '6', '5', ' ', '3', ' ', '4', ' ', ' '],
	[' ', ' ', '1', ' ', '9', '7', ' ', ' ', '8'],
	[' ', ' ', '9', ' ', '7', '1', ' ', '5', ' '],
	[' ', ' ', ' ', '9', '4', '6', ' ', '1', ' '],
	['1', ' ', '7', '2', '8', ' ', '9', ' ', ' '],
	['9', '7', '4', '8', '6', ' ', '1', '2', '5'],
	['5', ' ', ' ', '7', ' ', ' ', '3', '8', '4'],
	[' ', '8', '2', ' ', '1', '4', '6', '9', ' '],
]

def printcoords(puzzle):
	for y in range(9): # rows loop
		for x in range(9): # columns loop
			print(str(x) + ',' + str(y) + '=' + puzzle[y][x]) # print x and y coords and value


def printpuzzle(puzzle):
	print('+-----+-----+-----+') # top x axis border
	for y in range(9):  # rows loop
		line = '|' # far-left y axis border
		for x in range(9): # columns loop
			if (x == 2 or x == 5 or x == 8): # if we need a right-side border
				line = line + puzzle[y][x] + '|' # print value with right-side border
			else:
				line = line + puzzle[y][x] + ' ' # print value without right-side border
		print(line) # print the line created in columns loop
		if (y == 2 or y == 5 or y == 8): # if we need x axis border
			print('+-----+-----+-----+') # x axis border
print('Original puzzle:')
printpuzzle(puzzle)
#printcoords(puzzle)

# if the number of blanks in a row is 1, subtract the sum of the numbers in the row from 45, and that is the number for the blank
def completerow():
	for y in range(9): # rows loop
		blanks = 0 # counter for blanks
		total = 0 # to be the sum of the numbers already in the row
		for x in range(9): # columns loop
			if (puzzle[y][x] == ' '): # if it's a blank
				blanks = blanks + 1 # counting the blank spaces in the row
				locationy = y # remember y axis
				locationx = x # remember x axis
			else: # if it isn't blank add the value to the total
				total = total + int(puzzle[y][x]) # if we can change it to an int, add it to the total
		if (blanks == 1): # if there is only one blank, we can know the value of it
			puzzle[locationy][locationx] = str(45 - total) # set the value of the single blank on the row
			printpuzzle(puzzle) # unneeded printing, unless we want to watch as the puzzle is filled out
			return True
	return False

# if the number of blanks in a column is 1, subtract the sum of the numbers in the column from 45, and that is the number for the blank

def completecolumn():
	for x in range(9): # outer loop
		blanks = 0 # counter for blanks
		total = 0 # to be the sum of the numbers already in the column
		for y in range(9): # inner loop
			if (puzzle[y][x] == ' '): # if it's a blank
				blanks = blanks + 1 # counting the blank spaces in the column
				locationy = y # remember y axis of last known blank
				locationx = x # remember x axis of last known blank
			else: # if it isn't blank
				total = total + int(puzzle[y][x])
		if (blanks == 1): # if there is only one blank, we can know the value of it
			puzzle[locationy][locationx] = str(45 - total)
			printpuzzle(puzzle)
			return True
	return False

def completeblock():
	i = 0
	while (i < 7):
		j = 0
		while (j < 7):
			y = i
			blanks = 0
			total = 0
			while (y < (i + 3)):
				x = j
				while (x < (j + 3)):
					if (puzzle[y][x] == ' '): # if it's a blank
						blanks = blanks + 1 # counting the blank spaces
						locationy = y # remember y axis of last known blank
						locationx = x # remember x axis of last known blank
					else: # if it isn't blank
						total = total + int(puzzle[y][x])
					x = x + 1
				y = y + 1
			if (blanks == 1):
				puzzle[locationy][locationx] = str(45 - total)
				printpuzzle(puzzle)
				return True
			j = j + 3
		i = i + 3
	return False

while True:
	if (completerow()):
		continue
	if (completecolumn()):
		continue
	if (completeblock()):
		continue
	break
