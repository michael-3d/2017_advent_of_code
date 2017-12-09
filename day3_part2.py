puzzle_input = int(input("Puzzle input: "))

x = 1
y = 0
x_dir = 0
y_dir = 1
step = 1
step_size = 1
increase = True
num = 1
graph = {(0, 0): 1}
while num < puzzle_input:
	adjacents = [
		(x+1, y),
		(x+1, y+1),
		(x, y+1),
		(x-1, y+1),
		(x-1, y),
		(x-1, y-1),
		(x, y-1),
		(x+1, y-1),
	]
	adjacent_sum = 0
	for a in adjacents:
		try:
			adjacent_sum += graph[a]
		except KeyError as e:
			pass
	graph[(x, y)] = adjacent_sum
	num = adjacent_sum
	x += x_dir
	y += y_dir
	step = (step + 1) % step_size;
	if step == 0:
		if increase:
			step_size += 1
		increase = not increase
		if x_dir == 0:
			x_dir = -y_dir
			y_dir = 0
		else:
			y_dir = x_dir
			x_dir = 0
print(num)
