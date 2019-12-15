import fileinput
import itertools as it
from collections import defaultdict, deque
import threading
import queue

import sys,tty,termios
class _Getch:
    def __call__(self):
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(3)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

def get_dir_key():
        inkey = _Getch()
        while(1):
                k=inkey()
                if k!='':break
        if k=='\x1b[A':
            return 2
        elif k=='\x1b[B':
            return 1
        elif k=='\x1b[C':
            return 4
        elif k=='\x1b[D':
            return 3
        else:
            raise Exception("Not an arrow key")


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
            ins = input_queue.get()
            if ins is None:
                return
            else:
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




def print_world(world, rx, ry):
    minx, miny = 100000000, 100000000000
    maxx, maxy = -minx, -miny

    for (x,y) in world.keys():
        minx, miny = min(minx, x), min(miny, y)
        maxx, maxy = max(maxx, x), max(maxy, y)

    if len(world.keys()) == 0:
        minx, miny = -10, -10
        maxx, maxy = 10, 10
    

    for y in range(miny,maxy+1):
        for x in range(minx,maxx+1):
            if (x,y) == (rx,ry):
                print("O", end="")
                continue

            print(world[(x,y)], end="")
        print()

def route_to(G, x, y, tx, ty):
    INF = 10000000000000000
    if (tx, ty) ==  (x,y):
        return []

    
    # dijekstras
    Q = set()
    dist = {}
    prev = {}

    for p in G.keys():
        dist[p] = INF
        prev[p] = None
        Q.add(p)

    dist[(x,y)] = 0

    while len(Q) > 0:
        u = None
        for v in Q:
            if u == None or dist[v] < dist[u]:
                u = v

        Q.remove(u)

        if u == (tx,ty):
            S = []
            while u is not None:
                S.insert(0,u)
                u = prev[u]

            dirs = {(0,1): 1, (0,-1): 2, (-1,0): 3, (1,0): 4}

            diff = [dirs[(x2-x1, y2-y1)] for (x1,y1),(x2,y2) in zip(S[:-1], S[1:])]

            # Now we need to confirm the thing
            return diff

        
        for v in G[u]:
            alt = dist[u] + 1
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u



    
    return dist


def deepest(G, ox, oy):
    INF = 10000000000000000
    dists = route_to(G, ox, oy, -100000000, -1000000000)
    
    deep = 0
    for k, v in dists.items():
        if v == INF:
            continue

        deep = max(deep, v)

    return deep 

def solve(s):
    codes = [int(x) for x in s.split(",")]

    q1 = queue.Queue()
    q2 = queue.Queue()

    t = threading.Thread(target=exec, args=(codes[:], q1, q2))
    t.start()

    x, y = 0, 0
    world = defaultdict(lambda: str("?"))

    dirs = {1: (0,1), 2: (0,-1), 3: (-1,0), 4:(1,0)}
    undirs = {1: 2, 2: 1, 3: 4, 4: 3}
    
    # In the graph we only have nice
    G = {(0,0): set()}

    explored = set()
    
    # We got to do a bootstrap for first node 
    targets = deque([(0,0)])

    ox, oy = None, None

    while len(targets):
        # Route to xx, send inputs
        # 
        # Read x outs
        #
        # do probe.

        tx, ty = targets.pop()

        # ROUTE
        ins = route_to(G, x, y, tx, ty)
        for l in ins:
            q1.put(l)

        for _ in ins:
            if q2.get() == 0:
                raise Exception("This should not happen")

        x, y = tx, ty
        
        # Now we need to probe
        for k in [1,2,3,4]:
            dx, dy = dirs[k]
            nx, ny = x + dx, y + dy
            q1.put(k)
            res = q2.get()

            if res == 0:
                world[(nx,ny)] = "█"
            elif res == 1:
                world[(nx,ny)] = " "

                if (nx,ny) not in explored:
                    targets.append((nx,ny))

                G[(x,y)].add((nx,ny))
                G[(nx,ny)] = G.get((nx,ny), set())
                G[(nx,ny)].add((x,y))
                
                # Go back
                q1.put(undirs[k])
                q2.get()

                # Now we must add the links
            elif res == 2:
                world[(nx,ny)] = "Æ"
                if (nx,ny) not in explored:
                    targets.append((nx,ny))

                G[(x,y)].add((nx,ny))
                G[(nx,ny)] = G.get((nx,ny), set())
                G[(nx,ny)].add((x,y))

                ox, oy = nx, ny
                
                # Go back
                q1.put(undirs[k])
                q2.get()

        explored.add((x,y))
        #print('\033c')
        #print_world(world, x, y)

    
    # To terminate bot
    q1.put(None)


    # dfs to find deepst
    return deepest(G, ox, oy)

    
    # THis is quite easy, we simply loop
    # maxt = 0
    # for (lx,ly) in G:
    #     rr = route_to(G, lx,ly, ox, oy)
    #     if len(rr) > maxt:
    #         maxt = len(rr)

    return maxt



for line in fileinput.input():
    print(solve(line.strip()))
