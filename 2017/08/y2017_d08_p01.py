import fileinput as fi
import collections
import operator

regs = collections.defaultdict(int)
ops = {
    "<": operator.lt,
    "<=": operator.le,
    "==": operator.eq,
    "!=": operator.ne,
    ">=": operator.ge,
    ">": operator.gt,
}

for line in map(str.rstrip, fi.input()):
    reg, op, delta, _, op1, rel, op2 = line.split(" ")
    if op == "inc":
        delta = int(delta)
    else:
        delta = -int(delta)

    if ops[rel](regs[op1], int(op2)):
        regs[reg] += delta

print(max(regs.values()))
