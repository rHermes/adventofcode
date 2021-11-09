import fileinput as fi

INPUT = "".join(fi.input()).rstrip()
groups = INPUT.split("\n\n")
lines = [x.split() for x in INPUT.splitlines()]

ins = 0

regs = {"a": 0, "b": 0, "c": 1, "d": 0}

N = len(lines)
while ins < N:
    ops = lines[ins]
    # print(ins, regs, ops)

    if ops[0] == "cpy":
        x, y = ops[1], ops[2]
        if x.isnumeric():
            regs[y] = int(x)
        else:
            regs[y] = regs[x]

        ins += 1

    elif ops[0] == "inc":
        regs[ops[1]] += 1
        ins += 1
    elif ops[0] == "dec":
        regs[ops[1]] -= 1
        ins += 1
    elif ops[0] == "jnz":
        if ops[1].isnumeric():
            val = int(ops[1])
        else:
            val = regs[ops[1]]

        if val != 0:
            ins += int(ops[2])
        else:
            ins += 1

    else:
        raise Exception("SOMETHING MUST BE WRONG")



print(regs)


