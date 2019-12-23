import fileinput
import itertools as it
from collections import defaultdict, deque
import threading
import queue
import time

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

def exec(ops, input_queue, output_queue):
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
            try:
                ins = input_queue.get(block=False)
            except:
                ins = -1

            ops[dst] = ins
            eip += 2
        
        elif bop == 4: # OUTPUT
            src, = get_params(ops, eip, base, 1)
            output_queue.put(src)
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

    N = 50

    qins = [queue.Queue() for _ in range(N)]
    qouts = [queue.Queue() for _ in range(N)]

    # Put in network ids
    for i in range(N):
        qins[i].put(i)

    threads = [threading.Thread(target=exec, args=(codes[:], qins[i], qouts[i])) for i in range(N)]

    for t in threads:
        t.start()

    while True:
        # Go through all things
        for q in qouts:
            if q.qsize() < 3:
                continue
            
            dst, x, y = q.get(), q.get(), q.get()

            if dst == 255:
                print("We got the first 255 packet: {}".format(y))
            else:
                print("activity")
                qins[dst].put(x)
                qins[dst].put(y)

        time.sleep(1/60)



for line in fileinput.input():
    print(solve(line.strip()))
