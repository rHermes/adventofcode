import fileinput as fi
import itertools as it
import collections as cs
import re

# This is inspired by the awesome solution proposed by u/i_have_no_biscuits on
# the reddit mega thread: 
# https://old.reddit.com/r/adventofcode/comments/zmcn64/2022_day_15_solutions/j0b90nr/

regex = re.compile(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)")

maxb = 4000000


# For each (sensor, beacon) pair, we add the constraint that the target
# location has to be further away from the sensor than the beacon is
sensors: list[tuple[tuple[int,int],int]] = []
for line in fi.input():
    m = re.match(regex, line)
    if not m:
        continue

    sx, sy, bx, by = map(int, m.groups())

    beacon_dist = abs(bx - sx) + abs(by - sy)
    sensors.append(((sx,sy), beacon_dist))

down_coeffs = cs.defaultdict(int)
up_coeffs = cs.defaultdict(int)

for (sx,sy), r in sensors:
    down_coeffs[sy - sx + r + 1] += 1
    down_coeffs[sy - sx - r - 1] += 1

    up_coeffs[sy + sx - r - 1] += 1
    up_coeffs[sy + sx + r + 1] += 1

# We are only interested in coefficients which appear at least twice.
# The reason for this, is that we assume that the point is not on the edge
# of the area we are scanning. If it's in the middle of it, then it will
# need to be boxed in by at least two sensors for each axis. Since the sensors
# create a sort of rotated axis, it's easier to prove this if you tilt the
# axis, such that the sensors coverage areas are squares. If you play around
# a bit with this, it will be clear that if there is only 1 square that is to
# be free, then at least 2 sensors will need to share an "outer border" on each
# axis, to restrict it like that.

# This is not a good proof, but it's easier to just work it out by trying to box
# a single square in on paper, without having two sensors share an edge, given that
# the square we are looking for, is not on the border for the area.

# This brings the number of considerations down from 4224 to 25 for my input.
ups = {up for (up, times) in up_coeffs.items() if 1 < times}
downs = {down for (down, times) in down_coeffs.items() if 1 < times}

for up, down in it.product(ups, downs):
    # We skip points where the down coefficient is larger than the up up coefficient,
    # because the x coordinate of intersection point would be less than 0, which is
    # outside of our search area.
    #
    # We also skip the pairs where the delta is not an even number, because the
    # x coordinate of the intersection point would not be an integer.
    #
    # For my input, this brings the number of considerations down from
    # 4224 to 2880 without the filtering above, or from 25 to 20 with it.
    if up < down or (up - down) % 2 != 0:
        continue


    px = (up - down) // 2
    py = (up + down) // 2

    if 0 <= px <= maxb and 0 <= py <= maxb:
        if all(abs(px - sx) + abs(py - sy) > radius for ((sx,sy),radius) in sensors):
            print(maxb*px + py)
            break

