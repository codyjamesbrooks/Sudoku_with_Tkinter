import tkinter as tk 

class Sudoku():
	"""A Sudoku tkinter application"""
	def __init__(self):
		"""Establish the game window"""
		self.root = tk.Tk()
		self.root.title("Cody's Sudoku A Python Project")
		self.root.geometry('750x750')
		self.root.update()
		
		# build menu frame
		menu_frame = tk.Frame(self.root, bg='red', borderwidth=1)
		menu_frame.grid(row=0, column=0, sticky='NS', fill=YES, expand=)
		label1 = tk.Label(menu_frame, text="menu").pack()

		# build frame for sudoku game grid
		grid_frame = tk.Frame(self.root, bg='blue', borderwidth=1)
		grid_frame.grid(row=0, column=1, sticky='NS')
		label2 = tk.Label(grid_frame, text="game grid").pack()
		

		self.root.mainloop()

	# def game_intro(self):
	# 	# Function for opening screen and get difficulty setting
		
	# 	def get_difficulty(difficulty):
	# 		self.game_difficulty = difficulty

	# 	opening_frame = tk.Frame(self.root)

	# 	# Main Label # Diff buttons
	# 	game_label = tk.Label(opening_frame, text="Sudoku Pro", height=35, width=100)
	# 	easy_button = tk.Button(opening_frame, text="Easy", height=3, width=15,
	# 							command=lambda: get_difficulty("Easy"))
	# 	medium_button = tk.Button(opening_frame, text="Medium", height=3, width=15,
	# 							command=lambda: get_difficulty("Medium"))
	# 	hard_button = tk.Button(opening_frame, text="Hard", height=3, width=15,
	# 							command=lambda: get_difficulty("Hard"))

	# 	# Place the buttons and labels on the frame
	# 	game_label.grid(row=0, column=0, columnspan=3)
	# 	easy_button.grid(row=1, column=0)
	# 	medium_button.grid(row=1, column=1)
	# 	hard_button.grid(row=1, column=2)

	# 	opening_frame.pack(fill=tk.BOTH, expand=tk.YES)
		



		# self.puzzles = {
		# 	"Easy" : [[0, 0, 4, 9, 6, 2, 3, 0, 0],
		# 			[0, 6, 0, 1, 0, 0, 4, 0, 0],
		# 			[8, 2, 0, 3, 7, 0, 0, 0, 6],
		# 			[0, 0, 1, 4, 0, 6, 0, 2, 0],
		# 			[0, 0, 2, 7, 5, 0, 0, 0, 0],
		# 			[0, 9, 3, 2, 0, 0, 7, 0, 4],
		# 			[2, 7, 0, 0, 3, 0, 9, 4, 0],
		# 			[1, 0, 0, 0, 0, 0, 2, 7, 5],
		# 			[1, 0, 0, 0, 0, 0, 2, 7, 5],
		# 			[9, 0, 0, 8, 2, 0, 0, 0, 1]],
		# 	"Medium" : [[8, 7, 0, 3, 4, 5, 0, 0, 6], 
		# 			[0, 0, 9, 0, 0, 6, 0, 0, 1],
		# 			[0, 5, 0, 0, 0, 1, 0, 0, 0],
		# 			[0, 3, 0, 4, 0, 9, 0, 8, 5],
		# 			[0, 9, 0, 0, 0, 0, 7, 0, 0],
		# 			[7, 0, 0, 5, 0, 0, 0, 0, 0],
		# 			[6, 0, 3, 0, 5, 0, 0, 9, 7], 
		# 			[0, 1, 0, 6, 0, 0, 3, 0, 0],
		# 			[0, 2, 0, 0, 0, 0, 5, 0, 0]],
		# 	"Hard" : [[0, 0, 0, 5, 6, 8, 4, 0, 0],
		# 			[0, 8, 7, 0, 0, 0, 9, 0, 5],
		# 			[0, 5, 0, 0, 0, 0, 6, 8, 0],
		# 			[0, 0, 0, 9, 2, 0, 0, 7, 0],
		# 			[0, 2, 0, 0, 0, 1, 0, 0, 9],
		# 			[8, 0, 0, 0, 7, 0, 0, 0, 0], 
		# 			[4, 0, 0, 0, 0, 5, 0, 0, 2], 
		# 			[0, 3, 0, 0, 0, 0, 0, 6, 4], 
		# 			[0, 0, 0, 7, 3, 0, 0, 9, 0]]
		# }

if __name__ == '__main__':
	game = Sudoku()
