from aocd.models import Puzzle
from collections import defaultdict
from copy import deepcopy

puzzle_input = Puzzle(2021, 12).input_data.split("\n")
small_test_input = [
	"start-A",
	"start-b",
	"A-c",
	"A-b",
	"b-d",
	"A-end",
	"b-end"
]
medium_test_input = [
	"dc-end",
	"HN-start",
	"start-kj",
	"dc-start",
	"dc-HN",
	"LN-dc",
	"HN-end",
	"kj-sa",
	"kj-HN",
	"kj-dc",
]
large_test_input = [
	"fs-end",
	"he-DX",
	"fs-he",
	"start-DX",
	"pj-DX",
	"end-zg",
	"zg-sl",
	"zg-pj",
	"pj-he",
	"RW-he",
	"fs-DX",
	"pj-RW",
	"zg-RW",
	"start-pj",
	"he-WI",
	"zg-he",
	"pj-fs",
	"start-RW",
]

def generate_connection_dictionary(connections):
	# use of defaultdict saves us from having to instantiate an empty list (of check if a list already exists)
	connection_dictionary = defaultdict(list)
	for connection in connections:
		connection_pair = connection.strip().split("-")
		for start,end in zip(connection_pair, reversed(connection_pair)):
			if end != "start":
				connection_dictionary[start].append(end)
	
	del(connection_dictionary["end"])
	return connection_dictionary


# use DFS to find all valid paths from start to end
def find_paths(input_dictionary, part):
	connection_dictionary = deepcopy(input_dictionary)
	found_paths = []
	path_stack = []
	threshold = 10000

	current_path = "start,"
	path_stack.append({"start":connection_dictionary["start"]})

	while path_stack:

		small_caves_visited = [cave for cave in current_path.split(",") if cave.islower()]
		small_cave_visited_twice = len(small_caves_visited) > len(set(small_caves_visited))
		current_cave_dictionary = path_stack[-1]

		if part == "a":
			next_cave_options = [
				cave for cave in list(current_cave_dictionary.values())[0]
				if (cave.isupper() or cave not in current_path)
				and (current_path+f"{cave}" not in found_paths)]

		elif part == "b":
			next_cave_options = [
			cave for cave in list(current_cave_dictionary.values())[0]
			if (cave.isupper() or (cave != "start" and (cave not in current_path or not small_cave_visited_twice)))
			and (current_path+f"{cave}" not in found_paths)]

		else:
			print("Unknown part. Returning")
			break

		if not next_cave_options:
			current_cave_dictionary = path_stack.pop()
			current_cave_key = list(current_cave_dictionary.keys())[0]
			if not path_stack: break
			previous_cave_dict = path_stack[-1]
			previous_cave_key = list(previous_cave_dict.keys())[0]
			previous_cave_dict[previous_cave_key] = [cave for cave in previous_cave_dict[previous_cave_key] if cave != current_cave_key]
			current_path = ",".join(current_path.split(",")[:-2]) + ","

		else:
			next_cave = next_cave_options[0]
			current_path += f"{next_cave}" + ","
			path_stack.append({next_cave:connection_dictionary[next_cave]})
			if next_cave == "end":
				found_paths.append(current_path[:-1])  # remove trailing comma
				path_stack.pop()  # remove "end" from path stack
				current_path = ",".join(current_path.split(",")[:-2]) + ","  # remove "end," from current path

		# occasional status updates
		if len(found_paths) > threshold:
			print(len(found_paths))
			threshold += 10000

	print(len(found_paths))


def main():
	# part 1
	find_paths(generate_connection_dictionary(puzzle_input), part="a")

	# part 2
	find_paths(generate_connection_dictionary(puzzle_input), part="b")


if __name__ == "__main__": main()
