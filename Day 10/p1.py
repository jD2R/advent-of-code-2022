X = 1
cycle = 0
sum = 0

with open('input.txt') as file:
    for line in file.readlines():
        L = line.split()
        if L[0] == 'addx':
            cycle += 1
            cycle += 1
            X += int(L[1])
        else:
            cycle += 1

    print(sum)
