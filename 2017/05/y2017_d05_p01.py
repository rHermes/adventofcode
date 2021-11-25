import fileinput as fi

ops = [int(x.rstrip()) for x in fi.input()]
ins = 0

step = 0
while 0 <= ins < len(ops):
    ops[ins] += 1
    ins += ops[ins] - 1
    step += 1

print(step)
