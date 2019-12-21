import fileinput
import itertools as it
from collections import defaultdict, deque

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
            
            # We are reading inputs
            ins = inputs.pop(0)
            ops[dst] = ins
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

def find_prog(moves):
    # Now we need to find the 3 subs
    # Can have max 10 instructions with 10 commas
    MAX_N = 10
    a_off = 0
    for al in range(2,MAX_N):
        a = moves[a_off:a_off+al]
        # print(a)
        b_off = al
        while moves[b_off:b_off+al] == a:
            b_off += al

        for bl in range(2,MAX_N):
            b = moves[b_off:b_off+bl]
            if len(b) == 0:
                break

            # print(a, b)
            c_off = al+bl

            while moves[c_off:c_off+al] == a:
                c_off += al

            while moves[c_off:c_off+bl] == b:
                c_off += bl

            for cl in range(2, MAX_N):
                c = moves[c_off:c_off+cl]
                
                if len(c) == 0:
                    break
                
                
                xs = moves[:]
                main = []
                while len(xs):
                    match_a = len(xs[:al]) == len(a) and xs[:al] == a
                    match_b = len(xs[:bl]) == len(b) and xs[:bl] == b
                    match_c = len(xs[:cl]) == len(c) and xs[:cl] == c
                    
                    ss = match_a + match_b + match_c

                    if ss == 0:
                        break
                    elif ss > 1:
                        break
                    elif match_a:
                        # A
                        xs = xs[al:]
                        main.append("A")
                    elif match_b:
                        # B
                        xs = xs[bl:]
                        main.append("B")
                    elif match_c:
                        # C
                        xs = xs[cl:]
                        main.append("C")
                    else:
                        raise Exception("Should never happen!")
                else:
                    return (a, b, c, main)

def solve(s):
    codes = [int(x) for x in s.split(",")]
    _, outes = exec(codes[:], [])

    ox, oy, od = 0, 0, "N"
    world = set()
    x, y = 0, 0
    for m in outes:
        if m == 10:
            x = 0
            y += 1
        else:
            l = chr(m)
            if m != ord("."):
                world.add((x,y))
                if l in "^>v<":
                    ox, oy = x, y
                    od = {"^": "N", ">": "E", "v": "S", "<": "W"}[l]

            x += 1

    # Now we must just plot a course
    seen = set()
    seen.add((ox,oy))

    # print("We start at: {} facing {}".format((ox,oy), od))
    
    # From -> To
    trans = {
            "N": { "N": [], "E": ["R"], "S": ["R", "R"], "W": ["L"] },
            "E": { "E": [], "S": ["R"], "W": ["R", "R"], "N": ["L"] },
            "S": { "S": [], "W": ["R"], "N": ["R", "R"], "E": ["L"] },
            "W": { "W": [], "N": ["R"], "E": ["R", "R"], "S": ["L"] }
            }

    mvs = { "N": (0,-1), "E": (1,0), "S": (0,1), "W": (-1,0)}

    moves = []            
    while seen != world:
        left = world - seen

        # We assume that there is always just one way
        pts = [("S",(ox,oy+1)),("E", (ox+1,oy)),("N", (ox,oy-1)),("W", (ox-1,oy))]
        lpts = [p for p in pts if p[1] in left]
        if len(lpts) != 1:
            print("ERR: Moves: {}\nPos: {}".format(moves, lpts))
            return []

        d = lpts[0][0]

        moves.extend(trans[od][d])
        od = d
        
        dx, dy = mvs[od]

        c = 0
        while (ox+dx, oy+dy) in world:
            c += 1 
            ox += dx
            oy += dy
            seen.add((ox,oy))

        moves.append(str(c))

    # Now we need to find the 3 subs
    A, B, C, MAIN = find_prog(moves)
    
    # Create the input sequence
    insc = ",".join(MAIN) + "\n" + ",".join(A) + "\n" + ",".join(B) + "\n" + ",".join(C) + "\n" + "n" + "\n"
    ins = [ord(x) for x in insc]

    codes[0] = 2
    _, outes = exec(codes[:], ins)

    return outes[-1]

for line in fileinput.input():
    print(solve(line.strip()))
