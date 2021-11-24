import fileinput as fi
import itertools as it
import heapq

def create_map(lines):
    m = []
    points = {}
    for y, line in enumerate(lines):
        row = []
        for x, c in enumerate(line):
            row.append(c != '#')

            if c not in '.#':
                points[int(c)] = (x,y)

        m.append(row)

    return (m, points)

def best_path(M, src, dst):
    f = lambda p: abs(dst[0] - p[0]) + abs(dst[1] - p[1])
    Q = [(0 + f(src), 0, src)]


    seen = set()
    while len(Q) > 0:
        _, depth, (px,py) = heapq.heappop(Q)
        if (px,py) == dst:
            return depth

        if (px,py) in seen:
            continue
        else:
            seen.add((px,py))

        for dx, dy in [(0,1), (0, -1), (1, 0), (-1, 0)]:
            tx, ty = px + dx, py + dy

            if M[ty][tx]:
                heapq.heappush(Q,(depth + 1 + f((tx,ty)), depth + 1, (tx,ty)))

def optimal_it(G, src, seen, cost=0):
    min_cost = 1000000000000000000000000
    min_pth = None
    for (a, b), dcost in G.items():
        if a != src or b in seen:
            continue

        ocost, opth = optimal_it(G, b, seen + (b,), cost=cost+dcost)
        if ocost < min_cost:
            min_cost = ocost
            min_pth = opth


    if min_pth is None:
        return cost, seen
    else:
        return min_cost, min_pth


M, points = create_map(map(str.rstrip, fi.input()))

G = {}
for (an, ap), (bn, bp) in it.combinations(points.items(), 2):
    bp = best_path(M, ap, bp)
    G[(an,bn)] = bp
    G[(bn,an)] = bp

print(optimal_it(G, 0, (0,))[0])
