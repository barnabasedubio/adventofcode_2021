from aocd.models import Puzzle

puzzle_input = Puzzle(2021, 3).input_data.split("\n")
test_input = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]

def part1(input_list):
	columns = len(input_list[0])

	gamma = ""
	epsilon = ""

	for ix in range(columns):

		ones = get_count_of_bit_in_list(input_list, 1, ix)
		zeros = get_count_of_bit_in_list(input_list, 0, ix)
		
		if ones > zeros:
			gamma += "1"
			epsilon += "0"
		else:
			gamma += "0"
			epsilon += "1"

	gamma_as_decimal = int(gamma, 2)
	epsilon_as_decimal = int(epsilon, 2)

	return gamma_as_decimal * epsilon_as_decimal

print(part1(puzzle_input))

def part2(input_list, rating):

	current_numbers_to_look_at = input_list
	current_index = 0
	tie_breaker = 1 if rating == "oxygen generator" else (0 if rating == "co2 scrubber" else -1)
	
	while len(current_numbers_to_look_at) > 1:

		num_ones = get_count_of_bit_in_list(current_numbers_to_look_at, 1, current_index)
		num_zeros = get_count_of_bit_in_list(current_numbers_to_look_at, 0, current_index)

		most_common = 1 if num_ones > num_zeros else (0 if num_zeros > num_ones else tie_breaker)
		least_common = 1 if num_ones < num_zeros else (0 if num_zeros < num_ones else tie_breaker)

		criteria = str(most_common) if rating == "oxygen generator" else str(least_common)

		current_numbers_to_look_at = [number for number in current_numbers_to_look_at if number[current_index] == criteria]

		current_index += 1

	return int(current_numbers_to_look_at[0], 2)


print(part2(puzzle_input, "oxygen generator") * part2(puzzle_input, "co2 scrubber"))

def get_count_of_bit_in_list(numbers, bit, position):
	column_values = [row[position] for row in numbers]
	ones = column_values.count("1")
	zeros = column_values.count("0")
	if bit == 1: return ones
	else: return zeros
