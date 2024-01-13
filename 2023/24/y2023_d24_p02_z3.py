import fileinput as fi
import itertools as it

import z3
stones = []
for line in fi.input():
    pre, pos = line.split(" @ ")
    pre = [int(x) for x in pre.split(", ")]
    pos = [int(x) for x in pos.split(", ")]
    stones.append((pre,pos))

so = z3.Solver()
sx, sy, sz = z3.Ints("sx sy sz")
svx, svy, svz = z3.Ints("svx svy svz")

ses = []
for stone in stones:
    s = z3.FreshInt("s")
    ses.append(s)
    so.add(0 < s)
    (ax, ay, az), (avx, avy, avz) = stone
    so.add(
        ax + s*avx == sx + s*svx,
        ay + s*avy == sy + s*svy,
        az + s*avz == sz + s*svz
    )

if so.check() == z3.sat:
    m = so.model()
    # print(m)
    print(m[sx])
    print(m[sy])
    print(m[sz])

    dx = m[sx].as_long()
    dy = m[sy].as_long()
    dz = m[sz].as_long()

    print(m[svx])
    print(m[svy])
    print(m[svz])
    print("")

    dvx = m[svx].as_long()
    dvy = m[svy].as_long()
    dvz = m[svz].as_long()
    # k = [m[s].as_long() for s in ses]
    # k.sort()
    # print(k)
    # print([b-a for a,b in it.pairwise(k)])

    print(dx + dy + dz)
else:
    print("WTF")
