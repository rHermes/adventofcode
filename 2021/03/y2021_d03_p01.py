import fileinput as fi

x = None
for line in map(str.rstrip, fi.input()):
    if x is None:
        x = [[0,0] for _ in range(len(line))]

    for i, c in enumerate(line):
        x[i][int(c)] += 1

gamma = "".join("01"[a < b] for a,b in x)
print(int(gamma, 2) * int(gamma.translate(str.maketrans("01", "10")), 2))
