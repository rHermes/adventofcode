import fileinput as fi
import re

regex = re.compile(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)")

maxb = 4000000

# Constraint the two variables to be within the range given in the task
# s.add(0 <= tx, tx <= maxb)
# s.add(0 <= ty, ty <= maxb)

sensors = []

# For each (sensor, beacon) pair, we add the constraint that the target
# location has to be further away from the sensor than the beacon is
for line in fi.input():
    m = re.match(regex, line)
    if not m:
        continue

    sx, sy, bx, by = map(int, m.groups())

    beacon_dist = abs(bx - sx) + abs(by - sy)
    sensors.append(((sx,sy), beacon_dist))


for y in range(maxb+1):
# for y in range(0, maxb+1):
    # Let's build the ranges here:
    ranges = []
    for (sx,sy), dst in sensors:
            remaining = dst - abs(y - sy)
            if remaining < 0:
                continue

            minx = sx - remaining
            maxx = sx + remaining
            ranges.append((minx,maxx))

    sr = sorted(ranges)

    merged = [sr.pop(0)]
    for (cur_start, cur_end) in sr:
        top_start, top_end = merged[-1]
        if top_end < cur_start:
            merged.append((cur_start,cur_end))
        elif top_end < cur_end:
            merged[-1] = (top_start, cur_end)
    
    if 1 < len(merged):
        assert(len(merged) == 2)
        x = merged[0][1] + 1
        print(x * 4000000 + y)
        break
    else:
        minx, maxx = merged[0]
        if 0 < minx:
            print(y)
            break
        elif maxx < maxb:
            print(maxb * 4000000 + y)
            break
