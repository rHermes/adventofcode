import fileinput as fi

ops = [int(x.rstrip()) for x in fi.input()]
ins = 0

step = 0
while 0 <= ins < len(ops):
    aps = ops[ins]
    if aps >= 3:
        ops[ins] -= 1
    else:
        ops[ins] += 1

    ins += aps
    step += 1

print(step)
