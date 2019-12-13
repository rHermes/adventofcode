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

def exec(ops, inputs):
    #ops = [int(x) for x in s.split(",")]

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
            ins = inputs.pop(0)
            
            # ops[dst] = int(plane[(x,y)])

            eip += 2
        
        elif bop == 4: # OUTPUT
            src, = get_params(ops, eip, base, 1)
            outputs.append(src)
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

    
    return (ops, outputs)

def solve(s):
    codes = [int(x) for x in s.split(",")]
    ops, outs = exec(codes, [1])
    
    board = {}

    minx, miny = 10000000000000, 100000000000000
    maxx, maxy = -minx, -miny

    i = 0
    blocks = 0
    while i < len(outs):
        x, y, tile = outs[i], outs[i+1], outs[i+2]
        print("We have {} {} of type {}".format(x, y, tile))
        i += 3
        
        minx, miny = min(minx,x), min(miny,y)
        maxx, maxy = max(maxx,x), max(maxy,y)

        if tile == 0:
            board[(x,y)] = " "
        elif tile == 1:
            board[(x,y)] = "W"
        elif tile == 2:
            board[(x,y)] = "X"
            blocks += 1
        elif tile == 3:
            board[(x,y)] = "-"
        elif tile == 4:
            board[(x,y)] = "O"
        else:
            raise Exception("THIS IS AN ERROR")

    sss = ""
    
    for y in range(miny, maxy+1):
        for x in range(minx, maxx+1):
            sss += board[(x,y)]
        sss += "\n"
    
    return blocks
    # return outs

for line in fileinput.input():
    print(solve(line.strip()))
