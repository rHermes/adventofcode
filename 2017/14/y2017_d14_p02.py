import fileinput as fi
import itertools as it
import functools as ft
import collections
import operator

import more_itertools as mit

def knot_hash(ins, ar, cur, skip):
    for l in ins:
        ar[:l] = ar[:l][::-1]
        bw = collections.deque(ar)
        bw.rotate(-(l + skip))
        cur += l + skip
        ar = list(bw)
        skip += 1

    return ar, cur, skip

def kn(inp):
    cur = 0
    skip = 0
    anp = [ord(x) for x in inp] + [17, 31, 73, 47, 23]

    ar = list(range(256))
    for i in range(64):
        ar, cur, skip = knot_hash(anp, ar, cur, skip)

    bw = collections.deque(ar)
    bw.rotate(cur)
    ar = list(bw)

    dense_hash = (ft.reduce(operator.xor, g) for g in mit.chunked(ar, 16, strict=True))
    return "".join(map("{:08b}".format, dense_hash))


def find_group(G, src):
    Q = collections.deque([src])
    seen = set()

    while len(Q) > 0:
        w = Q.popleft()
        if w in seen:
            continue
        else:
            seen.add(w)

        for x in G[w]:
            Q.append(x)

    return seen

def solve(inp):
    grid = [kn("{}-{}".format(inp, x)) for x in range(128)]

    G = {}
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == "0":
                continue

            deltas = []
            if 0 < x:
                deltas.append((-1, 0))
            if x < (len(row)-1):
                deltas.append((1, 0))

            if 0 < y:
                deltas.append((0, -1))
            if y < (len(grid)-1):
                deltas.append((0, 1))

            neigh = []
            for dx, dy in deltas:
                tx, ty = x + dx, y + dy
                if grid[ty][tx] == "1":
                    neigh.append((tx,ty))

            G[(x,y)] = neigh


    not_seen = set(G.keys())

    groups = 0
    while len(not_seen) > 0:
        src = list(not_seen)[0]
        not_seen -= find_group(G, src)
        groups += 1

    return groups


print(solve(next(fi.input()).rstrip()))
