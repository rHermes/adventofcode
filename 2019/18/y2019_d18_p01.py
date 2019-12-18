import fileinput
import collections


# Returns the route to a place
def route_to(G, src, dst):
    before = {}
    Q = collections.deque([src])
    seen = set([src])

    while len(Q) > 0:
        v = Q.popleft()

        if v == dst:
            # Here we found it. Now to construct a way back
            lst = [v]
            while lst[0] in before:
                lst.insert(0, before[lst[0]])

            return lst
        
        for u in G[v]:
            if u in seen:
                continue

            seen.add(u)
            before[u] = v
            Q.append(u)

    return []


hashs = {}
def solve(G, src, keys, doors, keys_done, level=0):
    hh = tuple(keys_done)
    h = (src, hh)
    if h in hashs:
        return hashs[h]

    # Find the doors we don't have access too
    needed_keys = set(keys.keys()) - keys_done
    locked_doors = set(doors.keys()) - set(x.upper() for x in keys_done)

    if len(needed_keys) == 0:
        return 0

    removed = {}
    for k, v in doors.items():
        if k in locked_doors:
            removed[k] = set(G[v])
            G[v] = set()

    pos = {}
    for k in needed_keys:
        pth = route_to(G, src, keys[k])
        if len(pth) > 0:
            # we need to do -1 because the first step is not a step len(pth) - 1
            pos[k] = len(pth) - 1
    
    # Fix up the removed stuff again
    for k, v in removed.items():
        G[doors[k]] = removed[k]

    # Now evaluate
    best = 100000000000000000000
    for k, v in pos.items():
        co = v + solve(G, keys[k], keys, doors, keys_done | set(k), level=level+1)
        best = min(best, co)
    
    hashs[h] = best
    if level < 11:
        print("We had a return from level: {}".format(level))
    return best

keys = {}
revkeys = {}
doors = {}
revdoors = {}
world = set()
px = None
py = None

y = 0
for y, line in enumerate(fileinput.input()):
    for x, c in enumerate(line.strip()):
        if c == "#":
            continue
        
        world.add((x,y))

        if c == ".":
            continue

        if c.isupper():
            doors[c] = (x,y)
            revdoors[(x,y)] = c
        elif c.islower():
            keys[c] = (x,y)
            revkeys[(x,y)] = c
        else:
            px, py = x, y

# Build the graph
G = {}

for (x,y) in world:
    # Check if there is one above it
    s = G.get((x,y), set())

    for p in [(x,y-1),(x+1,y),(x,y+1),(x-1,y)]:
        if p in world:
            s.add(p)
    
    G[(x,y)] = s


# Build a dependency graph
DG = {}

# Solve dependency graph
for k,v in keys.items():
    pth = route_to(G, (px, py), v)
    # Figure out which doors are gating
    blocking = []
    for st in pth:
        if st in revdoors:
            blocking.append(revdoors[st])

    DG[k] = set(blocking)

    # print("To key {}: {} and blocked by: {}".format(k, len(pth), blocking))

# print("digraph {")
# for k in keys.keys():
    # print("  {}".format(k.upper()))

# for k, v in DG.items():
    # for a in v:
    #     print("  {} -> {}".format(k.upper(), a))
# print("}")


    
print(solve(G, (px,py), keys, doors, set()))
