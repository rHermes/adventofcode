import fileinput as fi
import itertools as it

import z3

def collide(A, B, mini, maxi):
    (ax, ay, _), (avx, avy, _) = A
    (bx, by, _), (bvx, bvy, _) = B

    so = z3.Solver()
    s = z3.Real("s")
    t = z3.Real("t")

    AX = ax + avx*s
    AY = ay + avy*s

    BX = bx + bvx*t
    BY = by + bvy*t

    so.add(mini <= AX, AX <= maxi)
    so.add(mini <= AY, AY <= maxi)

    so.add(mini <= BX, BX <= maxi)
    so.add(mini <= BY, BY <= maxi)

    so.add(0 <= s)
    so.add(0 <= t)

    so.add(AX == BX, AY == BY)

    if so.check() == z3.sat:
        # print("It can be done")
        return True
    else:
        return False

stones = []
for line in fi.input():
    pre, pos = line.split(" @ ")
    pre = [int(x) for x in pre.split(", ")]
    pos = [int(x) for x in pos.split(", ")]
    stones.append((pre,pos))



# MINI = 7
MINI = 200000000000000
# MAXI = 27
MAXI = 400000000000000
ans = 0
for a, b in it.combinations(stones, 2):
    ans += collide(a, b, MINI, MAXI)

print(ans)
