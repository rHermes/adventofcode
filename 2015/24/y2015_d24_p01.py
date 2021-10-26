import fileinput as fi
import itertools as it
import math

def powerset(iterable, k=0):
    s = list(iterable)
    return it.chain.from_iterable(it.combinations(s, r) for r in range(k, len(s) + 1))

def msolve(N, groups, min_len, rest):
    if groups <= 1:
        if sum(rest) != N or len(rest) < min_len:
            return None

        return math.prod(rest)

    for p in powerset(rest, min_len):
        if sum(p) != N:
            continue

        if msolve(N, groups - 1, len(p), rest - set(p)) is not None:
            return math.prod(p)

    return None


INPUT = "".join(fi.input()).rstrip()
packs = set(int(x) for x in INPUT.splitlines())

print(msolve(sum(packs)//3, 3, 0, packs))
