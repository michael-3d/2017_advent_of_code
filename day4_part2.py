file = open("puzzle_files/day4.txt", "r")

def charSort(s):
	return ''.join(sorted(s))

total = 0
for line in file:
	word_list = map(charSort, line.split())
	if len(word_list) == len(set(word_list)):
		total += 1

file.close()

print (total)
