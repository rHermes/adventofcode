import fileinput as fi
import itertools as it
import string

def grouper(iterable, n):
    "Collect data into non-overlapping fixed-length chunks or blocks"
    args = [iter(iterable)] * n
    return zip(*args, strict=True)

ans = 0
lines =  map(set, filter(bool, map(str.rstrip, fi.input())))
for a, b, c in grouper(lines, 3):
    ans += sum(string.ascii_letters.index(x) + 1 for x in a & b & c)

print(ans)
