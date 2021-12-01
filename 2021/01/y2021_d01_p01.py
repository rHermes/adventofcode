import fileinput as fi
import itertools as it

a, b = it.tee(map(int, fi.input()))
next(b, None)
print(sum(1 for x, y in zip(a, b) if x < y))
