import fileinput as fi
import collections

bots = collections.defaultdict(list)
insts = collections.defaultdict(list)

for line in map(str.rstrip, fi.input()):
    prts = line.split(" ")

    if line.startswith("value"):
        bots[int(prts[-1])].append(int(prts[1]))
    elif line.startswith("bot"):
        insts[int(prts[1])].append(" ".join(prts[2:]))

Q = [bot for bot, val in bots.items() if len(val) == 2]

ans = 1
while len(Q) > 0:
    bot = Q.pop()
    val = bots[bot]

    low, high = sorted(val)

    for inst in insts[bot]:
        thangs = inst.split(" ")

        lty, ln = thangs[3], int(thangs[4])
        rty, rn = thangs[8], int(thangs[9])

        if lty == "bot":
            bots[ln].append(low)
            if len(bots[ln]) == 2:
                Q.append(ln)

        if rty == "bot":
            bots[rn].append(high)
            if len(bots[rn]) == 2:
                Q.append(rn)

        if rty == "output" and rn in [0, 1, 2]:
            ans *= high

        if lty == "output" and ln in [0, 1, 2]:
            ans *= low

print(ans)
