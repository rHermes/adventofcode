import fileinput
import itertools as it
from collections import defaultdict
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
            ops[dst] = input_queue.get()
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

def print_board(board, minx, miny, maxx, maxy):
    print('\033c')
    minx, miny = max(0,minx), max(0, miny)
    for y in range(miny, maxy+1):
        for x in range(minx, maxx+1):
            print(board.get((x,y), " "), end="")
        print()
    
    # We are reading inputs
    print("SCORE: {}".format(board[(-1,0)]))
   

# Solution here can be to figure out ball position and where we are?


def animate(codes):
    #ops, outs = exec(codes[:], it.chain(inputs,it.repeat(0)))
    # Board is 42 wide x 23 tall?
    board = {}

    minx, miny = 10000000000000, 100000000000000
    maxx, maxy = -minx, -miny

    i = 0
    blocks = 0
    first_score = 0
    its = iter(exec(codes[:], it.repeat(1)))
    while True:
        x, y, tile = next(its), next(its), next(its)
        i += 3
        # print("We have {} {} of type {}".format(x, y, tile))
        i += 3
        
        minx, miny = min(minx,x), min(miny,y)
        maxx, maxy = max(maxx,x), max(maxy,y)

        if x == -1 and y == 0:
            first_score = 1
            board[(x,y)] = tile
            # print("New score: {}".format(tile))
        elif tile == 0:
            board[(x,y)] = " "
            #print_board(board, minx, miny, maxx, maxy)
        elif tile == 1:
            board[(x,y)] = "W"
            #print_board(board, minx, miny, maxx, maxy)
        elif tile == 2:
            board[(x,y)] = "X"
            #print_board(board, minx, miny, maxx, maxy)
            blocks += 1
        elif tile == 3:
            board[(x,y)] = "-"
            if first_score == 1:
                print_board(board, minx, miny, maxx, maxy)
                # time.sleep(1/16)
        elif tile == 4:
            board[(x,y)] = "O"
            if first_score == 1:
                print_board(board, minx, miny, maxx, maxy)
                time.sleep(1/30)
            #print_board(board, minx, miny, maxx, maxy)
        else:
            raise Exception("THIS IS AN ERROR")

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

        
def solve(s):
    codes = [int(x) for x in s.split(",")]

    q1 = queue.Queue()
    q2 = queue.Queue()

    t = threading.Thread(target=exec, args=(codes[:], q1, q2))
    t.start()

    x, y = 0, 0
    world = defaultdict(lambda: str("?"))

    dirs = {1: (0,1), 2: (0,-1), 3: (-1,0), 4:(1,0)}

    while True:
        print('\033c')
        print_world(world, x, y)

        dirr = get_dir_key()
        dx, dy = dirs[dirr]
        nx, ny = x + dx, y + dy

        q1.put(dirr)

        res = q2.get()

        if res == 0:
            world[(nx,ny)] = "█"
        elif res == 1:
            world[(nx,ny)] = " "
            x, y = nx, ny
        elif res == 2:
            world[(nx,ny)] = "Æ"
            x, y = nx, ny



for line in fileinput.input():
    print(solve(line.strip()))
