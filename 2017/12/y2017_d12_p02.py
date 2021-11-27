import fileinput as fi
import collections

def solve(G, src):
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

G = {}
for line in map(str.rstrip, fi.input()):
    src, dsts = line.split(" <-> ")
    G[int(src)] = [int(x) for x in dsts.split(", ")]

not_seen = set(G.keys())

groups = 0
while len(not_seen) > 0:
    src = list(not_seen)[0]
    not_seen -= solve(G, src)
    groups += 1

print(groups)
