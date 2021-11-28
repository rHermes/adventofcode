import fileinput as fi
import itertools as it


def fast_solve(S, f):
    ans = 0
    for d in S.keys():
        r = S[d]
        p = (d + f) % ((r-1)*2)
        if p == 0:
            return False

    return True


scanners = {}
for line in map(str.rstrip, fi.input()):
    a, b = map(int, line.split(": "))
    scanners[a] = b


for i in it.count():
    if fast_solve(scanners, i):
        break

print(i)
