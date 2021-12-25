from aocd.models import Puzzle
from functools import reduce

puzzle_input = Puzzle(2021, 9).input_data.split("\n")
puzzle_matrix = [[int(x) for x in line] for line in puzzle_input]
test_matrix = [
	[2,1,9,9,9,4,3,2,1,0],
	[3,9,8,7,8,9,4,9,2,1],
	[9,8,5,6,7,8,9,8,9,2],
	[8,7,6,7,8,9,6,7,8,9],
	[9,8,9,9,9,6,5,6,7,8]
]

def get_neighbors(input_matrix, row, col, coords):
	# corners
	if row == 0 and col == 0:
		return [input_matrix[row][col+1], input_matrix[row+1][col]] if not coords else [(row,col+1) ,(row+1,col)]  # east, south
	elif row == 0 and col == len(input_matrix[0])-1:
		return [input_matrix[row+1][col], input_matrix[row][col-1]] if not coords else [(row+1,col) ,(row,col-1)]  # south, west
	elif row == len(input_matrix)-1 and col == 0:
		return [input_matrix[row-1][col], input_matrix[row][col+1]] if not coords else [(row-1,col) ,(row,col+1)]  # north, east
	elif row == len(input_matrix)-1 and col == len(input_matrix[0])-1:
		return [input_matrix[row-1][col], input_matrix[row][col-1]] if not coords else [(row-1,col) ,(row,col-1)]  # north, west

	# edges
	if row == 0 and col not in (0, len(input_matrix[0])-1):
		return [input_matrix[row][col+1], input_matrix[row+1][col], input_matrix[row][col-1]] if not coords else [(row,col+1), (row+1,col), (row,col-1)]  # east, south, west
	elif row == len(input_matrix)-1 and col not in (0, len(input_matrix[0])-1):
		return [input_matrix[row-1][col], input_matrix[row][col+1], input_matrix[row][col-1]] if not coords else [(row-1,col), (row,col+1), (row,col-1)] # north, east, west
	elif col == 0 and row not in (0, len(input_matrix)-1):
		return [input_matrix[row-1][col], input_matrix[row][col+1], input_matrix[row+1][col]] if not coords else [(row-1,col), (row,col+1), (row+1,col)] # north, east, south
	elif col == len(input_matrix[0])-1 and row not in (0, len(input_matrix)-1):
		return [input_matrix[row-1][col], input_matrix[row+1][col], input_matrix[row][col-1]] if not coords else [(row-1,col), (row+1,col), (row,col-1)] # north, south, west

	# inside
	elif row not in (0, len(input_matrix)-1) and col not in (0, len(input_matrix[0])-1):
		return [
			input_matrix[row-1][col], # north
			input_matrix[row][col+1], # east
			input_matrix[row+1][col], # south
			input_matrix[row][col-1], # west
		] if not coords else [
			(row-1,col), (row,col+1), (row+1,col), (row,col-1)
		]


def get_low_points(input_matrix, coords):
	low_points = []
	low_points_coords = []
	for ix, row in enumerate(input_matrix):
		for iy, item in enumerate(row):
			neighbors = get_neighbors(input_matrix, ix, iy, False)
			if item < min(neighbors):
				low_points.append(item)
				low_points_coords.append((ix, iy))

	return low_points_coords if coords else low_points

def part2(input_matrix):
	list_of_basins = []
	for low_point_coord in get_low_points(input_matrix, True):
		local_basin = []
		local_basin.append(low_point_coord)
		# begin BFS
		queue = [low_point_coord]
		while queue:
			current = queue.pop(0)
			valid_neighbors = [coord for coord in get_neighbors(input_matrix, current[0], current[1], True) if input_matrix[coord[0]][coord[1]] != 9 and coord not in local_basin]
			for neighbor in valid_neighbors:
					local_basin.append(neighbor)
			queue += valid_neighbors

		list_of_basins.append(local_basin)

	list_of_basins.sort(key=len, reverse=True)
	result = reduce(lambda x, y: x*y, [len(x) for x in list_of_basins[:3]])
	print(result)

# part 1
print(sum([x+1 for x in get_low_points(puzzle_matrix, False)]))

# part 2
part2(puzzle_matrix)