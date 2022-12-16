import fileinput as fi
import re
import collections as cs


cache = {}
def best(rates: dict[str,int], dists: dict[tuple[str,str],int], remaining: int,  notdone: frozenset[str], node: str) -> int:
    global cache
    if remaining == 0 or len(notdone) == 0:
        return 0
    
    
    # I trust there will be no hash collitions, so I just store the hash values, to avoid memory growth
    hh = hash((remaining, notdone, node))
    if hh in cache:
        return cache[hh]

    ans = 0
    for next_node in notdone:
        cost = dists[(node, next_node)]
        time_left_then = remaining - cost -1
        if time_left_then < 1:
            continue


        next_node_rate = rates[next_node]
        nwdone = notdone - frozenset([next_node])
        sw = time_left_then * next_node_rate
        ans = max(ans, sw + best(rates, dists, time_left_then, nwdone, next_node))

    cache[hh] = ans
    return ans


lines = fi.input()
def solve() -> int:
    dists = cs.defaultdict(lambda: 10000000000000)
    rates = {}
    for line in lines:
        m = re.match(r"Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? ((?:[A-Z][A-Z], )*[A-Z][A-Z])", line)
        if not m:
            continue
        name, rate, leads = m.groups()
        rates[name] = int(rate)

        dists[(name,name)] = 0
        for lead in leads.split(", "):
            dists[(name,lead)] = 1

    
    # Calculate the shortest distance between all paths
    ks = list(rates.keys())
    for k in ks:
        for i in ks:
            for j in ks:
                if dists[(i,k)] + dists[(k,j)] < dists[(i,j)]:
                    dists[(i,j)] = dists[(i,k)] + dists[(k,j)]
    
    notdone = frozenset(sorted(name for name, rate in rates.items() if rate != 0))
    return best(rates, dists, 30, notdone, "AA")



print(solve())
