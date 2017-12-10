import tkinter as tk 

window = tk.Tk()

mainFrame = tk.Frame(window)

board = []

# Automatically generate the empty sudoku board
for row in range(9):
	board.append([])
	for col in range(9):
		board[row].append(tk.Entry(window, width=3, justify='center'))
		board[row][col].grid(row=row, column=col)
			
# Solve Button
solveButton = tk.Button(window, text=" Solve! ")
solveButton.grid(row=10, column=1, columnspan=3, pady=2)

# Clear Button
clearButton = tk.Button(window, text=" Clear! ")
clearButton.grid(row=10, column=5, columnspan=3, pady=2)

## Returns first empty space on the board ##
def findEmpty():
	for row in range(9):
		for col in range(9):
			if board[row][col].get() == "":
				return [row, col]
	return None

## Returns True if valid, else False ##
def checkValid(row, col):
	number = board[row][col].get()
	# Check if the same number exists in the same row or col
	for i in range(9):
		if i != row and board[i][col].get() == number:
			return False
		if i != col and board[row][i].get() == number:
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
				if board[b_row + y][b_col + x].get() == number:
					return False
	return True

# Check is there any empty spaces
# Try 1 - 9 
# Check if valid
# Recurse and find next empty space
def solve(event):

	empty = findEmpty()
	if empty != None:
		row, col = empty
	else:
		"We're done!"
		return

	for attempt in range(1,10):
		board[row][col].insert(0, str(attempt))

		if checkValid(row, col):
			solve(event)
			check = findEmpty()
			if check == None:
				"We're Done!"
				return
		# Not valid, empty out the board and try again
		board[row][col].delete(0, 'end')
	# 1 - 9 didn't work, backtrack it. 
	return

def clear(event):
	for y in range(9):
		for x in range(9):
			board[y][x].delete(0, 'end')

solveButton.bind("<Button-1>", solve)
clearButton.bind("<Button-1>", clear)

# Mainloop keeps the window up
window.mainloop()
