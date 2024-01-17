# The idea here is to convert each hailstone into a 2d line and then
# do standard intersection on them. By removing the time aspect of the
# hailstones, we are able to do the intersections faster. We use fractions
# to avoid floating point issues.
import fileinput as fi
import itertools as it

# For a free 2-3x speedup switch this out with cfractions
try:
    from cfractions import Fraction
except ImportError as e:
    from fractions import Fraction

def convert(pos, vel):
    """This convert them over to standard (m, b) form"""
    px, py, _ = pos
    dx, dy, _ = vel

    # We just pick two easy points, s = 0 and s = 1
    x0, y0 = px, py
    x1, y1 = px + dx, py + dy

    return (
        Fraction(y1 - y0, x1 - x0),
        Fraction(x1*y0 - x0*y1, x1 - x0)
    )


def collides(a, b, mmin=200000000000000, mmax=400000000000000):
    (apx, _, _), (adx, _, _), (ma, ba) = a
    (bpx, _, _), (bdx, _, _), (mb, bb) = b

    nom = bb - ba
    dem = ma - mb
    if dem == 0:
        return bb == ba

    cx = nom / dem
    cy = ma * cx + ba
    at = (cx - apx) / adx
    bt = (cx - bpx) / bdx

    return 0 <= at and 0 <= bt and (mmin <= cx <= mmax) and (mmin <= cy <= mmax)

lines = []
for line in fi.input():
    pos, vel = line.split(" @ ")
    pos = tuple(int(x) for x in pos.split(", "))
    vel = tuple(int(x) for x in vel.split(", "))
    lines.append((pos, vel, convert(pos, vel)))

ans = 0
for first, sec in it.combinations(lines, 2):
    ans += collides(first, sec)

print(ans)
