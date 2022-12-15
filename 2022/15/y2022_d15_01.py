import fileinput as fi
import re


regex = re.compile(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)")

cannot = set()
beacons = set()

ty = 2000000
for line in fi.input():
    m = re.match(regex, line)
    if not m:
        continue

    sx, sy, bx, by = map(int, m.groups())

    beacon_dist = abs(bx - sx) + abs(by - sy)
    if by == ty:
        beacons.add(bx)
   
    # This is how many steps we have remaining, which is also how many on each
    # side we have remaining, which cannot be our beacon.
    remaining = beacon_dist - abs(ty - sy)
    for x in range(-remaining,remaining+1):
        cannot.add(sx + x)

# Print the length of the cannots versus the beacons
print(len(cannot - beacons))
