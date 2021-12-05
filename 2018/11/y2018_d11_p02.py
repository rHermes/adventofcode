import fileinput as fi

def cell_power(n, x, y):
    assert(0 < x <= 300 and 0 < y <= 300)
    rack_id = x + 10

    power = rack_id * y
    power += n
    power *= rack_id

    p = (power // 100) % 10
    return p - 5

def solve(n):
    # Create summation table
    grid = []
    prev_row = [0 for _ in range(301)]
    for y in range(300):
        row = [0]
        for x in range(300):
            row.append(cell_power(n, x+1, y+1) + prev_row[x+1] + row[-1] - prev_row[x])

        grid.append(row[1:])
        prev_row = row

    # Calculate best setup
    best = -100000
    best_pt = (-1000,-1000,-1000)
    for w in range(1,300):
        for y in range(300-w):
            for x in range(300-w):
                sm = grid[y+w][x+w] - grid[y+w][x] - grid[y][x+w] + grid[y][x]
                if best < sm:
                    best = sm
                    best_pt = (x+2,y+2,w)

    return ",".join(map(str,best_pt))



print(solve(int(next(fi.input()))))
