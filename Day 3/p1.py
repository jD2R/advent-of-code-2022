file = open('input.txt', 'r')
lines = file.readlines()
file.close()

priority = '+abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

sum = 0

for line in lines:
  n = len(line)
  comp1 = line[0:n//2]
  comp2 = line[n//2:]
  letter = "".join(list(set(comp1) & set(comp2)))
  print(letter)
  val = priority.find(str(letter));
  sum += val

print(sum)
