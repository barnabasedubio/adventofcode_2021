from aocd.models import Puzzle
import copy

puzzle_input = Puzzle(2021, 11).input_data.split("\n")
puzzle_matrix = [[int(x) for x in line] for line in puzzle_input]
test_matrix = [
	[5,4,8,3,1,4,3,2,2,3],
	[2,7,4,5,8,5,4,7,1,1],
	[5,2,6,4,5,5,6,1,7,3],
	[6,1,4,1,3,3,6,1,4,6],
	[6,3,5,7,3,8,5,4,7,8],
	[4,1,6,7,5,2,4,6,4,5],
	[2,1,7,6,8,4,1,7,2,1],
	[6,8,8,2,8,8,1,1,3,4],
	[4,8,4,6,8,4,8,5,5,4],
	[5,2,8,3,7,5,1,5,2,6]
]
small_test_matrix = [
	[1,1,1,1,1],
	[1,9,9,9,1],
	[1,9,1,9,1],
	[1,9,9,9,1],
	[1,1,1,1,1]
]

def get_all_neighbors(input_matrix, row, col):
    neighbors = []
    row_above = max(row-1, 0)
    row_below = min(row+1, len(input_matrix)-1)
    col_before = max(col-1, 0)
    col_after = min(col+1, len(input_matrix[0])-1)

    for current_row in range(row_above, row_below+1):
        for current_col in range(col_before, col_after+1):
            if not (current_row == row and current_col == col):
                neighbors.append((current_row,current_col))

    return neighbors

def count_flashes(input_matrix, steps):
	flashes = 0
	input_matrix_copy = input_matrix[:]

	for _ in range(steps):
		input_matrix_copy = [[min(x+1, 10) for x in row] for row in input_matrix_copy]
		previous_iteration_matrix = copy.deepcopy(input_matrix_copy)
		processed_cells = []

		while True:
			charged_cells = [(row,col) 
							for row in range(len(input_matrix_copy)) 
							for col in range(len(input_matrix_copy)) 
							if input_matrix_copy[row][col] == 10]

			for cell in charged_cells:
				if cell in processed_cells: continue
				charged_cell_neighbors = get_all_neighbors(input_matrix_copy, cell[0], cell[1])
				for neighbor in charged_cell_neighbors:
					if neighbor not in processed_cells:
						input_matrix_copy[neighbor[0]][neighbor[1]] = min((input_matrix_copy[neighbor[0]][neighbor[1]]+1), 10)
			
			processed_cells += charged_cells

			if input_matrix_copy == previous_iteration_matrix: break
			else: previous_iteration_matrix = copy.deepcopy(input_matrix_copy)

		
		for row in range(len(input_matrix_copy)):
			for col in range(len(input_matrix_copy[0])):
				if input_matrix_copy[row][col] == 10:
					flashes += 1
					input_matrix_copy[row][col] = 0


	print(flashes)

def determine_synchronized_flash(input_matrix):
	steps = 1
	input_matrix_copy = input_matrix[:]

	for _ in range(9999999999): # if it ever reaches this number then I f-ed up. I just don't want to make this a while True loop.
		input_matrix_copy = [[min(x+1, 10) for x in row] for row in input_matrix_copy]
		previous_iteration_matrix = copy.deepcopy(input_matrix_copy)
		processed_cells = []

		while True:
			charged_cells = [(row,col) 
							for row in range(len(input_matrix_copy)) 
							for col in range(len(input_matrix_copy)) 
							if input_matrix_copy[row][col] == 10]

			for cell in charged_cells:
				if cell in processed_cells: continue
				charged_cell_neighbors = get_all_neighbors(input_matrix_copy, cell[0], cell[1])
				for neighbor in charged_cell_neighbors:
					if neighbor not in processed_cells:
						input_matrix_copy[neighbor[0]][neighbor[1]] = min((input_matrix_copy[neighbor[0]][neighbor[1]]+1), 10)
			
			processed_cells += charged_cells

			if input_matrix_copy == previous_iteration_matrix: break
			else: previous_iteration_matrix = copy.deepcopy(input_matrix_copy)

		
		for row in range(len(input_matrix_copy)):
			for col in range(len(input_matrix_copy[0])):
				if input_matrix_copy[row][col] == 10:
					input_matrix_copy[row][col] = 0

		if input_matrix_copy == [
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]:
			break

		steps += 1


	print(steps)

# part a
count_flashes(puzzle_matrix, 100)

# part b
determine_synchronized_flash(puzzle_matrix)
