import fileinput as fi

pos = {}
for line in map(str.rstrip, fi.input()):
    a, b = line.split(" (contains ")
    foods = set(a.split())
    algs = set(b[:-1].split(", "))

    for alg in algs:
        if alg not in pos:
            pos[alg] = foods.copy()
        else:
            pos[alg] &= foods


taken = set()
items = []
while True:
    for alg, foods in pos.items():
        if len(foods - taken) == 1:
            o = min(foods-taken)
            items.append((alg,o))
            taken.add(o)
            break
    else:
        break

print(",".join(x[1] for x in sorted(items)))
