import tkinter as tk
from puzzle_grid import PuzzleGrid as PG

puzzle = [[8, 7, 0, 3, 4, 5, 0, 0, 6], 
		  [0, 0, 9, 0, 0, 6, 0, 0, 1],
		  [0, 5, 0, 0, 0, 1, 0, 0, 0],
		  [0, 3, 0, 4, 0, 9, 0, 8, 5],
		  [0, 9, 0, 0, 0, 0, 7, 0, 0],
		  [7, 0, 0, 5, 0, 0, 0, 0, 0],
		  [6, 0, 3, 0, 5, 0, 0, 9, 7], 
		  [0, 1, 0, 6, 0, 0, 3, 0, 0],
		  [0, 2, 0, 0, 0, 0, 5, 0, 0]]

grid = PG(puzzle)
print(grid.sq00)

# game = tk.Tk()
# game.title('Sudoku by Cody v.1')



# # Set up a frame widget to house the puzzle grid
# game_frame = tk.Frame(game)
# game_frame.pack(padx=15, pady=15)

# # Establish all of the Entry Fields and put them in the frame
# sq00 = tk.Entry(game_frame, width=3)
# sq01 = tk.Entry(game_frame, width=3)
# sq02 = tk.Entry(game_frame, width=3)
# sq03 = tk.Entry(game_frame, width=3)
# sq04 = tk.Entry(game_frame, width=3)
# sq05 = tk.Entry(game_frame, width=3)
# sq06 = tk.Entry(game_frame, width=3)
# sq07 = tk.Entry(game_frame, width=3)
# sq08 = tk.Entry(game_frame, width=3)

# sq00.grid(row=0, column=0, padx=1, pady=1)
# sq01.grid(row=0, column=1, padx=1, pady=1)
# sq02.grid(row=0, column=2, padx=1, pady=1)
# sq03.grid(row=0, column=3, padx=1, pady=1)
# sq04.grid(row=0, column=4, padx=1, pady=1)
# sq05.grid(row=0, column=5, padx=1, pady=1)
# sq06.grid(row=0, column=6, padx=1, pady=1)
# sq07.grid(row=0, column=7, padx=1, pady=1)
# sq08.grid(row=0, column=8, padx=1, pady=1)

# squares = [(sq00, 0, 0), (sq01, 0, 1), (sq02, 0, 2), (sq03, 0, 3), (sq04, 0, 4),
# 			(sq05, 0, 5), (sq06, 0, 6), (sq07, 0, 7), (sq08, 0, 8)]

# for square, y, x in squares:
# 	square.insert(0, puzzle[y][x])

# game.mainloop()