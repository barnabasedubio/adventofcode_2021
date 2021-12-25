from aocd.models import Puzzle

puzzle_input = Puzzle(2021, 7).input_data.split(",")
puzzle_input = [int(x) for x in puzzle_input]
test_input = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

def calculate_fuel(start, end, part):
    return sum([x for x in range(abs(start-end)+1)]) if part == "part2" else abs(start-end)

def get_min_fuel_cost(input_list, part):

    reference_list = [x for x in range(max(input_list)+1)]
    distances_for_each_crab = [0 for _ in range(len(reference_list))]

    for item in input_list:
        for ix, distance in enumerate(reference_list):
            distances_for_each_crab[ix] += calculate_fuel(item, distance, part)

    print(min(distances_for_each_crab))

# part 1
get_min_fuel_cost(puzzle_input, "part1")

# part 2
get_min_fuel_cost(puzzle_input, "part2")
