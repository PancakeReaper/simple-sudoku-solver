import tkinter as tk 
import time

window = tk.Tk()

mainFrame = tk.Frame(window)

board = []
numbers = []

# Automatically generate the empty sudoku board
for row in range(9):
	board.append([])
	numbers.append([])
	for col in range(9):
		board[row].append(tk.Entry(window, width=3, justify='center'))
		board[row][col].grid(row=row, column=col)
		numbers[row].append(0)
			
# Solve Button
solveButton = tk.Button(window, text=" Solve! ")
solveButton.grid(row=10, column=1, columnspan=3, pady=2)

# Clear Button
clearButton = tk.Button(window, text=" Clear! ")
clearButton.grid(row=10, column=5, columnspan=3, pady=2)

## Returns first empty space on the board ##
def findEmpty(board):
	for row in range(9):
		for col in range(9):
			if board[row][col] == 0:
				return [row, col]
	return None

## Returns True if valid, else False ##
def checkValid(board, row, col):
	number = board[row][col]
	# Check if the same number exists in the same row or col
	for i in range(9):
		if i != row and board[i][col] == number:
			return False
		if i != col and board[row][i] == number:
			return False
	# Check if the same number exists in the same 3x3 box
	b_row = row
	b_col = col
	while not (b_row == 0 or b_row == 3 or b_row == 6):
		b_row -= 1
	while not (b_col == 0 or b_col == 3 or b_col == 6):
		b_col -= 1
	for x in range(3):
		for y in range(3):
			if b_row + y != row and b_col + x != col:
				if board[b_row + y][b_col + x] == number:
					return False
	return True

# Check is there any empty spaces
# Try 1 - 9 
# Check if valid
# Recurse and find next empty space
def solve(board):

	empty = findEmpty(board)
	if empty != None:
		row, col = empty
	else:
		return

	for attempt in range(1,10):
		board[row][col] = attempt

		if checkValid(board, row, col):
			solve(board)
			check = findEmpty(board)
			if check == None:
				# Check if there are any empty spaces left
				return
		# Not valid, empty out the board and try again
		board[row][col] = 0
	# 1 - 9 didn't work, backtrack it. 
	return

def solveHelp(event):
	starttime = time.clock()

	for row in range(9):
		for col in range(9):
			try:
				i = int(board[row][col].get())
			except:
				i = 0
			numbers[row][col] = i
			board[row][col].delete(0, 'end')

	solve(numbers)

	for row in range(9):
		for col in range(9):
			board[row][col].insert(0, str(numbers[row][col]))

	endtime = time.clock()
	print("Time elapsed: " + str(endtime - starttime) + "s")


def clear(event):
	for y in range(9):
		for x in range(9):
			board[y][x].delete(0, 'end')

solveButton.bind("<Button-1>", solveHelp)
clearButton.bind("<Button-1>", clear)

# Mainloop keeps the window up
window.mainloop()
