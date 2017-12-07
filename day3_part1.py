puzzle_input = int(input("Puzzle input: "))

x = 1
step = 1
step_iteration = 1

while x < puzzle_input:
    prev_x = x
    x += step
    if step_iteration == 0:
        step += 1
    step_iteration = (step_iteration + 1) % 2

x -= 1
centre = x - ((x - prev_x) / 2)

print((step / 2) + abs(centre - puzzle_input))