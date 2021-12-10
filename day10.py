from aocd.models import Puzzle


puzzle_input = Puzzle(2021, 10).input_data.split("\n")
test_input = [
	"[({(<(())[]>[[{[]{<()<>>",
	"[(()[<>])]({[<{<<[]>>(",
	"{([(<{}[<>[]}>{[]{[(<()>",
	"(((({<>}<{<{<>}{[]{[]{}",
	"[[<[([]))<([[{}[[()]]]",
	"[{[{({}]{}}([{[{{{}}([]",
	"{<[[]]>}<{[{[{[]{()[[[]",
	"[<(<(<(<{}))><([]([]()",
	"<{([([[(<>()){}]>(<<{{",
	"<{([{{}}[<[[[<>{}]]]>[]]"
]

openers = ["(", "[", "{", "<"]
closers = [")", "]", "}", ">"]


def get_opening_symbol(symbol):
	if symbol == ")": return "("
	if symbol == "]": return "["
	if symbol == "}": return "{"
	if symbol == ">": return "<"


def get_closing_symbol(symbol):
	if symbol == "(": return ")"
	if symbol == "[": return "]"
	if symbol == "{": return "}"
	if symbol == "<": return ">"	


def is_line_corrupt(line):
	symbol_stack = []
	for symbol in line:
		if symbol in openers:
			symbol_stack.append(symbol)
		elif symbol in closers:
			if symbol_stack[-1] == get_opening_symbol(symbol):
				symbol_stack.pop()
			else:
				return True
		else:
			print(f"Cannot assign symbol: {symbol}")
			return
	return False


def get_score(sequence_list):
	total = 0
	for sequence in sequence_list:
		total *= 5
		if sequence == ")":
			total += 1
		elif sequence == "]":
			total += 2
		elif sequence == "}":
			total += 3
		elif sequence == ">":
			total += 4
	return total


def part1(input_list):
	errors = {x:0 for x in closers}
	for entry in input_list:
		symbol_stack = []
		for symbol in entry:
			if symbol in openers:
				symbol_stack.append(symbol)
			elif symbol in closers:
				# check to see if opening symbol is the top entry of the stack
				if symbol_stack[-1] == get_opening_symbol(symbol):
					symbol_stack.pop()
				else:
					errors[symbol] += 1
					break  # since we only need the first illegal character
			else:
				print(f"Cannot assign symbol: {symbol}")
				return
	
	print(3*errors[")"] + 57*errors["]"] + 1197*errors["}"] + 25137*errors[">"])


def part2(input_list):
	completion_sequences = []
	for entry in [x for x in input_list if not is_line_corrupt(x)]:
		symbol_stack = []
		completion_sequence = ""
		for symbol in entry:
			if symbol in openers:
				symbol_stack.append(symbol)
			elif symbol in closers:
				if symbol_stack[-1] == get_opening_symbol(symbol):
					symbol_stack.pop()
			else:
				print(f"Cannot assign symbol: {symbol}")
				return
		# find out required symbols to complete the stack
		while symbol_stack:
			completion_sequence += get_closing_symbol(symbol_stack.pop())
		completion_sequences.append(completion_sequence)

	scores = sorted([get_score(sequence) for sequence in completion_sequences])
	middle_index = int(int(len(scores)-1) / 2)
	print(scores[middle_index])


def main():
	part1(puzzle_input)
	part2(puzzle_input)

if __name__ == "__main__": main()
