class PuzzleGrid:
	"""Class that houses the puzzle grid
	Also has some lists that allow for quick column, row, and local square grouping
	"""
	def __init__(self, puzzle):
		self.puzzle = puzzle
		# Row One
		self.sq00 = self.puzzle[0][0]
		self.sq01 = self.puzzle[0][1]
		self.sq02 = self.puzzle[0][2]
		self.sq03 = self.puzzle[0][3]
		self.sq04 = self.puzzle[0][4]
		self.sq05 = self.puzzle[0][5]
		self.sq06 = self.puzzle[0][6]
		self.sq07 = self.puzzle[0][7]
		self.sq08 = self.puzzle[0][8]

		# Row Two
		self.sq10 = self.puzzle[1][0]
		self.sq11 = self.puzzle[1][1]
		self.sq12 = self.puzzle[1][2]
		self.sq13 = self.puzzle[1][3]
		self.sq14 = self.puzzle[1][4]
		self.sq15 = self.puzzle[1][5]
		self.sq16 = self.puzzle[1][6]
		self.sq17 = self.puzzle[1][7]
		self.sq18 = self.puzzle[1][8]

		# Row Three
		self.sq20 = self.puzzle[2][0]
		self.sq21 = self.puzzle[2][1]
		self.sq22 = self.puzzle[2][2]
		self.sq23 = self.puzzle[2][3]
		self.sq24 = self.puzzle[2][4]
		self.sq25 = self.puzzle[2][5]
		self.sq26 = self.puzzle[2][6]
		self.sq27 = self.puzzle[2][7]
		self.sq28 = self.puzzle[2][8]

		# Row Four
		self.sq30 = self.puzzle[3][0]
		self.sq31 = self.puzzle[3][1]
		self.sq32 = self.puzzle[3][2]
		self.sq33 = self.puzzle[3][3]
		self.sq34 = self.puzzle[3][4]
		self.sq35 = self.puzzle[3][5]
		self.sq36 = self.puzzle[3][6]
		self.sq37 = self.puzzle[3][7]
		self.sq38 = self.puzzle[3][8]

		# Row Five
		self.sq40 = self.puzzle[4][0]
		self.sq41 = self.puzzle[4][1]
		self.sq42 = self.puzzle[4][2]
		self.sq43 = self.puzzle[4][3]
		self.sq44 = self.puzzle[4][4]
		self.sq45 = self.puzzle[4][5]
		self.sq46 = self.puzzle[4][6]
		self.sq47 = self.puzzle[4][7]
		self.sq48 = self.puzzle[4][8]

		# Row Six
		self.sq50 = self.puzzle[5][0]
		self.sq51 = self.puzzle[5][1]
		self.sq52 = self.puzzle[5][2]
		self.sq53 = self.puzzle[5][3]
		self.sq54 = self.puzzle[5][4]
		self.sq55 = self.puzzle[5][5]
		self.sq56 = self.puzzle[5][6]
		self.sq57 = self.puzzle[5][7]
		self.sq58 = self.puzzle[5][8]

		# Row Seven
		self.sq60 = self.puzzle[6][0]
		self.sq61 = self.puzzle[6][1]
		self.sq62 = self.puzzle[6][2]
		self.sq63 = self.puzzle[6][3]
		self.sq64 = self.puzzle[6][4]
		self.sq65 = self.puzzle[6][5]
		self.sq66 = self.puzzle[6][6]
		self.sq67 = self.puzzle[6][7]
		self.sq68 = self.puzzle[6][8]

		# Row Eight
		self.sq70 = self.puzzle[7][0]
		self.sq71 = self.puzzle[7][1]
		self.sq72 = self.puzzle[7][2]
		self.sq73 = self.puzzle[7][3]
		self.sq74 = self.puzzle[7][4]
		self.sq75 = self.puzzle[7][5]
		self.sq76 = self.puzzle[7][6]
		self.sq77 = self.puzzle[7][7]
		self.sq78 = self.puzzle[7][8]

		# Row Nine 
		self.sq80 = self.puzzle[8][0]
		self.sq81 = self.puzzle[8][1]
		self.sq82 = self.puzzle[8][2]
		self.sq83 = self.puzzle[8][3]
		self.sq84 = self.puzzle[8][4]
		self.sq85 = self.puzzle[8][5]
		self.sq86 = self.puzzle[8][6]
		self.sq87 = self.puzzle[8][7]
		self.sq88 = self.puzzle[8][8]

		# Helpful row names
		self.row0 = self.puzzle[0]
		self.row1 = self.puzzle[1]
		self.row2 = self.puzzle[2]
		self.row3 = self.puzzle[3]
		self.row4 = self.puzzle[4]
		self.row5 = self.puzzle[5]
		self.row6 = self.puzzle[6]
		self.row7 = self.puzzle[7]
		self.row8 = self.puzzle[8]

		# Helpful col names. 
		self.col0 = [row[0] for row in self.puzzle]
		self.col1 = [row[1] for row in self.puzzle]
		self.col2 = [row[2] for row in self.puzzle]
		self.col3 = [row[3] for row in self.puzzle]
		self.col4 = [row[4] for row in self.puzzle]
		self.col5 = [row[5] for row in self.puzzle]
		self.col6 = [row[6] for row in self.puzzle]
		self.col7 = [row[7] for row in self.puzzle]
		self.col8 = [row[8] for row in self.puzzle]

		# Helpful local square groupings.
		self.local1 = [self.puzzle[i][j] for i in range(3) for j in range(3)]
		self.local2 = [self.puzzle[i][j] for i in range(3) for j in range(3, 6)]
		self.local3 = [self.puzzle[i][j] for i in range(3) for j in range(6, 9)]
		self.local4 = [self.puzzle[i][j] for i in range(3, 6) for j in range(3)]
		self.local5 = [self.puzzle[i][j] for i in range(3, 6) for j in range(3, 6)]
		self.local6 = [self.puzzle[i][j] for i in range(3, 6) for j in range(6, 9)]
		self.local7 = [self.puzzle[i][j] for i in range(6, 9) for j in range(3)]
		self.local8 = [self.puzzle[i][j] for i in range(6, 9) for j in range(3, 6)]
		self.local9 = [self.puzzle[i][j] for i in range(6, 9) for j in range(6, 9)]

		self.rows_by_row_int = {
								0: puzzle[0],
								1: puzzle[1],
								2: puzzle[2],
								3: puzzle[3],
								4: puzzle[4],
								5: puzzle[5],
								6: puzzle[6],
								7: puzzle[7],
								8: puzzle[8]
								}
		self.cols_by_col_int = {
								0: [row[0] for row in puzzle],
								1: [row[1] for row in puzzle],
								2: [row[2] for row in puzzle],
								3: [row[3] for row in puzzle],
								4: [row[4] for row in puzzle],
								5: [row[5] for row in puzzle],
								6: [row[6] for row in puzzle],
								7: [row[7] for row in puzzle],
								8: [row[8] for row in puzzle]								
								}
		self.localnum_by_int = {
								1:[puzzle[i][j] for i in range(3) for j in range(3)]
								2:[puzzle[i][j] for i in range(3) for j in range(3, 6)]
								3:[puzzle[i][j] for i in range(3) for j in range(6, 9)]
								4:[puzzle[i][j] for i in range(3, 6) for j in range(3)]
								5:[puzzle[i][j] for i in range(3, 6) for j in range(3, 6)]
								6:[puzzle[i][j] for i in range(3, 6) for j in range(6, 9)]
								7:[puzzle[i][j] for i in range(6, 9) for j in range(3)]
								8:[puzzle[i][j] for i in range(6, 9) for j in range(3, 6)]
								9:[puzzle[i][j] for i in range(6, 9) for j in range(6, 9)]
								}


puzzle1 = [[8, 7, 0, 3, 4, 5, 0, 0, 6], 
		[0, 0, 9, 0, 0, 6, 0, 0, 1],
		[0, 5, 0, 0, 0, 1, 0, 0, 0],
		[0, 3, 0, 4, 0, 9, 0, 8, 5],
		[0, 9, 0, 0, 0, 0, 7, 0, 0],
		[7, 0, 0, 5, 0, 0, 0, 0, 0],
		[6, 0, 3, 0, 5, 0, 0, 9, 7], 
		[0, 1, 0, 6, 0, 0, 3, 0, 0],
		[0, 2, 0, 0, 0, 0, 5, 0, 0]]
grid = PuzzleGrid(puzzle1)

# Ran a test using puzzle above. All Values are working and pulling correctly. 
# Uncomment tests to double check. 
# print("Printing each indivdaul value")
# print(grid.sq00, grid.sq01, grid.sq02, grid.sq03, grid.sq04, grid.sq05, grid.sq06, grid.sq07, grid.sq08)
# print(grid.sq10, grid.sq11, grid.sq12, grid.sq13, grid.sq14, grid.sq15, grid.sq16, grid.sq17, grid.sq18)
# print(grid.sq20, grid.sq21, grid.sq22, grid.sq23, grid.sq24, grid.sq25, grid.sq26, grid.sq27, grid.sq28)
# print(grid.sq30, grid.sq31, grid.sq32, grid.sq33, grid.sq34, grid.sq35, grid.sq36, grid.sq37, grid.sq38)
# print(grid.sq40, grid.sq41, grid.sq42, grid.sq43, grid.sq44, grid.sq45, grid.sq46, grid.sq47, grid.sq48)
# print(grid.sq50, grid.sq51, grid.sq52, grid.sq53, grid.sq54, grid.sq55, grid.sq56, grid.sq57, grid.sq58)
# print(grid.sq60, grid.sq61, grid.sq62, grid.sq63, grid.sq64, grid.sq65, grid.sq66, grid.sq67, grid.sq68)
# print(grid.sq70, grid.sq71, grid.sq72, grid.sq73, grid.sq74, grid.sq75, grid.sq76, grid.sq77, grid.sq78)
# print(grid.sq80, grid.sq81, grid.sq82, grid.sq83, grid.sq84, grid.sq85, grid.sq86, grid.sq87, grid.sq88)
# print("Rows in Lists")
# print(grid.row0)
# print(grid.row1)
# print(grid.row2)
# print(grid.row3)
# print(grid.row4)
# print(grid.row5)
# print(grid.row6)
# print(grid.row7)
# print(grid.row8)
# print("Columns in Lists")
# print(grid.col0)
# print(grid.col1)
# print(grid.col2)
# print(grid.col3)
# print(grid.col4)
# print(grid.col5)
# print(grid.col6)
# print(grid.col7)
# print(grid.col8)
# print("Local Square Groups in List")
# print(grid.local1)
# print(grid.local2)
# print(grid.local3)
# print(grid.local4)
# print(grid.local5)
# print(grid.local6)
# print(grid.local7)
# print(grid.local8)
# print(grid.local9)
print(grid.rows_by_row_int.keys())
print(grid.rows_by_row_int.values())