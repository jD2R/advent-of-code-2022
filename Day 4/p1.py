
## Advent of Code
## Day 4, Problem 1
## Dominic R. 2022

## FILE HANDLING
# open the file in reading mode
file = open('input.txt', 'r')
# grab the lines
lines = file.readlines()
# close the file
file.close()

# finds if there is a complete overlap of two lists
def findOverlap(e1, e2):
    return (e1[0] <= e2[0] and e1[1] >= e2[1]) or (e2[0] <= e1[0] and e2[1] >= e1[1])

# iterate through and find how many complete overlaps there are
count = 0
for line in lines:
    numbers = line.replace(',', '-').replace('\n', '').split('-')
    elf_1 = [int(numbers[0]), int(numbers[1])]
    elf_2 = [int(numbers[2]), int(numbers[3])]
    
    if findOverlap(elf_1, elf_2):
        count += 1
# output the final number
print(count)

    
