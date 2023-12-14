import fileinput as fi

def solve(group):
    grid = [[c for c in line] for line in group.splitlines()]
    Y, X = (len(grid), len(grid[0]))

    # We check vertical.
    for y in range(1,Y):
        up = y-1
        down = y

        while 0 <= up and down < Y:
            urow = grid[up]
            drow = grid[down]

            if urow != drow:
                break

            up -= 1
            down += 1
        else:
            return y * 100

    # We check vertical.
    for x in range(1,X):
        left = x-1
        right = x
        while 0 <= left and right < X:
            lcol = [grid[y][left] for y in range(Y)]
            rcol = [grid[y][right] for y in range(Y)]

            if lcol != rcol:
                break

            # We advance
            left -= 1
            right += 1
        else:
            return x

    return 0

# Input parsing
INPUT = "".join(fi.input()).rstrip()
groups = INPUT.split("\n\n")

ans = 0
for group in groups:
    ans += solve(group)

print(ans)
