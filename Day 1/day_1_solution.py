# open the input file
file = open('day_1_input.txt', 'r')
# read the lines
Lines = file.readlines()

# initialize a list for storing each elf's food supply
numList = [[]]
# loop through the raw input data and store it in the list
count = 0
for line in Lines:
    count += 1
    if line == '\n':
        numList.append([])
    else:
        numList[len(numList) - 1].append(int(line))
# find the sum of each list item (another list)
sums = []
for i in numList:
    sums.append(sum(i))

# number of calories the elf with the most calories is carrying
# STAR 1 OUTPUT
print(max(sums))

# reverse sort the list and print the top three summed together
sums.sort(reverse=True)
# STAR 2 OUTPUT
print(sums[0] + sums[1] + sums[2]);
        
