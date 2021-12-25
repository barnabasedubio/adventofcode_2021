from aocd.models import Puzzle

puzzle_input = Puzzle(2021, 1).input_data.split("\n")
puzzle_input = [int(x) for x in puzzle_input]

def part1(input_list):
	current = input_list[0]
	counter = 0
	for entry in input_list[1:]:
		if entry > current:
			counter += 1
		current = entry

	return counter

print(part1(puzzle_input))

def part2(input_list):
	counter = 0
	for ix in range(1, len(input_list)-2):
		previous = input_list[ix-1] +  input_list[ix] + input_list[ix+1]
		current =  input_list[ix] + input_list[ix+1] + input_list[ix+2]

		if current > previous:
			counter += 1
		previous = current

	return counter

print(part2(puzzle_input))
