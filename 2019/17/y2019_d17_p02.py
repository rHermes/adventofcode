import fileinput
import itertools as it
from collections import defaultdict, deque
import threading
import queue
import time

import z3

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


    print("Target was {}".format((tx,ty)))
    raise Exception("We should never reach this")

MAX_NUM = 20

Direction, (NORTH, EAST, SOUTH, WEST) = z3.EnumSort("Direction", ["NORTH", "EAST", "SOUTH", "WEST"])

Point = z3.Datatype("Point")
Point.declare("cons", ("x", z3.IntSort()), ("y", z3.IntSort()))
Point = Point.create()

Robot = z3.Datatype("Robot")
Robot.declare('cons', ('p', Point), ('d', Direction), ('seen', z3.SetSort(Point)))
Robot = Robot.create()

def insts_to_str(insts):
    s = z3.StringVal("")
    first = True
    for inst in insts:
        k = z3.If(inst == z3.StringVal(""), z3.StringVal(""), z3.StringVal(","))
        if first:
            first = False 
            s += inst 
        else:
            s += k + inst

    return s
    

def must_follow(insts):
    st = []
    for (b,a) in zip(insts[1:], insts[:-1]):
        # if b then a
        st.append(z3.Implies(b != z3.StringVal(""), a != z3.StringVal("")))
        st.append(z3.Implies(b == z3.StringVal("L"), a != z3.StringVal("R")))
        st.append(z3.Implies(b == z3.StringVal("R"), a != z3.StringVal("L")))
    for (b,a) in zip(insts[1:], insts[:-1]):
        # if b then a
        st.append(z3.Implies(b != z3.StringVal(""), a != z3.StringVal("")))
        st.append(z3.Implies(b == z3.StringVal("L"), a != z3.StringVal("R")))
        st.append(z3.Implies(b == z3.StringVal("R"), a != z3.StringVal("L")))

    return z3.And(*st)


def must_be_in_set(insts, e_set):
    st = []
    for x in insts:
        st.append(z3.Implies(x != z3.StringVal(""), z3.IsMember(x, e_set)))

    return z3.And(*st)


# Turns the robot
def eval_rotate_robo(r, inst):
    d = Robot.d(r)

    lturn = z3.If(d == NORTH, WEST, d)
    lturn = z3.If(d == EAST, NORTH, lturn)
    lturn = z3.If(d == SOUTH, EAST, lturn)
    lturn = z3.If(d == WEST, SOUTH, lturn)

    rturn = z3.If(d == NORTH, EAST, d)
    rturn = z3.If(d == EAST, SOUTH, rturn)
    rturn = z3.If(d == SOUTH, WEST, rturn)
    rturn = z3.If(d == WEST, NORTH, rturn)

    turn = z3.If(inst == z3.StringVal("L"), lturn, d)
    turn = z3.If(inst == z3.StringVal("R"), rturn, turn)

    return Robot.cons(Robot.p(r), turn, Robot.seen(r))

def eval_walk_robo(r, inst):
    d = Robot.d(r)
    dx = z3.If(d == EAST, z3.IntVal(1), z3.If(d == WEST, z3.IntVal(-1), 0))
    dy = z3.If(d == SOUTH, z3.IntVal(1), z3.If(d == NORTH, z3.IntVal(-1), 0))

    walks = r
    
    rp = Robot.p(r)
    rx, ry = Point.x(rp), Point.y(rp)
    for i in range(1,MAX_NUM):
        pset = z3.EmptySet(Point)
        for j in range(1,i+1):
            pset = z3.SetAdd(pset, Point.cons(rx+dx*j, ry+dy*j))

        rr = Robot.cons(Point.cons(rx+dx*i, ry + dy*i), d, z3.SetUnion(Robot.seen(r), pset))

        walks = z3.If(inst == z3.StringVal(str(i)), rr, walks)

    return walks



def eval_ro_inst(world, r, inst):
    r = eval_rotate_robo(r, inst)
    r = eval_walk_robo(r, inst)

    return r

def eval_ro_insts(world, r, insts):
    for inst in insts:
        r = eval_ro_inst(world, r, inst)

    return r


def eval_m_inst(world, r, a_insts, b_insts, c_insts, inst):
    r = z3.If(inst == z3.StringVal("A"), eval_ro_insts(world, r, a_insts), r)
    r = z3.If(inst == z3.StringVal("B"), eval_ro_insts(world, r, b_insts), r)
    r = z3.If(inst == z3.StringVal("C"), eval_ro_insts(world, r, c_insts), r)

    return r

# Return the robot
def eval_robot_insts(world, r, a_insts, b_insts, c_insts, m_insts):
    for mi in m_insts:
        r = eval_m_inst(world, r, a_insts, b_insts, c_insts, mi)

    return r

# Returns the best program there is
def best(world, rx, ry, rd):
    s = z3.Solver()

    # z3.set_param('parallel.enable', True)
    z3.set_param(verbose = 10)
    
    # Declare the instructions
    a_insts = [z3.String("a{}".format(i)) for i in range(10)]
    b_insts = [z3.String("b{}".format(i)) for i in range(10)]
    c_insts = [z3.String("c{}".format(i)) for i in range(10)]
    m_insts = [z3.String("m{}".format(i)) for i in range(10)]


    # Must be part of the valid set
    m_set = z3.EmptySet(z3.StringSort())
    for k in "ABC":
        m_set = z3.SetAdd(m_set, z3.StringVal(k))

    abc_set = z3.EmptySet(z3.StringSort())
    numbers = [str(x) for x in range(1,MAX_NUM)]
    for k in ["L", "R"] + numbers:
        abc_set = z3.SetAdd(abc_set, z3.StringVal(k))

    a_set_in = must_be_in_set(a_insts, abc_set)
    b_set_in = must_be_in_set(b_insts, abc_set) 
    c_set_in = must_be_in_set(c_insts, abc_set) 
    m_set_in = must_be_in_set(m_insts, m_set)
    s.add(a_set_in)
    s.add(b_set_in)
    s.add(c_set_in)
    s.add(m_set_in)

    # That it must be sequentive
    a_follow = must_follow(a_insts)
    b_follow = must_follow(b_insts)
    c_follow = must_follow(c_insts)
    m_follow = must_follow(m_insts)
    s.add(a_follow)
    s.add(b_follow)
    s.add(c_follow)
    s.add(m_follow)

    # The length requirement
    a_str = insts_to_str(a_insts)
    b_str = insts_to_str(b_insts)
    c_str = insts_to_str(c_insts)
    m_str = insts_to_str(m_insts)
    s.add(z3.Length(a_str) <= 20)
    s.add(z3.Length(b_str) <= 20)
    s.add(z3.Length(c_str) <= 20)
    s.add(z3.Length(m_str) <= 20)

    

    d = {"^": NORTH, ">": EAST, "v": SOUTH, "<": WEST}[chr(rd)]

    r = Robot.cons(Point.cons(rx, ry), d, z3.EmptySet(Point))

    # PLaces
    places_set = z3.EmptySet(Point)

    for (x,y) in world.keys():
        places_set = z3.SetAdd(places_set, Point.cons(x,y))


    # Here we must eval for a certain amount of steps
    rr = eval_robot_insts(world, r, a_insts, b_insts, c_insts, m_insts)
    print("we have created the possibility tree")

    s.add(places_set == Robot.seen(rr))

    if s.check() == z3.sat:
        m = s.model()
        aa = m.evaluate(a_str).as_string()
        bb = m.evaluate(b_str).as_string()
        cc = m.evaluate(c_str).as_string()
        mm = m.evaluate(m_str).as_string()
        print("A: " + aa)
        print("B: " + bb)
        print("C: " + cc)
        print("M: " + mm)
    else:
        print("It cannot work!")


    return "-"

        
def solve(s):
    # print('\033c', end="")
    codes = [int(x) for x in s.split(",")]

    q1 = queue.Queue()
    q2 = queue.Queue()

    t = threading.Thread(target=exec, args=(codes[:], q1, q2))
    t.start()


    t.join()
    

    rx, ry = 0, 0
    rd = '^'
    world = {}
    x, y = 0, 0
    while not q2.empty():
        m = q2.get()
        if m == 10:
            x = 0
            y += 1
        else:
            if m != ord("."):
                world[(x,y)] = True
                if m != ord("#"):
                    rx, ry = x, y
                    rd = m


            x += 1

    # Ok so we can define a set of valid moves for a spot
    # 

    kaka = best(world, rx, ry, rd)
    return kaka

    # Now we need to define the possibilities here.
    for a_len in range(11):
        for b_len in range(11):
            for c_len in range(11):
                for main_len in range(11):
                    dk = poss(world, rx, ry, rd, a_len, b_len, c_len, main_len)

    
    ans = 0
    for x,y in world.keys():
        pts = [(x,y+1),(x+1,y),(x,y-1),(x-1,y)]

        for p in pts:
            if p not in world:
                break
        else:
            ans += x * y

    
    return ans

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


        
        # Move to edge of screen
        print("\033[0;0H", end="")
        print_world(world, x, y)
        time.sleep(1/30)

    # To terminate the seach
    q1.put(None)

    # Now we can get the length form start to tx, ty
    rr = route_to(G, 0, 0, ox, oy)
    return len(rr)



for line in fileinput.input():
    print(solve(line.strip()))
