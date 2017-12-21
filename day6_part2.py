file = open("puzzle_files/day6.txt", "r")

bank = []
for line in file:
    bank = map(int, line.split())
file.close()

bank_perms = []
count = 0
while bank not in bank_perms:
    bank_perms.append(list(bank))
    largest = sorted(bank).pop()
    largest_pos = bank.index(largest)
    bank[largest_pos] = 0
    i = largest_pos
    size = len(bank)
    for x in xrange(0, largest):
        i = (i + 1) % size
        bank[i] += 1
    count += 1

print(len(bank_perms) - bank_perms.index(bank))
