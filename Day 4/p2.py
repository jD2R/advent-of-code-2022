
## Advent of Code
## Day 4, Problem 2
## Dominic R. 2022

## FILE HANDLING
# open the file in reading mode
file = open('Day 4\input.txt', 'r')
# grab the lines
lines = file.readlines()
# close the file
file.close()

# iterate through the lines
count = 0
for line in lines:
    numbers = line.replace(',', '-').replace('\n', '').split('-')

    # create a set of ranges for each elf
    elf_1 = set(range(int(numbers[0]), int(numbers[1]) + 1))
    elf_2 = set(range(int(numbers[2]), int(numbers[3]) + 1))

    # check for overlap (credit to @davidism on GitHub)
    if elf_1 <= elf_2 or elf_2 <= elf_1:
        count += 1
    elif elf_1 & elf_2:
        count += 1
# output the final number
print(count)
