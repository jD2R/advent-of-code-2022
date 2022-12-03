file = open('input.txt', 'r')
lines = file.readlines()
file.close()

priority = '+abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

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

sacks = separateRucksacks();
sum = 0
for sack in sacks:
  val = list(set(sack[0]) & set(sack[1]) & set(sack[2]))[0]
  sum += priority.find(val)

print(sum)
