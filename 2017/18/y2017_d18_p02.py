import fileinput as fi
import collections

def reg_or_val(regs, x):
    if x.isalpha():
        return regs[x]
    else:
        return int(x)

def single_run(lines, regs, i, ins):
    while 0 <= i < len(lines):
        parts = lines[i].split(" ")
        if parts[0] == "snd":
            val = reg_or_val(regs, parts[1])
            i += 1
            return regs, i, ins, val, True

        elif parts[0] == "rcv":
            if len(ins) == 0:
                return regs, i, ins, None, True

            regs[parts[1]] = ins.pop(0)

        elif parts[0] == "set":
            regs[parts[1]] = reg_or_val(regs, parts[2])

        elif parts[0] == "add":
            regs[parts[1]] = regs[parts[1]] + reg_or_val(regs, parts[2])

        elif parts[0] == "mul":
            regs[parts[1]] = regs[parts[1]] * reg_or_val(regs, parts[2])

        elif parts[0] == "mod":
            regs[parts[1]] = regs[parts[1]] % reg_or_val(regs, parts[2])

        elif parts[0] == "jgz":
            if 0 < reg_or_val(regs, parts[1]):
                i += reg_or_val(regs, parts[2])
                continue
        else:
            raise Exception("Unknown operator: {}".format(parts[0]))

        i += 1

    return regs, i, ins, None, False

def solve(lines):
    a_regs = collections.defaultdict(int)
    a_regs["p"] = 0
    a_ip = 0
    a_ins = []
    a_running = True
    a_waiting = False

    b_regs = collections.defaultdict(int)
    b_regs["p"] = 1
    b_ip = 0
    b_ins = []
    b_running = True
    b_waiting = False

    ans = 0
    while (a_running or b_running) and not (b_waiting and a_waiting):
        if a_running:
            a_regs, a_ip, a_ins, a_out, a_running = single_run(lines, a_regs, a_ip, a_ins)
            if a_out is not None:
                b_ins.append(a_out)
            else:
                a_waiting = a_running

        if b_running:
            b_regs, b_ip, b_ins, b_out, b_running = single_run(lines, b_regs, b_ip, b_ins)
            if b_out is not None:
                ans += 1
                a_ins.append(b_out)
            else:
                b_waiting = b_running

    return ans

# Input parsing
lines = list("".join(fi.input()).rstrip().splitlines())

print(solve(lines))
