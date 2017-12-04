puzzle_input = str(input("Puzzle input: "))

input_length = len(puzzle_input)
total = 0
for i in range(0, input_length):
    next_i = (i + 1) % input_length
    if puzzle_input[i] == puzzle_input[next_i]:
        total = total + int(puzzle_input[i])

print total