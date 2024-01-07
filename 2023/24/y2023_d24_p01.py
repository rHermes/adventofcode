import fileinput as fi
import itertools as it
from fractions import Fraction

def convert(pos, vel):
    """This convert them over to standard (m, b) form"""
    px, py, _ = pos
    dx, dy, _ = vel

    x0s = Fraction(-px, dx)
    y0 = dy*x0s + py

    x1s = Fraction((1-px), dx)
    y1 = dy*x1s + py

    m = (y1-y0)
    b = y0

    return (m, b)


def collides(a, b, mmin=200000000000000, mmax=400000000000000):
    (apx, apy, _), (adx, ady, _), (ma, ba) = a
    (bpx, bpy, _), (bdx, bdy, _), (mb, bb) = b

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
