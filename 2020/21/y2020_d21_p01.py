import fileinput as fi
from collections import Counter
import itertools as it

all_foods = set()
times = Counter()

pos = {}
for line in map(str.rstrip, fi.input()):
    a, b = line.split(" (contains ")
    foods = set(a.split())
    algs = set(b[:-1].split(", "))

    all_foods |= foods
    times.update(foods)

    for alg in algs:
        if alg not in pos:
            pos[alg] = foods.copy()
        else:
            pos[alg] &= foods

bad = set(it.chain.from_iterable(pos.values()))

print(sum(times[food] for food in (all_foods - bad)))
