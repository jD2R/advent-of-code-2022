X = 1
o = []

with open('input.txt') as file:
    for line in file.readlines():
        L = line.split()
        if L[0] == 'addx':
            o.append(X)
            o.append(X)
            X += int(L[1])

        else:
            o.append(X)
    # @hyper-neutrino
    for i in range(0, len(o), 40):
        for j in range(40):
            print(end="#" if abs(o[i + j] - j) <= 1 else " ")
        print()
