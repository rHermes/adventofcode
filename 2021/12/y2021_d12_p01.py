import fileinput as fi
import collections as cs

def solve(G: dict[str, set[str]], src: str, seen: frozenset[str]) -> int:
    pths = 0

    for w in G[src]:
        if w == "end":
            pths += 1
            continue

        nseen = seen
        if w[0].islower():
            if w in seen:
                continue
            nseen = seen.union([w])

        pths += solve(G, w, nseen)

    return pths


G = cs.defaultdict(set)
for line in map(str.rstrip, fi.input()):
    a, b = line.split("-")
    G[a].add(b)
    G[b].add(a)


print(solve(G, "start", frozenset(["start"])))
