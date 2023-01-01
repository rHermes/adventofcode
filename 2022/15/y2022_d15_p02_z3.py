import fileinput as fi
import re

import z3

# We need an abs for z3, so here it is
def myabs(x):
    return z3.If(x>=0, x, -x)

regex = re.compile(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)")

s = z3.Solver()
tx, ty = z3.Ints("tx ty")
maxb = 4000000

# Constraint the two variables to be within the range given in the task
s.add(0 <= tx, tx <= maxb)
s.add(0 <= ty, ty <= maxb)

# For each (sensor, beacon) pair, we add the constraint that the target
# location has to be further away from the sensor than the beacon is
for line in fi.input():
    m = re.match(regex, line)
    if not m:
        continue

    sx, sy, bx, by = map(int, m.groups())

    beacon_dist = abs(bx - sx) + abs(by - sy)
    distress_dist = myabs(tx - sx) + myabs(ty - sy)
    s.add(beacon_dist < distress_dist)

if s.check() == z3.sat:
    m = s.model()
    vx = m[tx].as_long()
    vy = m[ty].as_long()
    print(vx * 4000000 + vy)
else:
    print("The problem is not solvable")
