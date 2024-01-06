# This is an attempt to include a solution that would work fine during
# the competition, but which is not very good for post contest optimization.
#
# This solution simply picks random nodes and find the shortest path
# between them, and then count the edges used. We then assume that the
# three most used edges are the ones that split the graph.
#
# This is in no way guaranteed to be true, but for the contest it's super
# simple to implement and it's quite likely to give the right answer for
# if run 2-3 times.
import fileinput as fi
import collections as cs
import random
import itertools as it


def shortest_path(G, src, dst):
    seen = set()
    Q = cs.deque([(src, (src,))])
    while Q:
        cur, path = Q.popleft()

        if cur in seen:
            continue
        seen.add(cur)

        if cur == dst:
            return path

        for next in G[cur]:
            if next in seen:
                continue

            Q.append((next, path + (next,)))

    return None

def cluster_size(G, src):
    seen = set()
    Q = [src]
    while Q:
        cur = Q.pop()
        if cur in seen:
            continue
        seen.add(cur)

        for next in G[cur]:
            if next in seen:
                continue

            Q.append(next)

    return len(seen)


# Parse the input
G = cs.defaultdict(set)
for line in fi.input():
    src, *dsts = line.replace(":", "").split()
    for dst in dsts:
        G[src].add(dst)
        G[dst].add(src)

vertices = list(G)
edges = cs.Counter()
for _ in range(5000):
    src, dst = random.sample(vertices, 2)
    path = shortest_path(G, src, dst) or tuple()
    for a, b in it.pairwise(path):
        a, b = min(a,b), max(a,b)
        edges[(a,b)] += 1

for (a, b), _ in edges.most_common(3):
    G[a].remove(b)
    G[b].remove(a)

cluster_a_size = cluster_size(G, vertices[0])
cluster_b_size = len(vertices) - cluster_a_size
print(cluster_a_size * cluster_b_size)
