import copy


class SudokuSolver():
	"""Solves a given Sudoku Grid
	Uses some handy attributes from the PuzzleGrid class.
	Such as:
	- any squares value is stored .sqyx for any row y and col x
	- all of the rows are stored in lists called .rowy for row number y
	- all of the cols are stored in lists called .colx for column number x
	- any grid square local numbers are stored in lists called localz where z
								   1 | 2 | 3
	  							  ___|___|___
	  is mapped out in this grid   4 | 5 | 6
	  							  ___|___|___
	  							   7 | 8 | 9 
	"""
	def __init__(self, puzzle):
		self.puzzle = puzzle
		# Obtain (row, col) coordinates for every zero element in the give sudoku puzzle
		# Create a copy that can be modified while solving
		self.zeros = [(i, j) for i in range(9) for j in range(9) if puzzle[i][j] == 0]
		
		# Create a deep copy of the puzzle that can be modified while solving
		self.solving_puzzle = copy.deepcopy(puzzle)

	def puzzle_solver(self):
		# Solves the puzzle that the class was instantiated with returns solved puzzle
		puzzle = self.solving_puzzle
		zeros = self.zeros

		
		# Below loop will continue to calculate the possible options for each empty
		# square, filling in squares able, until the puzzl is fully solved. 
		while zeros != []:
			numbers_solved = 0
			for i, j in zeros:
				options = self.get_squares_possible_options(i, j, puzzle)
				if len(options) == 1:
					puzzle[i][j] = options[0]
					zeros.remove((i, j))
					numbers_solved += 1

			#Saftey Break. I.e. if the puzzle is too hard for this method we break the loop
			if numbers_solved == 0:
				print("Puzzle is to Hard for this method")
				break
		return puzzle 

	def get_squares_possible_options(self, row, col, solving_puzzle):
		# Return a list of numbers that could fit into a given position
		# Every square can have the numbers 1 to 9
		options = list(range(1, 10))

		# Get list of all the numbers in the came row, col, and local square.
		row_values = solving_puzzle[row]
		col_values = [x[col] for x in solving_puzzle if x != 0]
		local_square = [solving_puzzle[i][j] for i in range((row//3 * 3),(row//3 * 3 + 3)) for j in range((col//3 * 3),(col//3 * 3 + 3))] 
		
		# Remove numbers in same row from options
		for x in row_values:
			if x in options:
				options.remove(x)
		# Remove numbers in the same column
		for x in col_values:
			if x in options:
				options.remove(x)
		# Remove numbers in the same local square
		for x in local_square:
			if x in options:
				options.remove(x)

		# Anything left could potentially be the correct number
		return options 

puzzle1 = [[8, 7, 0, 3, 4, 5, 0, 0, 6], 
		[0, 0, 9, 0, 0, 6, 0, 0, 1],
		[0, 5, 0, 0, 0, 1, 0, 0, 0],
		[0, 3, 0, 4, 0, 9, 0, 8, 5],
		[0, 9, 0, 0, 0, 0, 7, 0, 0],
		[7, 0, 0, 5, 0, 0, 0, 0, 0],
		[6, 0, 3, 0, 5, 0, 0, 9, 7], 
		[0, 1, 0, 6, 0, 0, 3, 0, 0],
		[0, 2, 0, 0, 0, 0, 5, 0, 0]]


# Testing Sudoku Solver on puzzle 
game = SudokuSolver(puzzle1)
print(game.puzzle_solver())


