import fileinput as fi
import itertools as it
import copy

# Input parsing
INPUT = "".join(fi.input()).rstrip()
groups = INPUT.split("\n\n")
lines = [x.split() for x in INPUT.splitlines()]

def perform(ilines, a_state):
    # lines = copy.deepcopy(ilines)
    lines = ilines

    ins = 0
    regs = {"a": a_state, "b": 0, "c": 0, "d": 0}

    N = len(lines)
    steps = 0
    while 0 <= ins < N:
        if steps+1 % 10000000 == 0:
            print("Step {}: {} {}".format(steps, ins, regs))

        steps += 1

        ops = lines[ins]
        # print(ops)
        # print(ins, regs, ops)

        if ops[0] == "cpy":
            x, y = ops[1], ops[2]
            if y not in "abcd":
                print("SKIPPED")
                print(ops)
                ins += 1
                continue

            if x not in "abcd":
                regs[y] = int(x)
            else:
                regs[y] = regs[x]

            ins += 1

        elif ops[0] == "inc":
            if ops[1] not in "abcd":
                print("SKIPPED")
                ins += 1
                continue

            regs[ops[1]] += 1
            ins += 1
        elif ops[0] == "dec":
            if ops[1] not in "abcd":
                print("SKIPPED")
                ins += 1
                continue

            regs[ops[1]] -= 1
            ins += 1
        elif ops[0] == "jnz":
            if ops[1] not in "abcd":
                val = int(ops[1])
            else:
                val = regs[ops[1]]

            if ops[2] not in "abcd":
                jval = int(ops[2])
            else:
                jval = regs[ops[2]]

            if val != 0:
                ins += jval
            else:
                ins += 1
        elif ops[0] == "tgl":
            if ops[1] not in "abcd":
                val = int(ops[1])
            else:
                val = regs[ops[1]]

            if ins + val >= N or ins + val < 0:
                print("WTF")
                pass
            else:
                oops = lines[ins+val]
                if len(oops) == 2:
                    if oops[0] == "inc":
                        oops[0] = "dec"
                    else:
                        oops[0] = "inc"
                elif len(oops) == 3:
                    if oops[0] == "jnz":
                        oops[0] = "cpy"
                    else:
                        oops[0] = "jnz"
                else:
                    raise Exception("WTF!!")

            ins += 1
        elif ops[0] == "out":
            if ops[1] not in "abcd":
                val = int(ops[1])
            else:
                val = regs[ops[1]]

            yield val
            ins += 1

        else:
            print(ops)
            raise Exception("SOMETHING MUST BE WRONG")


for x in it.count():
    gen = perform(lines, x)
    for expt, act, cnt in zip(it.cycle((0,1)), gen, it.count()):
        if expt != act:
            break

        if cnt > 100:
            break

    if cnt > 100:
        print(x)
        break
