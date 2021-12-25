from aocd.models import Puzzle

def generate_list_of_boards(input_list):
	list_of_boards = []
	current_board = []
	for entry in input_list:
		if entry != "":
			entry = [x for x in entry.split(" ")]
			entry = [x for x in entry if x.isnumeric()]  # remove whitespace in front of single digits
			current_board.append([x for x in entry])
		else:
			# board complete. Add to board array and begin creating new board
			list_of_boards.append(current_board)
			current_board = []

	# once done with the puzzle input. Add the board that was being created. Since there is no " " line at the end
	list_of_boards.append(current_board)

	return list_of_boards

puzzle_input = Puzzle(2021, 4).input_data.split("\n")

order_of_selected_numbers = [x for x in puzzle_input[0].split(",")]
list_of_boards = generate_list_of_boards(puzzle_input[2:])  # ignore order of numbers selected and the initial blank line

test_order_of_selected_numbers = [str(x) for x in [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]]
test_list_of_boards = \
[[['22', '13', '17', '11', '0'],
  ['8', '2', '23', '4', '24'],
  ['21', '9', '14', '16', '7'],
  ['6', '10', '3', '18', '5'],
  ['1', '12', '20', '15', '19']],
 [['3', '15', '0', '2', '22'],
  ['9', '18', '13', '17', '5'],
  ['19', '8', '7', '25', '23'],
  ['20', '11', '10', '24', '4'],
  ['14', '21', '16', '12', '6']],
 [['14', '21', '17', '24', '4'],
  ['10', '16', '15', '9', '19'],
  ['18', '8', '23', '26', '20'],
  ['22', '11', '13', '6', '5'],
  ['2', '0', '12', '3', '7']]]

def part1(order_of_selected_numbers, list_of_boards):
	for selected_number in order_of_selected_numbers:
		for board in list_of_boards:
			board = mark_number(board, selected_number)
			if does_bingo_exist(board):
				return get_sum_of_unmarked_numbers(board) * int(selected_number)

def part2(order_of_selected_numbers, list_of_boards):
	last_winning_board, last_selected_number = None, None
	for selected_number in order_of_selected_numbers:
		for board in list_of_boards:
			if not does_bingo_exist(board):
				board = mark_number(board, selected_number)
				if does_bingo_exist(board):
					last_winning_board, last_selected_number = board, selected_number

	return get_sum_of_unmarked_numbers(last_winning_board) * int(last_selected_number)

part1(order_of_selected_numbers, list_of_boards)

# you need to refresh the cell that defines the puzzle input before executing this cell

part2(order_of_selected_numbers, list_of_boards)

def does_bingo_exist(board):
	# first check if a row exists with only marked numbers
	for numbers_row in board:
		if numbers_row[0][0] == "." and (numbers_row[0][0] == numbers_row[1][0] == numbers_row[2][0] == numbers_row[3][0] == numbers_row[4][0]):
			return True

	# check if a column exists with only marked numbers
	for column_entries in list(zip(board[0], board[1], board[2], board[3], board[4])):
		if column_entries[0][0] == "." and (column_entries[0][0] == column_entries[1][0] == column_entries[2][0] == column_entries[3][0] == column_entries[4][0]):
			return True

	return False

def mark_number(board, selected_number):
	for row in range(len(board)):
		for col in range(len(board[0])):
			if board[row][col] == selected_number:
				board[row][col] = "." + board[row][col]
	return board

def get_sum_of_unmarked_numbers(board):
	unmarked_numbers = []
	for row in board:
		for number in row:
			if not number.startswith("."):
				unmarked_numbers.append(number)
	
	return sum([int(x) for x in unmarked_numbers])
