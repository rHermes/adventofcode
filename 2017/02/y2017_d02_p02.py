import fileinput

def solve_row(row):
    xs = list(sorted(row))
    for i in range(len(xs)-1):
        for j in range(i+1, len(xs)):
            if (xs[j] % xs[i]) == 0:
                return xs[j] // xs[i]

sheet = [[int(x) for x in line.strip().split()] for line in fileinput.input()]
ans = sum([solve_row(row) for row in sheet])

print(ans)
