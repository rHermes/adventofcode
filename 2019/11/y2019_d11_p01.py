import fileinput
import itertools as it
from collections import defaultdict


def get_params(ops, eip, base, nargs, last_dst=False):
    op = ops[eip]
    ddd = ("{:0" + str(nargs+2) + "}").format(op)
    parms = list(reversed([int(x) for x in ddd[:-2]]))

    if last_dst and parms[-1] == 1:
        raise Exception("With last destination, you cannot have an intermedite value")

    outs = []
    for i, x in enumerate(parms):
        a = ops[eip+1+i]
        if x == 0:
            if last_dst and i == (len(parms)-1):
                outs.append(a)
            else:
                outs.append(ops[a])
        elif x == 1:
            outs.append(a)
        elif x == 2:
            if last_dst and i == (len(parms)-1):
                outs.append(a+base)
            else:
                outs.append(ops[a+base])
        else:
            raise Exception("Not a valid instruction")

    return outs

def exec(ops):
    #ops = [int(x) for x in s.split(",")]

    panels = set()
    plane = defaultdict(bool)
    direction = "N"
    x, y = 0, 0
    trans = {
            "N": {0: "W", 1: "E"},
            "E": {0: "N", 1: "S"},
            "S": {0: "E", 1: "W"},
            "W": {0: "S", 1: "N"}
            }
    mov = {
            "N": (0,1),
            "E": (1,0),
            "S": (0,-1),
            "W": (-1,0)
            }

    phase = 0
    
    mops = defaultdict(int)

    for i, x in enumerate(ops):
        mops[i] = x

    ops = mops

    outputs = []
    eip = 0
    base = 0
    while True:
        op = ops[eip]
        bop = op % 100

        if bop == 1: # ADD 
            a, b, dst = get_params(ops, eip, base, 3, last_dst=True)
            ops[dst] = a + b
            eip += 4

        elif bop == 2: # MULT
            a, b, dst = get_params(ops, eip, base, 3, last_dst=True)
            ops[dst] = a * b
            eip += 4

        elif bop == 3: # INPUT
            dst, = get_params(ops, eip, base, 1, last_dst=True)
            
            # We are faking the input
            #ins = inputs.pop(0)
            
            ops[dst] = int(plane[(x,y)])

            eip += 2
        
        elif bop == 4: # OUTPUT
            src, = get_params(ops, eip, base, 1)
            outputs.append(src)
            if phase == 0:
                phase = 1
                panels.add((x,y))
                plane[(x,y)] = bool(src)
            else:
                direction = trans[direction][src]
                dx,dy = mov[direction]
                x, y = x + dx, y + dy
                phase = 0

            eip += 2

        elif bop == 5: # JT
            a, b = get_params(ops, eip, base, 2)

            if a != 0:
                eip = b
            else:
                eip += 3

        elif bop == 6: # JF
            a, b = get_params(ops, eip, base, 2)

            if a == 0:
                eip = b
            else:
                eip += 3

        elif bop == 7: # LT
            a, b, dst = get_params(ops, eip, base, 3, last_dst=True)
            ops[dst] = int(a < b)
            eip += 4

        elif bop == 8: # EQ
            a, b, dst = get_params(ops, eip, base, 3, last_dst=True)
            ops[dst] = int(a == b)
            eip += 4

        elif bop == 9: # BASE
            a, = get_params(ops, eip, base, 1)
            base += a
            eip += 2

        elif bop == 99:
            break
        else:
            raise Exception("Unkown op: {}".format(op))

    
    return (ops, outputs, len(panels))

def solve(s):
    codes = [int(x) for x in s.split(",")]
    ops, outs, panels = exec(codes)
    return panels

for line in fileinput.input():
    print(solve(line.strip()))
