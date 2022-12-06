
## Advent of Code
## Day 1, Problem 1
## Dominic R. 2022

## FILE HANDLING
# open the file in reading mode
file = open('input.txt', 'r')
# grab the lines
lines = file.readlines()
# close the file
file.close()

# initialize a list for storing each elf's food supply
numList = [[]]
# loop through the raw input data and store it in the list
for line in lines:
    if line == '\n':
        numList.append([])
    else:
        numList[len(numList) - 1].append(int(line))
# find the sum of each list item (another list)
sums = []
for i in numList:
    sums.append(sum(i))

# number of calories the elf with the most calories is carrying
print(max(sums))
