import fileinput as fi
import re
import collections as cs


cache = {}
def best(rates: dict[str,int], dists: dict[tuple[str,str],int], iremaining: int, eremaining: int, notdone: frozenset[str], inode: str, enode: str) -> int:
    global cache
    if (iremaining == 0 and eremaining == 0) or len(notdone) == 0:
        return 0
    
    if enode < inode:
        iremaining, eremaining = eremaining, iremaining
        inode, enode = enode, inode
    
    # I trust there will be no hash collitions, so I just store the hash values, to avoid memory growth
    hh = hash((iremaining, eremaining, notdone, inode, enode))
    if hh in cache:
        return cache[hh]

    ans = 0
    for ennode in notdone:
        cost = dists[(enode, ennode)]
        time_left_then = eremaining - cost -1
        if time_left_then < 1:
            continue


        ennode_rate = rates[ennode]
        nwdone = notdone - frozenset([ennode])
        sw = time_left_then * ennode_rate
        ans = max(ans, sw + best(rates, dists, iremaining, time_left_then, nwdone, inode, ennode))

    for innode in notdone:
        cost = dists[(inode, innode)]
        time_left_then = iremaining - cost -1
        if time_left_then < 1:
            continue


        innode_rate = rates[innode]
        nwdone = notdone - frozenset([innode])
        sw = time_left_then * innode_rate
        ans = max(ans, sw + best(rates, dists, time_left_then, eremaining, nwdone, innode, enode))


    cache[hh] = ans
    return ans


lines = fi.input()
def solve() -> int:
    # We build a fast way to see
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
                if dists[(i,j)] > dists[(i,k)] + dists[(k,j)]:
                    dists[(i,j)] = dists[(i,k)] + dists[(k,j)]

    notdone = frozenset(sorted(name for name, rate in rates.items() if rate != 0))
    return best(rates, dists, 26, 26, notdone, "AA", "AA")



print(solve())
