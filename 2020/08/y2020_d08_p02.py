import fileinput

# Read in program
prog = []
for line in fileinput.input():
    if line.rstrip():
        op, arg = line.rstrip().split(" ")
        prog.append([op, int(arg)])

def does_terminate(prog):
    # By adding the one beyond to seen, we exit when needed
    seen = set([len(prog)])
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

    if ip == len(prog):
        return acc

# Map between instructions
M = {"jmp": "nop", "nop": "jmp"}

for (i, (op, arg)) in enumerate(prog):
    if op == "acc":
        continue

    prog[i][0] = M[op]
    ans = does_terminate(prog)
    prog[i][0] = M[M[op]]
    if ans:
        break

print(ans)
