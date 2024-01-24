import fileinput as fi
import itertools as it

inp = fi.input()
next(inp); next(inp)

nodes = []
for line in inp:
    nam, sz, used, avail, use = [x for x in line.split(" ") if x]
    sz = int(sz[:-1])
    used = int(used[:-1])
    nodes.append((sz, used))


ans = 0
for (asz, aused), (bsz, bused) in it.combinations(nodes, 2):
    ans += aused != 0 and aused <= (bsz-bused)
    ans += bused != 0 and bused <= (asz-aused)

print(ans)
