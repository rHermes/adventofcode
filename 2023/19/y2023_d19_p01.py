import fileinput as fi

# Input parsing
INPUT = "".join(fi.input()).rstrip()
groups = INPUT.split("\n\n")
lines = list(INPUT.splitlines())

workflows = {}
for line in groups[0].splitlines():
    line = line.rstrip()
    name, rr = line.split("{")
    rr = rr[:-1]
    chain = []
    for rv in rr.split(","):
        chain.append(rv)

    workflows[name] = chain

def valid(workflows, vals):
    beg = "in"

    while True:
        chain = workflows[beg]
        for line in chain:
            if ":" not in line:
                beg = line
                break

            cond, dest = line.split(":")
            if "<" in cond:
                reg, val = cond.split("<")
                bv = {"x": 0, "m": 1, "a": 2, "s": 3}
                ourval = vals[bv[reg]]
                if ourval < int(val):
                    beg = dest
                    break
            elif ">" in cond:
                reg, val = cond.split(">")
                bv = {"x": 0, "m": 1, "a": 2, "s": 3}
                ourval = vals[bv[reg]]
                if ourval > int(val):
                    beg = dest
                    break

        if beg == "R":
            return False
        elif beg == "A":
            return True

ans = 0
for line in groups[1].splitlines():
    line = line.rstrip()[1:-1]
    vals = []
    for k in line.split(","):
        _, v = k.split("=")
        vals.append(int(v))

    if valid(workflows, vals):
        ans += sum(vals)

print(ans)
