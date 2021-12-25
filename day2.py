from aocd.models import Puzzle

puzzle_input = Puzzle(2021, 2).input_data.split("\n")

def part1(input_list):
	position = [0, 0]
	for entry in input_list:
		direction, amount = entry.split(" ")[0], int(entry.split(" ")[1])
		if direction == "forward":
			position[0] += amount
		if direction == "up":
			position[1] -= amount
		if direction == "down":
			position[1] += amount
	
	return position[0] * position[1]

print(part1(puzzle_input))

def part2(input_list):
	position = [0, 0]
	aim = 0
	for entry in input_list:
		direction, amount = entry.split(" ")[0], int(entry.split(" ")[1])
		if direction == "forward":
			position[0] += amount
			position[1] += aim * amount
		if direction == "up":
			aim -= amount
		if direction == "down":
			aim += amount
	
	return position[0] * position[1]

print(part2(puzzle_input))
