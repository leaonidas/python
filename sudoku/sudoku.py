#Sudoku Solver
#Uses Backtracking algorithm

def solver(puzzle):
	num = 1
	row, col = findEmpty(puzzle)
	if row == -1 or col == -1:
		return True

	for num in range(1, 10):
		if checkRow(puzzle, row, num) and checkCol(puzzle, col, num) and checkBox(puzzle, row, col, num):
			puzzle[row][col]=num
			if solver(puzzle):
				return True
			puzzle[row][col] = 0
	
	return False


def findEmpty(puzzle):
	for row in range(9):
		for col in range(9):
			if puzzle[row][col]==0:
				return row, col
	return -1, -1

def checkRow(puzzle, row, num):
	for col in range(9):
		if num == puzzle[row][col]:
			return False
	return True

def checkCol(puzzle, col, num):
	for row in range(9):
		if num == puzzle[row][col]:
			return False
	return True

def checkBox(puzzle, row, col, num):
	rowZone = row // 3
	colZone = col // 3
	for r in range(rowZone*3, rowZone*3 + 3):
		for c in range(colZone*3, colZone*3 + 3):
			if num == puzzle[r][c]:
				return False
	return True

def printSudoku(puzzle):
	for i in range(len(puzzle)):
		if i % 3 == 0 and i != 0:
			print("- - - - - - - - - - - - - ")
		for j in range(len(puzzle[0])):
			if j % 3 == 0 and j != 0:
				print(" | ", end="")
			if j == 8:
				print(puzzle[i][j])
			else:
				print(str(puzzle[i][j]) + " ", end="")

###############################
puzzle = [
	[7, 8, 0, 4, 0, 0, 1, 2, 0],
	[6, 0, 0, 0, 7, 5, 0, 0, 9],
	[0, 0, 0, 6, 0, 1, 0, 7, 8],
	[0, 0, 7, 0, 4, 0, 2, 6, 0],
	[0, 0, 1, 0, 5, 0, 9, 3, 0],
	[9, 0, 4, 0, 6, 0, 0, 0, 5],
	[0, 7, 0, 3, 0, 0, 0, 1, 2],
	[1, 2, 0, 0, 0, 7, 4, 0, 0],
	[0, 4, 9, 2, 0, 6, 0, 0, 7]
]
if not solver(puzzle):
	print("No solution found!")
printSudoku(puzzle)