from aocd.models import Puzzle
from pprint import pprint

puzzle_input = Puzzle(2021, 5).input_data
directions = []
for coords in puzzle_input.split("\n"):

	source_coords = coords.split(" -> ")[0]
	dest_coords = coords.split(" -> ")[1]

	source_coords_x = int(source_coords.split(",")[0])
	source_coords_y = int(source_coords.split(",")[1])

	dest_coords_x = int(dest_coords.split(",")[0])
	dest_coords_y = int(dest_coords.split(",")[1])

	directions.append([(source_coords_x, source_coords_y), (dest_coords_x, dest_coords_y)])

test_directions = [
	[(0, 9), (5, 9)],
	[(8, 0), (0, 8)],
	[(9, 4), (3, 4)],
	[(2, 2), (2, 1)],
	[(7, 0), (7, 4)],
	[(6, 4), (2, 0)],
	[(0, 9), (2, 9)],
	[(3, 4), (1, 4)],
	[(0, 0), (8, 8)],
	[(5, 5), (8, 2)]
]

def mark_fissures(input_directions, only_lines, threshold):
	# determine the largest number of the input directions. This will be the field size.
	largest_number = get_largest_number(input_directions)
	field = [[0 for _ in range(largest_number+1)] for _ in range(largest_number+1)]

	if only_lines:
		input_directions_copy = input_directions[:]
		input_directions = [direction for direction in input_directions_copy if (direction[0][0] == direction[1][0] or direction[0][1] == direction[1][1])]
	
	for direction in input_directions:
		delta_horizontal = direction[1][0] - direction[0][0]
		delta_vertical = direction[1][1] - direction[0][1]
		current_position = direction[0]
		target_position = direction[1]
		field[current_position[1]][current_position[0]] += 1
		while current_position != target_position:
			step_horizontal = 0 if not delta_horizontal else int(delta_horizontal / abs(delta_horizontal))
			step_vertical = 0 if not delta_vertical else int(delta_vertical / abs(delta_vertical))
			new_position = (current_position[0] + step_horizontal, current_position[1] + step_vertical)
			field[new_position[1]][new_position[0]] += 1
			current_position = new_position

	# return number of points higher than threshold
	count = 0
	for row in range(len(field)):
		for col in range(len(field)):
			if field[row][col] >= threshold:
				count += 1
	
	return count
	

def get_largest_number(input_directions):
	current_largest_number = -1
	for direction in input_directions:
		direction_numbers = [direction[0][0], direction[0][1], direction[1][0], direction[1][1]]
		current_largest_number = max(direction_numbers) if max(direction_numbers) > current_largest_number else current_largest_number
	return current_largest_number


# part 1
mark_fissures(directions, True, 2)

# part 2
mark_fissures(directions, False, 2)
