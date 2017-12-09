file = open("puzzle_files/day4.txt", "r")

total = 0
for line in file:
	word_list = line.split()
	if len(word_list) == len(set(word_list)):
		total += 1

file.close()

print (total)
