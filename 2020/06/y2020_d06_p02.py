import fileinput


grps = []
ans = 0
cur = set()
for line in fileinput.input():
    line = line.rstrip()

    if line == "":
        wc = grps[0]
        for k in grps[1:]:
            wc = wc & k
        ans += len(wc)
        grps = []
    else:
        cu = set(line)
        grps.append(cu)
        # for c in line:
        #     cur.add(c)

wc = grps[0]
for k in grps[1:]:
    wc = wc & k
ans += len(wc)

print(ans)


