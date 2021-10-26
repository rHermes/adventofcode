import fileinput as fi

def solve(col, row, S=20151125):
    M = 33554393
    B = 252533

    max_y = 1
    idx = 0
    while True:
        y = max_y
        x = 1
        max_y += 1

        while y > 0:
            if y == row and x == col:
                return (S * pow(B, idx, M)) % M

            idx += 1
            y -=1
            x += 1

parts = next(fi.input()).split()
row = int(parts[parts.index("row")+1][:-1])
column = int(parts[parts.index("column")+1][:-1])

print(solve(column, row))
