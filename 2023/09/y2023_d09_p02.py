import fileinput as fi

ans = 0
for line in fi.input():
    rows = [[int(x) for x in line.split()]]

    while not all(x == 0 for x in rows[-1]):
        rows.append([y - x for x, y in zip(rows[-1][:-1], rows[-1][1:])])
    
    # We don't need the last row, as it's all zeros
    rows.pop()
    rows.reverse()

    last_diff = 0
    for row in rows:
        last_diff = row[0] - last_diff
    
    ans += last_diff

print(ans)
