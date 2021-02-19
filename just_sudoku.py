import tkinter as tk
from sudoku_solver import SudokuSolver


game = tk.Tk()
game.title('Sudoku by Cody v.1')

puzzle = [[8, 7, 0, 3, 4, 5, 0, 0, 6], 
		  [0, 0, 9, 0, 0, 6, 0, 0, 1],
		  [0, 5, 0, 0, 0, 1, 0, 0, 0],
		  [0, 3, 0, 4, 0, 9, 0, 8, 5],
		  [0, 9, 0, 0, 0, 0, 7, 0, 0],
		  [7, 0, 0, 5, 0, 0, 0, 0, 0],
		  [6, 0, 3, 0, 5, 0, 0, 9, 7], 
		  [0, 1, 0, 6, 0, 0, 3, 0, 0],
		  [0, 2, 0, 0, 0, 0, 5, 0, 0]]

def deactivate_and_style_given_numbers():
	# Disables and styles Buttons with already given puzzle valeus.
	for row in list_of_buttons:
		for button in row: 
			if button['text'] != 0:
				button.config(state=tk.DISABLED)
				button.config(bg='white')
				button.config(disabledforeground='black')
				button.config(font='bold')

def initate_starting_numbers(puzzle):
	# Given a puzzle, function loads the button grid with the puzzle values
	for i in range(9):
		row_of_buttons = list_of_buttons[i]
		for j in range(9):
			button = row_of_buttons[j]
			button.config(text=puzzle[i][j])
	# Disables and styles Buttons with already given puzzle valeus. 		
	deactivate_and_style_given_numbers()
		

def assign_number_button_menu(button):
	# function called by assign_number(i, j). When player wants to assign a new number to a given
	# square. launches a second tk window, with a numpad of buttons. clicked buttton is assigned
	# as passed buttons text
	button_menu = tk.Toplevel()
	button_menu.title("Select the Squares Value")

	def number_input(button, number):
		# changes text label of button to number. closes second tkinter window.
		button.config(text=number)
		button_menu.destroy()

	# create buttons and instruction label
	button_menu_lbl = tk.Label(button_menu, text="Click Number to Assign")
	num1 = tk.Button(button_menu, text="1", width=7, height=3, command=lambda: number_input(button, 1))
	num2 = tk.Button(button_menu, text="2", width=7, height=3, command=lambda: number_input(button, 2))
	num3 = tk.Button(button_menu, text="3", width=7, height=3, command=lambda: number_input(button, 3))
	num4 = tk.Button(button_menu, text="4", width=7, height=3, command=lambda: number_input(button, 4))
	num5 = tk.Button(button_menu, text="5", width=7, height=3, command=lambda: number_input(button, 5))
	num6 = tk.Button(button_menu, text="6", width=7, height=3, command=lambda: number_input(button, 6))
	num7 = tk.Button(button_menu, text="7", width=7, height=3, command=lambda: number_input(button, 7))
	num8 = tk.Button(button_menu, text="8", width=7, height=3, command=lambda: number_input(button, 8))
	num9 = tk.Button(button_menu, text="9", width=7, height=3, command=lambda: number_input(button, 9))
	# place buttons on numpad grid
	num1.grid(row=0, column=0)
	num2.grid(row=0, column=1)
	num3.grid(row=0, column=2)
	num4.grid(row=1, column=0)
	num5.grid(row=1, column=1)
	num6.grid(row=1, column=2)
	num7.grid(row=2, column=0)
	num9.grid(row=2, column=2)
	num8.grid(row=2, column=1)
	button_menu_lbl.grid(row=3, column=0, columnspan=3)			

def assign_number(i, j):
	# allows user to assign new value to the clicked button. 
	# finds button that was clicked, send it to assign_number_button_menu
	update_button = list_of_buttons[i][j]
	assign_number_button_menu(update_button)

# Store all the buttons in list. position in list will mirror grid. 
list_of_buttons = []
# The puzzle buttons.
# Organized by rows. Row 0:
button00 = tk.Button(game, text="X", command=lambda: assign_number(0, 0), height=3, width=7)
button01 = tk.Button(game, text="X", command=lambda: assign_number(0, 1), height=3, width=7)
button02 = tk.Button(game, text="X", command=lambda: assign_number(0, 2), height=3, width=7)
button03 = tk.Button(game, text="X", command=lambda: assign_number(0, 3), height=3, width=7)
button04 = tk.Button(game, text="X", command=lambda: assign_number(0, 4), height=3, width=7)
button05 = tk.Button(game, text="X", command=lambda: assign_number(0, 5), height=3, width=7)
button06 = tk.Button(game, text="X", command=lambda: assign_number(0, 6), height=3, width=7)
button07 = tk.Button(game, text="X", command=lambda: assign_number(0, 7), height=3, width=7)
button08 = tk.Button(game, text="X", command=lambda: assign_number(0, 8), height=3, width=7)
# Place Buttons on puzzle gird. 
button00.grid(row=0, column=0)
button01.grid(row=0, column=1)
button02.grid(row=0, column=2, padx=(0,8))
button03.grid(row=0, column=3)
button04.grid(row=0, column=4)
button05.grid(row=0, column=5, padx=(0,8))
button06.grid(row=0, column=6)
button07.grid(row=0, column=7)
button08.grid(row=0, column=8)
# Place row of buttons in list of buttons for future use. 
list_of_buttons.append([button00, button01, button02, button03, button04, button05,
						button06, button07, button08])

# Row 1:
button10 = tk.Button(game, text="X", command=lambda: assign_number(1, 0), height=3, width=7)
button11 = tk.Button(game, text="X", command=lambda: assign_number(1, 1), height=3, width=7)
button12 = tk.Button(game, text="X", command=lambda: assign_number(1, 2), height=3, width=7)
button13 = tk.Button(game, text="X", command=lambda: assign_number(1, 3), height=3, width=7)
button14 = tk.Button(game, text="X", command=lambda: assign_number(1, 4), height=3, width=7)
button15 = tk.Button(game, text="X", command=lambda: assign_number(1, 5), height=3, width=7)
button16 = tk.Button(game, text="X", command=lambda: assign_number(1, 6), height=3, width=7)
button17 = tk.Button(game, text="X", command=lambda: assign_number(1, 7), height=3, width=7)
button18 = tk.Button(game, text="X", command=lambda: assign_number(1, 8), height=3, width=7)
button10.grid(row=1, column=0)
button11.grid(row=1, column=1)
button12.grid(row=1, column=2, padx=(0,8))
button13.grid(row=1, column=3)
button14.grid(row=1, column=4)
button15.grid(row=1, column=5, padx=(0,8))
button16.grid(row=1, column=6)
button17.grid(row=1, column=7)
button18.grid(row=1, column=8)
list_of_buttons.append([button10, button11, button12, button13, button14, button15,
						button16, button17, button18])

# Row 2:
button20 = tk.Button(game, text="X", command=lambda: assign_number(2, 0), height=3, width=7)
button21 = tk.Button(game, text="X", command=lambda: assign_number(2, 1), height=3, width=7)
button22 = tk.Button(game, text="X", command=lambda: assign_number(2, 2), height=3, width=7)
button23 = tk.Button(game, text="X", command=lambda: assign_number(2, 3), height=3, width=7)
button24 = tk.Button(game, text="X", command=lambda: assign_number(2, 4), height=3, width=7)
button25 = tk.Button(game, text="X", command=lambda: assign_number(2, 5), height=3, width=7)
button26 = tk.Button(game, text="X", command=lambda: assign_number(2, 6), height=3, width=7)
button27 = tk.Button(game, text="X", command=lambda: assign_number(2, 7), height=3, width=7)
button28 = tk.Button(game, text="X", command=lambda: assign_number(2, 8), height=3, width=7)
button20.grid(row=2, column=0, pady=(0,8))
button21.grid(row=2, column=1, pady=(0,8))
button22.grid(row=2, column=2, padx=(0,8), pady=(0,8))
button23.grid(row=2, column=3, pady=(0,8))
button24.grid(row=2, column=4, pady=(0,8))
button25.grid(row=2, column=5, padx=(0,8), pady=(0,8))
button26.grid(row=2, column=6, pady=(0,8))
button27.grid(row=2, column=7, pady=(0,8))
button28.grid(row=2, column=8, pady=(0,8))
list_of_buttons.append([button20, button21, button22, button23, button24, button25,
						button26, button27, button28])

# Row 3:
button30 = tk.Button(game, text="X", command=lambda: assign_number(3, 0), height=3, width=7)
button31 = tk.Button(game, text="X", command=lambda: assign_number(3, 1), height=3, width=7)
button32 = tk.Button(game, text="X", command=lambda: assign_number(3, 2), height=3, width=7)
button33 = tk.Button(game, text="X", command=lambda: assign_number(3, 3), height=3, width=7)
button34 = tk.Button(game, text="X", command=lambda: assign_number(3, 4), height=3, width=7)
button35 = tk.Button(game, text="X", command=lambda: assign_number(3, 5), height=3, width=7)
button36 = tk.Button(game, text="X", command=lambda: assign_number(3, 6), height=3, width=7)
button37 = tk.Button(game, text="X", command=lambda: assign_number(3, 7), height=3, width=7)
button38 = tk.Button(game, text="X", command=lambda: assign_number(3, 8), height=3, width=7)
button30.grid(row=3, column=0)
button31.grid(row=3, column=1)
button32.grid(row=3, column=2, padx=(0,8))
button33.grid(row=3, column=3)
button34.grid(row=3, column=4)
button35.grid(row=3, column=5, padx=(0,8))
button36.grid(row=3, column=6)
button37.grid(row=3, column=7)
button38.grid(row=3, column=8)
list_of_buttons.append([button30, button31, button32, button33, button34, button35,
						button36, button37, button38])

# Row 4:
button40 = tk.Button(game, text="X", command=lambda: assign_number(4, 0), height=3, width=7)
button41 = tk.Button(game, text="X", command=lambda: assign_number(4, 1), height=3, width=7)
button42 = tk.Button(game, text="X", command=lambda: assign_number(4, 2), height=3, width=7)
button43 = tk.Button(game, text="X", command=lambda: assign_number(4, 3), height=3, width=7)
button44 = tk.Button(game, text="X", command=lambda: assign_number(4, 4), height=3, width=7)
button45 = tk.Button(game, text="X", command=lambda: assign_number(4, 5), height=3, width=7)
button46 = tk.Button(game, text="X", command=lambda: assign_number(4, 6), height=3, width=7)
button47 = tk.Button(game, text="X", command=lambda: assign_number(4, 7), height=3, width=7)
button48 = tk.Button(game, text="X", command=lambda: assign_number(4, 8), height=3, width=7)
button40.grid(row=4, column=0)
button41.grid(row=4, column=1)
button42.grid(row=4, column=2, padx=(0,8))
button43.grid(row=4, column=3)
button44.grid(row=4, column=4)
button45.grid(row=4, column=5, padx=(0,8))
button46.grid(row=4, column=6)
button47.grid(row=4, column=7)
button48.grid(row=4, column=8)
list_of_buttons.append([button40, button41, button42, button43, button44, button45,
						button46, button47, button48])

# Row 5:
button50 = tk.Button(game, text="X", command=lambda: assign_number(5, 0), height=3, width=7)
button51 = tk.Button(game, text="X", command=lambda: assign_number(5, 1), height=3, width=7)
button52 = tk.Button(game, text="X", command=lambda: assign_number(5, 2), height=3, width=7)
button53 = tk.Button(game, text="X", command=lambda: assign_number(5, 3), height=3, width=7)
button54 = tk.Button(game, text="X", command=lambda: assign_number(5, 4), height=3, width=7)
button55 = tk.Button(game, text="X", command=lambda: assign_number(5, 5), height=3, width=7)
button56 = tk.Button(game, text="X", command=lambda: assign_number(5, 6), height=3, width=7)
button57 = tk.Button(game, text="X", command=lambda: assign_number(5, 7), height=3, width=7)
button58 = tk.Button(game, text="X", command=lambda: assign_number(5, 8), height=3, width=7)
button50.grid(row=5, column=0, pady=(0,8))
button51.grid(row=5, column=1, pady=(0,8))
button52.grid(row=5, column=2, padx=(0,8), pady=(0,8))
button53.grid(row=5, column=3, pady=(0,8))
button54.grid(row=5, column=4, pady=(0,8))
button55.grid(row=5, column=5, padx=(0,8), pady=(0,8))
button56.grid(row=5, column=6, pady=(0,8))
button57.grid(row=5, column=7, pady=(0,8))
button58.grid(row=5, column=8, pady=(0,8))
list_of_buttons.append([button50, button51, button52, button53, button54, button55,
						button56, button57, button58])

# Row 6:
button60 = tk.Button(game, text="X", command=lambda: assign_number(6, 0), height=3, width=7)
button61 = tk.Button(game, text="X", command=lambda: assign_number(6, 1), height=3, width=7)
button62 = tk.Button(game, text="X", command=lambda: assign_number(6, 2), height=3, width=7)
button63 = tk.Button(game, text="X", command=lambda: assign_number(6, 3), height=3, width=7)
button64 = tk.Button(game, text="X", command=lambda: assign_number(6, 4), height=3, width=7)
button65 = tk.Button(game, text="X", command=lambda: assign_number(6, 5), height=3, width=7)
button66 = tk.Button(game, text="X", command=lambda: assign_number(6, 6), height=3, width=7)
button67 = tk.Button(game, text="X", command=lambda: assign_number(6, 7), height=3, width=7)
button68 = tk.Button(game, text="X", command=lambda: assign_number(6, 8), height=3, width=7)
button60.grid(row=6, column=0)
button61.grid(row=6, column=1)
button62.grid(row=6, column=2, padx=(0,8))
button63.grid(row=6, column=3)
button64.grid(row=6, column=4)
button65.grid(row=6, column=5, padx=(0,8))
button66.grid(row=6, column=6)
button67.grid(row=6, column=7)
button68.grid(row=6, column=8)
list_of_buttons.append([button60, button61, button62, button63, button64, button65,
						button66, button67, button68])

# Row 7:
button70 = tk.Button(game, text="X", command=lambda: assign_number(7, 0), height=3, width=7)
button71 = tk.Button(game, text="X", command=lambda: assign_number(7, 1), height=3, width=7)
button72 = tk.Button(game, text="X", command=lambda: assign_number(7, 2), height=3, width=7)
button73 = tk.Button(game, text="X", command=lambda: assign_number(7, 3), height=3, width=7)
button74 = tk.Button(game, text="X", command=lambda: assign_number(7, 4), height=3, width=7)
button75 = tk.Button(game, text="X", command=lambda: assign_number(7, 5), height=3, width=7)
button76 = tk.Button(game, text="X", command=lambda: assign_number(7, 6), height=3, width=7)
button77 = tk.Button(game, text="X", command=lambda: assign_number(7, 7), height=3, width=7)
button78 = tk.Button(game, text="X", command=lambda: assign_number(7, 8), height=3, width=7)
button70.grid(row=7, column=0)
button71.grid(row=7, column=1)
button72.grid(row=7, column=2, padx=(0,8))
button73.grid(row=7, column=3)
button74.grid(row=7, column=4)
button75.grid(row=7, column=5, padx=(0,8))
button76.grid(row=7, column=6)
button77.grid(row=7, column=7)
button78.grid(row=7, column=8)
list_of_buttons.append([button70, button71, button72, button73, button74, button75,
						button76, button77, button78])

# Row 8:
button80 = tk.Button(game, text="X", command=lambda: assign_number(8, 0), height=3, width=7)
button81 = tk.Button(game, text="X", command=lambda: assign_number(8, 1), height=3, width=7)
button82 = tk.Button(game, text="X", command=lambda: assign_number(8, 2), height=3, width=7)
button83 = tk.Button(game, text="X", command=lambda: assign_number(8, 3), height=3, width=7)
button84 = tk.Button(game, text="X", command=lambda: assign_number(8, 4), height=3, width=7)
button85 = tk.Button(game, text="X", command=lambda: assign_number(8, 5), height=3, width=7)
button86 = tk.Button(game, text="X", command=lambda: assign_number(8, 6), height=3, width=7)
button87 = tk.Button(game, text="X", command=lambda: assign_number(8, 7), height=3, width=7)
button88 = tk.Button(game, text="X", command=lambda: assign_number(8, 8), height=3, width=7)
button80.grid(row=8, column=0, pady=(0,8))
button81.grid(row=8, column=1, pady=(0,8))
button82.grid(row=8, column=2, padx=(0,8), pady=(0,8))
button83.grid(row=8, column=3, pady=(0,8))
button84.grid(row=8, column=4, pady=(0,8))
button85.grid(row=8, column=5, padx=(0,8), pady=(0,8))
button86.grid(row=8, column=6, pady=(0,8))
button87.grid(row=8, column=7, pady=(0,8))
button88.grid(row=8, column=8, pady=(0,8))
list_of_buttons.append([button80, button81, button82, button83, button84, button85,
						button86, button87, button88])


start_game = tk.Button(game, text="Clik to Load Puzzle", command=lambda: initate_starting_numbers(puzzle))
start_game.grid(row=9, column=3, columnspan =3, pady=20)

game.mainloop()


