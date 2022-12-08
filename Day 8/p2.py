# https://github.com/hyper-neutrino/advent-of-code/blob/main/2022/day08p2.py
with open('input.txt') as file:
    grid = [list(map(lambda l: int(l.strip()), line.replace('\n', ''))) for line in file.readlines()]

    t = 0

    for r in range(len(grid)):
        for c in range(len(grid[r])):
            selected = grid[r][c]
            left = right = up = down = 0
            for x in range(c - 1, -1, -1):
                left += 1
                if grid[r][x] >= selected:
                    break
            for x in range(c + 1, len(grid[r])):
                right += 1
                if grid[r][x] >= selected:
                    break
            for x in range(r - 1, -1, -1):
                up += 1
                if grid[x][c] >= selected:
                    break
            for x in range(r + 1, len(grid)):
                down += 1
                if grid[x][c] >= selected:
                    break
            t = max(t, up * down * left * right)

    print(t)
