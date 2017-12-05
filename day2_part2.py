file = open("puzzle_files/day2.txt", "r")

total = 0
for line in file:
    sorted_list = sorted(line.split(), key=int)
    found = False
    while not found:
        largest_number = int(sorted_list.pop())
        for i in range(0, len(sorted_list)):
            if (largest_number % int(sorted_list[i])) == 0:
                total = total + (largest_number / int(sorted_list[i]))
                found = True

file.close()

print total