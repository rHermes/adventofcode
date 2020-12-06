import fileinput


grps = []
ans = 0
cur = set()
for line in fileinput.input():
    line = line.rstrip()

    if line == "":
        ans += len(cur)
        cur.clear()
    else:
        for c in line:
            cur.add(c)

ans += len(cur)

print(ans)


