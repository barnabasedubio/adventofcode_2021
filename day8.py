from aocd.models import Puzzle
from pprint import pprint


puzzle_input = Puzzle(2021, 8).input_data.split("\n")

test_input = [
			"be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe", 
			"edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc", 
			"fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg", 
			"fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
			"aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea", 
			"fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb", 
			"dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe", 
			"bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef", 
			"egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb", 
			"gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"]


def part1(input_list):
	counter = 0
	for entry in input_list:
		output_list = entry.split(" | ")[1].split(" ")
		relevant_digits = [output for output in output_list if len(output) in (2, 4, 3, 7)]
		counter += len(relevant_digits)
	
	print(counter)


def get_unique_numbers(entry):
	all_codes = entry.split(" | ")[0].split(" ") + entry.split(" | ")[1].split(" ")
	one = [item for item in all_codes if len(item) == 2][0]
	four = [item for item in all_codes if len(item) == 4][0]
	seven = [item for item in all_codes if len(item) == 3][0]
	eight = [item for item in all_codes if len(item) == 7][0]

	return one, four, seven, eight


def decode_number(item, one, four, seven, eight):
	if len(item) == 6:
		# can either be 9, 6,  or 0
		if len(intersection(list(four), list(item))) == len(list(four)):
			return "9"
		elif len(intersection(list(one), list(item))) != len(list(one)):
			return "6"
		else:
			return "0"

	elif len(item) == 5:
		# can either be 2, 3 or 5:
		if len(intersection(list(one), list(item))) == len(list(one)):
			return "3"
		elif len(intersection(list(four), list(item))) == 3:
			return "5"
		else:
			return "2"


def intersection(list1, list2):
	return [item for item in list1 if item in list2]


def part2(input_list):
	total = 0
	for entry in input_list:
		one, four, seven, eight = get_unique_numbers(entry)
		# print(one, four, seven, eight)
		output_list = entry.split(" | ")[1].split(" ")
		number_string = ""
		for item in output_list:
			# print(f"Item: {item}")
			if sorted(list(item)) == sorted(list(one)):
				number_string += "1"
			elif sorted(list(item)) == sorted(list(four)):
				number_string += "4"
			elif sorted(list(item)) == sorted(list(seven)):
				number_string += "7"
			elif sorted(list(item)) == sorted(list(eight)):
				number_string += "8"
			else:
				# print(item)
				number_string += decode_number(item, one, four, seven, eight)
			# print(number_string)
		total += int(number_string)
	print(total)


part1(puzzle_input)
part2(puzzle_input)
