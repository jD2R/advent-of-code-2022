
## Advent of Code
## Day 3, Problem 1
## Dominic R. 2022

## FILE HANDLING
# open the file in reading mode
file = open('Day 3\input.txt', 'r')
# grab the lines
lines = file.readlines()
# close the file
file.close()

# priority list rankings
priority = '+abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# sum of all the priorities
sum = 0

# iterate through the lines
for line in lines:
  n = len(line)
  # slice the lines
  comp1 = line[0:n//2]
  comp2 = line[n//2:]
  # find the common letter
  letter = "".join(list(set(comp1) & set(comp2)))
  # find the letter in the priority string
  val = priority.find(str(letter));
  # add the index in the priority string to the sum
  sum += val
# output the sum of the priorities
print(sum)
