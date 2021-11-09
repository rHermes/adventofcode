import fileinput as fi

INPUT = "".join(fi.input()).rstrip()
lines = list(INPUT.splitlines())

def gen_cpy(x, y):
    if x.isnumeric():
        x = int(x)
        def g(s):
            s[y] = x
            s["ins"] += 1
        return g
    else:
        def g(s):
            s[y] = s[x]
            s["ins"] += 1
        return g

def gen_inc(reg, inc=True):
    if inc:
        def g(s):
            s[reg] += 1
            s["ins"] += 1
        return g
    else:
        def g(s):
            s[reg] -= 1
            s["ins"] += 1
        return g

def gen_jnz(x, y):
    y = int(y)
    if x.isnumeric():
        if int(x) == 0:
            y = 1

        def g(s):
            s["ins"] += y

        return g
    else:
        def g(s):
            if s[x] != 0:
                s["ins"] += y
            else:
                s["ins"] += 1
        return g


# convert lines to program
opers = []
for line in lines:
    op, *args = line.split()
    if op == "inc":
        opers.append(gen_inc(args[0]))
    elif op == "dec":
        opers.append(gen_inc(args[0], inc=False))
    elif op == "cpy":
        opers.append(gen_cpy(*args))
    elif op == "jnz":
        opers.append(gen_jnz(*args))
    else:
        raise Exception("Something is wrong here")



state = {"a": 0, "b": 0, "c": 1, "d": 0, "ins": 0}
N = len(lines)
while state["ins"] < N:
    opers[state["ins"]](state)

print(state["a"])
