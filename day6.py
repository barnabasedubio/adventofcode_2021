from aocd.models import Puzzle

puzzle_input = Puzzle(2021, 6).input_data.split(",")
puzzle_input = [int(x) for x in puzzle_input]
test_input = [3, 4, 3, 1, 2]

def simulate_population(initial_state, epochs):
    population_dict = {str(x):0 for x in range(9)}

    for entry in [str(x) for x in initial_state]:
        population_dict[entry] += 1

    new_fish_amount = population_dict["0"]

    for _ in range(epochs):
        for ix in range(8):
            population_dict[str(ix)] = population_dict[str(ix+1)]

            if ix == 6:
                population_dict[str(ix)] += new_fish_amount

        population_dict["8"] = new_fish_amount
        new_fish_amount = population_dict["0"]
    
    print(sum(population_dict.values()))

# part 1
simulate_population(puzzle_input, 80)

# part 2
simulate_population(puzzle_input, 256)
