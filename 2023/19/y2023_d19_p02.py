import fileinput as fi


def evalt(workflows, rest, beg="in"):
    minx, maxx, minm, maxm, mina, maxa, mins, maxs = rest

    # If any of these overlap, we are not good
    if maxx <= minx or maxm <= minm or maxa <= mina or maxs <= mins:
        print("We hot")
        return []

    if beg == "R":
        return []

    if beg == "A":
        return [rest]

    rst = {
            "x": (minx, maxx),
            "m": (minm, maxm),
            "a": (mina, maxa),
            "s": (mins, maxs)
        }

    # print(beg)
    pos = []

    chain = workflows[beg]

    for line in chain:
        if ":" not in line:
            gvs = (*rst["x"], *rst["m"], *rst["a"], *rst["s"])
            pos.extend(evalt(workflows, gvs, beg=line))
            continue


        cond, dest = line.split(":")
        if "<" in cond:
            reg, val = cond.split("<")
            val = int(val)

            gmin, gmax = rst[reg]
            rst[reg] = (gmin, min(gmax, val))
            gvs = (*rst["x"], *rst["m"], *rst["a"], *rst["s"])
            pos.extend(evalt(workflows, gvs, beg=dest))

            rst[reg] = (max(gmin,val-1), gmax)
        elif ">" in cond:
            reg, val = cond.split(">")
            val = int(val)

            gmin, gmax = rst[reg]
            rst[reg] = (max(gmin, val), gmax)
            gvs = (*rst["x"], *rst["m"], *rst["a"], *rst["s"])
            pos.extend(evalt(workflows, gvs, beg=dest))

            rst[reg] = (gmin, min(gmax, val+1))



    return pos

# Parse workflows
workflows = {}
for line in map(str.rstrip, fi.input()):
    if not line:
        break

    name, rr = line.split("{")
    rr = rr[:-1]
    chain = []
    for rv in rr.split(","):
        chain.append(rv)

    workflows[name] = chain

NG = 4000
goods = evalt(workflows, (0, NG+1, 0, NG+1, 0, NG+1, 0, NG+1))
ans = 0
for minx, maxx, minm, maxm, mina, maxa, mins, maxs in goods:
    ans += (maxx - minx - 1) * (maxm - minm - 1) * (maxa - mina - 1) * (maxs - mins - 1)

print(ans)
