from aocd.models import Puzzle
from collections import defaultdict

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

def generate_connection_directory(connection_list):
	connection_map = defaultdict(list)
	for connection in connection_list:
		pair = connection.strip().split("-")
		for p1, p2 in zip(pair, reversed(pair)):  # [a, b] --> [(a, b), (b, a)]
			if p2 != "start":
				connection_map[p1].append(p2)
	del(connection_map["end"])

	return connection_map

def traverse1(input, path=["start"]):
	count = 0
	for cave in input[path[-1]]:
		if cave.isupper() or not cave in path:
			count = count+1 if cave == "end" else count+traverse1(input, path+[cave])
	return count

def traverse2(input, path=["start"]):
	count = 0
	for cave in input[path[-1]]:
		count = count+1 if cave == "end" else count+(traverse2, traverse1)[cave.islower() and cave in path](input, path+[cave])
	return count

# part a
traverse1(generate_connection_directory(puzzle_input))

# part b
traverse2(generate_connection_directory(puzzle_input))
