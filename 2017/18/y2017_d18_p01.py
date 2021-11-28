import fileinput as fi
import collections


def reg_or_val(regs, x):
    if x.isalpha():
        return regs[x]
    else:
        return int(x)


lines = list("".join(fi.input()).rstrip().splitlines())
regs = collections.defaultdict(int)

ans = 0
i = 0
while 0 <= i < len(lines):
    parts = lines[i].split(" ")
    if parts[0] == "snd":
        ans = reg_or_val(regs, parts[1])

    elif parts[0] == "rcv":
        if reg_or_val(regs, parts[1]) != 0:
            break

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

print(ans)
