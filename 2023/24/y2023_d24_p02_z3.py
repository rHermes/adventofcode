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

for stone in stones:
    s = z3.FreshInt("s")
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

    dx = m[sx].as_long()
    dy = m[sy].as_long()
    dz = m[sz].as_long()

    dvx = m[svx].as_long()
    dvy = m[svy].as_long()
    dvz = m[svz].as_long()

    print(dx + dy + dz)
else:
    print("WTF")
