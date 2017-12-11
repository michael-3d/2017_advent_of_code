file = open("puzzle_files/day5.txt", "r")

step_list = []
for x in file:
    step_list.append(int(x))
file.close()

i = 0
step_count = 0
while True:
    try:
        new_i = i + step_list[i]
        step_list[i] += 1
        i = new_i
        step_count += 1
    except IndexError as e:
        break

print(step_count)