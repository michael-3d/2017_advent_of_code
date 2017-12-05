file = open("puzzle_files/day2.txt", "r")

total = 0
for line in file:
    sorted_list = sorted(line.split(), key=int)
    total = total + (int(sorted_list.pop()) - int(sorted_list[0]))

file.close()

print total