
## Advent of Code
## Day 3, Problem 2
## Dominic R. 2022

## FILE HANDLING
# open the file in reading mode
file = open('input.txt', 'r')
# grab the lines
lines = file.readlines()
# close the file
file.close()

# priority string
priority = '+abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# separates the raw input into rucksacks
def separateRucksacks():
  rucksacks = [[]]
  count = 1
  for line in lines:
    rucksacks[len(rucksacks) - 1].append(line.replace('\n', ''))
    count += 1
    if count > 3:
      count = 1
      rucksacks.append([])
  rucksacks.pop()
  return rucksacks;

# grab the rucksacks
sacks = separateRucksacks();
sum = 0
# iterate through, find the common letter, and add the index to the sum
for sack in sacks:
  val = list(set(sack[0]) & set(sack[1]) & set(sack[2]))[0]
  sum += priority.find(val)
# output the sum of the priorities
print(sum)
