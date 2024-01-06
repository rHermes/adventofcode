# I found the description of this algorithm on the subreddit and it's so
# extremely beautiful, I want to describe it.
#
# It is built mainly on the fact that we know that the min-cut is 3 and
# we also know that there is only 1 such cut. The last one is a bit of
# an assumption, but for all inputs I've seen it's held true.
#
# With these two assumptions on the input, we know a few things. Each
# vertex is either part of group A or group B. Since there is only one
# min-cut of 3, it means that there is always at least 4 unique paths,
# unique meaning they share no edges, between any two nodes in the same
# group. It also means that if there is not 4 unique paths, then the two
# nodes must be in different groups.
#
# So what we can do is that we can pick out two random nodes, and try to
# find 4 unique paths. If we can do this, we know they are in the same group,
# and we pick out two new random nodes. If we cannot, then we know they are
# in two different groups.
#
# Once we know this, we can actually remove all the edges used by these 3
# paths. This splits the two groups A and B from each other, but it doesn't
# split either group, as each pair of nodes in a group has at least 4 unique
# paths between them. So as soon as we have separated the two groups, we can
# simply use a DFS to get the size of one of the groups. Once we know this
# size, we also know the size of the other group, and we have solved the
# task.
#
# We can actually improve the running time a bit, by not just choosing
# random pairs, but instead fixing the source node and iterating through
# the rest of the nodes randomly. We still want to shuffle the remaining
# nodes, as the input might have been sorted in some fashion. Once it's
# shuffled, we can look a bit at how many steps we might have to take.
#
# If SA is the size of group A, SB is the size of group B and N is SA + SB,
# then we have to look at the two possibilities. There is SA / N chance
# that the first node we picked is in. If this is the case, then for each
# iteration of the rest. We have a SB / (N - 1) chance of picking a node
# in group B. The chance of going n turns to not pick a node in group
# B is ((SA - 1) / (N - 1))^n
#
# The same is is true for if we pick a node in B first, just reversed.
# The overall probability that we make it to n rounds is:
#
# p(n) = 
#   (SA / N) * ((SA-1) / (N-1))^n
#   +
#   (1 - (SA / N)) * ((SB-1) / (N-1))^n
#
# Let's look at an example here, which is my input:
#
# SA = 796
# SB = 707
# N = 1503
#
# This gives us:
# p(n) = 0.5296 * 0.5293^n + 0.4704 * 0.47^n
#
# For some values of n we get:
#
# p(1)  = 0.5014
# p(2)  = 0.2523
# p(3)  = 0.1274
# p(4)  = 0.0645
# p(5)  = 0.0328
# p(6)  = 0.0167
# p(7)  = 0.0085
# p(8)  = 0.0044
# p(9)  = 0.0023
# p(10) = 0.0012
#
# This is a very good case where there is about an equal amount of elements
# in each group. As we see this approaches there is a 1% chance we even get
# to 6 iterations here, without hitting two different groups. Since each round
# runs so quickly, this means the algorithm is very very fast for this case.

import fileinput as fi
import collections as cs
import random
import itertools as it


def shortest_path(G, src, dst, banned):
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
            if (cur, next) in banned:
                continue

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


def solve(G):
    graph: dict[str, set[str]] = dict()
    for k, v in G.items():
        graph[k] = v

    nodes = list(G.keys())
    src = nodes.pop()
    random.shuffle(nodes)
    for dst in nodes:
        banned = set()
        paths = []

        for _ in range(4):
            path = shortest_path(G, src, dst, banned)
            if path is None:
                break

            paths.append(path)

            for a, b in it.pairwise(path):
                banned.add((a,b))
                banned.add((b,a))

        if len(paths) == 4:
            continue

        for a,b in banned:
            graph[a].discard(b)
            graph[b].discard(a)

        size_a = cluster_size(graph, src)
        size_b = len(nodes) + 1 - size_a
        return size_a * size_b


# Parse the input
G = cs.defaultdict(set)
for line in fi.input():
    src, *dsts = line.replace(":", "").split()
    for dst in dsts:
        G[src].add(dst)
        G[dst].add(src)

print(solve(G))
