import tkinter as tk
import tkinter.ttk as ttk
from sudoku_solver import SudokuSolver

puzzle = [[8, 7, 0, 3, 4, 5, 0, 0, 6], 
		  [0, 0, 9, 0, 0, 6, 0, 0, 1],
		  [0, 5, 0, 0, 0, 1, 0, 0, 0],
		  [0, 3, 0, 4, 0, 9, 0, 8, 5],
		  [0, 9, 0, 0, 0, 0, 7, 0, 0],
		  [7, 0, 0, 5, 0, 0, 0, 0, 0],
		  [6, 0, 3, 0, 5, 0, 0, 9, 7], 
		  [0, 1, 0, 6, 0, 0, 3, 0, 0],
		  [0, 2, 0, 0, 0, 0, 5, 0, 0]]

root = tk.Tk()
root.title('Button Boy')

game = SudokuSolver(puzzle)
solved_puzzle = game.puzzle_solver()

def deactivate_and_style_given_numbers():
	for row in list_of_buttons:
		for button in row: 
			if button['text'] != 0:
				button.config(state=tk.DISABLED)
				button.config(bg='white')
				button.config(disabledforeground='black')
			else: 
				button.config(relief=tk.RAISED)
				button.config(bg="SystemButtonFace")
				button.config(state=tk.ACTIVE)
	start_game["state"] = tk.DISABLED
	reset_game["state"] = tk.ACTIVE

def initate_starting_numbers(puzzle):
	for i in range(3):
		row_of_buttons = list_of_buttons[i]
		for j in range(3):
			button = row_of_buttons[j]
			button.config(text=puzzle[i][j])
	deactivate_and_style_given_numbers()

def check_entry(button, i, j):
	if button['text'] == solved_puzzle[i][j]:
		button['bg'] = '#90EE90'
	else: 
		button['bg'] = "#FF8B8B"

def ensure_number_was_entered(button, i, j):
	# If button menu was closed and no number was entered, this function will reset the selected
	# buttons formatting
	if button['text'] == 0:
		update_button.config(relief=tk.ACTIVE)
		update_button.config(bg="SystemButtonFace")

def assign_number_button_menu(button, i, j):
	button_menu = tk.Toplevel()
	button_menu.title("Select the Squares Value")

	# Dynamically position number menu to left or right of game grid
	x = root.winfo_x()
	screen_width = root.winfo_screenwidth()
	if screen_width - x >= screen_width / 2: # More space on right side
		print("move right", x, screen_width, screen_width-x)
		button_menu.geometry("+%d+%d" % (x + 195, root.winfo_y()))
	else: # More space on left side
		print("move left", x, screen_width, x-screen_width)
		button_menu.geometry("+%d+%d" % (x - 190, root.winfo_y()))

	button_menu.grab_set()

	def number_input(button, number):
		button.config(text=number)
		button.config(relief=tk.RAISED)
		button.config(bg='#FFFFA2')
		button_menu.destroy()

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
	# submit_button = tk.Button(button_menu, text="Close Window", command=button_menu.destroy, padx=3)
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

def check_puzzle(variable, indx, mode):
	active_buttons_and_pos = [(list_of_buttons[i][j], i, j) for i in range(3) for j in range(3) if list_of_buttons[i][j]['state'] != tk.DISABLED]
	if validate.get() == 1:
		for button in active_buttons_and_pos:
			i, j = button[1], button[2]
			if button[0]["text"] == 0:
				continue
			elif button[0]['text'] == solved_puzzle[i][j]:
				button[0]['bg'] = '#90EE90'
			else: 
				button[0]['bg'] = "#FF8B8B"
	else: 
		for button in active_buttons_and_pos:
			button[0]['bg'] = "SystemButtonFace"
	validate.set(0)

def assign_number(i, j):
	update_button = list_of_buttons[i][j]
	update_button.config(relief=tk.SUNKEN)
	update_button.config(bg='grey')
	assign_number_button_menu(update_button, i, j)

def reset():
	initate_starting_numbers(puzzle)



# Create Buttons
button00 = tk.Button(root, text="X", command=lambda: assign_number(0, 0), height=3, width=7, state=tk.DISABLED)
button01 = tk.Button(root, text="X", command=lambda: assign_number(0, 1), height=3, width=7, state=tk.DISABLED)
button02 = tk.Button(root, text="X", command=lambda: assign_number(0, 2), height=3, width=7, state=tk.DISABLED)
button10 = tk.Button(root, text="X", command=lambda: assign_number(1, 0), height=3, width=7, state=tk.DISABLED)
button11 = tk.Button(root, text="X", command=lambda: assign_number(1, 1), height=3, width=7, state=tk.DISABLED)
button12 = tk.Button(root, text="X", command=lambda: assign_number(1, 2), height=3, width=7, state=tk.DISABLED)
button20 = tk.Button(root, text="X", command=lambda: assign_number(2, 0), height=3, width=7, state=tk.DISABLED)
button21 = tk.Button(root, text="X", command=lambda: assign_number(2, 1), height=3, width=7, state=tk.DISABLED)
button22 = tk.Button(root, text="X", command=lambda: assign_number(2, 2), height=3, width=7, state=tk.DISABLED)
# Place Buttons on grid
button00.grid(row=0, column=0)
button01.grid(row=0, column=1)
button02.grid(row=0, column=2, padx=(0,8))
button10.grid(row=1, column=0)
button11.grid(row=1, column=1)
button12.grid(row=1, column=2, padx=(0,8))
button20.grid(row=2, column=0, pady=(0,8))
button21.grid(row=2, column=1, pady=(0,8))
button22.grid(row=2, column=2, padx=(0,8), pady=(0,8))

# List of the buttons. Each button is located in the list at its sudoku grid position. 
list_of_buttons = [[button00, button01, button02],
					[button10, button11, button12],
					[button20, button21, button22]]

validate = tk.IntVar()
validate.trace_add('write', check_puzzle)
validate_entry = tk.Checkbutton(root, text="Validate Entries", variable=validate)
validate_entry.grid(row=4, column=0, columnspan=3, pady=5)

start_game = tk.Button(root, text="Clik to Load Puzzle", command=lambda: initate_starting_numbers(puzzle))
start_game.grid(row=3, column=0, columnspan=3, pady=5)

reset_game = tk.Button(root, text="Reset Game", command=reset, state=tk.DISABLED)
reset_game.grid(row=5, column=0, columnspan=3, pady=5)

root.mainloop()

