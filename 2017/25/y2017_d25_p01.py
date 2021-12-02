import fileinput as fi
import collections

def parse_header(header):
    hd = header.split("\n")
    start_state = hd[0].split(" ")[-1][:-1]
    goal = int(hd[1].split(" ")[-2])
    return start_state, goal

def parse_state(group):
    lines = [x.strip().split(" ") for x in group.split("\n")]

    name = lines[0][-1][:-1]
    for i in range(1, len(lines), 4):
        cval = lines[i][-1] == "1:"
        write = lines[i+1][-1] == "1."
        dx = {"right.": 1, "left.": -1}[lines[i+2][-1]]
        nx = lines[i+3][-1][:-1]

        if cval:
            rr = (write, dx, nx)
        else:
            ff = (write, dx, nx)

    return (name, ff, rr)

# Input parsing
INPUT = "".join(fi.input()).rstrip()
groups = INPUT.split("\n\n")

states = {}
for grp in groups[1:]:
    name, ff, rr = parse_state(grp)
    states[name] = (ff, rr)

tape = collections.defaultdict(bool)
state, goal = parse_header(groups[0])
c = 0

for _ in range(goal):
    tape[c], dx, state = states[state][tape[c]]
    c += dx

print(sum(tape.values()))
