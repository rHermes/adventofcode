import fileinput as fi

N = 65535

def solve(G, wire, cache):
    if wire.isnumeric():
        return int(wire)

    if wire in cache:
        return cache[wire]

    xs = G[wire]

    if len(xs) == 1:
        ans = solve(G, xs[0], cache)
    elif len(xs) == 2:
        ans = ~solve(G, xs[1], cache)
    elif len(xs) == 3:
        l, op, r = xs
        l = solve(G, l, cache)
        r = solve(G, r, cache)

        if op == "AND":
            ans = l & r
        elif op == "OR":
            ans = l | r
        elif op == "LSHIFT":
            ans = (l << r) & N
        elif op == "RSHIFT":
            ans = l >> r

    cache[wire] = ans
    return ans


rights = {}
for line in map(str.rstrip, fi.input()):
    l, r = line.split(" -> ")
    rights[r] = l.split(" ")

print(solve(rights, "a", {}))
