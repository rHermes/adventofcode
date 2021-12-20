import fileinput as fi

all_ops = {}

def reg_op(func):
    """Decorator to add operator to all_ops table"""
    x, oname = func.__name__.split("_")
    assert(x == "op")
    assert(oname not in all_ops)
    all_ops[oname] = func

    return func


@reg_op
def op_addr(regs, a, b, c):
    regs[c] = regs[a] + regs[b]

@reg_op
def op_addi(regs, a, b, c):
    regs[c] = regs[a] + b

@reg_op
def op_mulr(regs, a, b, c):
    regs[c] = regs[a] * regs[b]

@reg_op
def op_muli(regs, a, b, c):
    regs[c] = regs[a] * b

@reg_op
def op_banr(regs, a, b, c):
    regs[c] = regs[a] & regs[b]

@reg_op
def op_bani(regs, a, b, c):
    regs[c] = regs[a] & b

@reg_op
def op_borr(regs, a, b, c):
    regs[c] = regs[a] | regs[b]

@reg_op
def op_bori(regs, a, b, c):
    regs[c] = regs[a] | b

@reg_op
def op_setr(regs, a, b, c):
    regs[c] = regs[a]

@reg_op
def op_seti(regs, a, b, c):
    regs[c] = a

@reg_op
def op_gtir(regs, a, b, c):
    regs[c] = int(regs[b] < a)

@reg_op
def op_gtri(regs, a, b, c):
    regs[c] = int(b < regs[a])

@reg_op
def op_gtrr(regs, a, b, c):
    regs[c] = int(regs[b] < regs[a])

@reg_op
def op_eqir(regs, a, b, c):
    regs[c] = int(a == regs[b])

@reg_op
def op_eqri(regs, a, b, c):
    regs[c] = int(regs[a] == b)

@reg_op
def op_eqrr(regs, a, b, c):
    regs[c] = int(regs[a] == regs[b])


def parse_case(case):
    lines = case.splitlines()
    ireg = [int(x) for x in lines[0][len("Before: ["):-1].split(", ")]
    code, a, b, c = map(int, lines[1].split())
    oreg = [int(x) for x in lines[2][len("After:  ["):-1].split(", ")]

    return ireg, (code, a, b, c), oreg


def pos_ops(ireg, oreg, a, b, c):
    pos = set()
    for nm, op in all_ops.items():
        regs = [x for x in ireg]
        try:
            op(regs, a, b, c)
            if regs == oreg:
                pos.add(nm)
        except IndexError:
            pass

    return pos


def solve(groups):
    mm = [set(all_ops.keys()) for _ in range(16)]
    known = {}

    for group in groups[:-2]:
        ireg, (code, a, b, c), oreg = parse_case(group)
        if code in known:
            continue

        pos = pos_ops(ireg, oreg, a, b, c)
        mm[code] &= pos

        if len(mm[code]) == 1:
            op = mm[code].pop()
            known[code] = op

            if len(known) == 16:
                break

            for v in mm:
                v.discard(op)


    regs = [0, 0, 0, 0]
    for line in groups[-1].splitlines():
        code, a, b, c = map(int, line.split())
        all_ops[known[code]](regs, a, b, c)

    return regs[0]


# Input parsing
INPUT = "".join(fi.input()).rstrip()
groups = INPUT.split("\n\n")
print(solve(groups))
