import fileinput

prog = []
for line in fileinput.input():
    op, arg = line.rstrip().split(" ")
    prog.append([op, int(arg)])

seen = set()
ip, acc = 0, 0
while ip not in seen:
    seen.add(ip)
    op, arg = prog[ip]

    if op == "acc":
        acc += arg
        ip += 1
    elif op == "nop":
        ip += 1
    elif op == "jmp":
        ip += arg
    else:
        raise Exception("WTF")

print(acc)
