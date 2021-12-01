import fileinput as fi
import itertools as it

a, b = it.tee(map(int, fi.input()))
print(sum(1 for x, y in zip(a, it.islice(b, 3, None)) if x < y))
