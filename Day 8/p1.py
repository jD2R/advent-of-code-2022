# https://github.com/hyper-neutrino/advent-of-code/blob/main/2022/day08p1.py
with open('input.txt') as file:
    grid = [list(map(lambda l: int(l.strip()), line.replace('\n', ''))) for line in file.readlines()]

    t = 0

    for r in range(len(grid)):
        for c in range(len(grid[r])):
            selected = grid[r][c]
            t += int(
                    all(grid[x][c] < selected for x in range(r)) or
                    all(grid[r][x] < selected for x in range(c)) or
                    all(grid[x][c] < selected for x in range(r + 1, len(grid))) or
                    all(grid[r][x] < selected for x in range(c + 1, len(grid[r])))
                 )

    print(t)
