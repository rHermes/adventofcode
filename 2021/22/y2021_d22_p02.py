import fileinput as fi
import re
import collections as cs

# This is heavily inspired by
# https://old.reddit.com/r/adventofcode/comments/rlxhmg/2021_day_22_solutions/hpizza8/
cubes = cs.Counter()

for line in fi.input():
    nsgn = line[1] == 'n'
    nx0, nx1, ny0, ny1, nz0, nz1 = map(int, re.findall("-?\d+", line))

    update = cs.Counter()
    for (ex0, ex1, ey0, ey1, ez0, ez1), esgn in cubes.items():
        ix0, ix1 = max(nx0, ex0), min(nx1, ex1)
        iy0, iy1 = max(ny0, ey0), min(ny1, ey1)
        iz0, iz1 = max(nz0, ez0), min(nz1, ez1)
        
        if ix0 <= ix1 and iy0 <= iy1 and iz0 <= iz1:
            update[(ix0, ix1, iy0, iy1, iz0, iz1)] -= esgn

        
    if nsgn:
        update[(nx0, nx1, ny0, ny1, nz0, nz1)] += 1

    cubes.update(update)

    for k in update.keys():
        if cubes[k] == 0:
            del cubes[k]



ans = 0
for (x0, x1, y0, y1, z0, z1), sgn in cubes.items():
    area = (x1-x0 + 1)*(y1-y0+1)*(z1-z0+1)*sgn
    ans += area

print(ans)
