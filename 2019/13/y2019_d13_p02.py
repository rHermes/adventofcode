import fileinput
import itertools as it
from collections import defaultdict
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
            # ins = inputs.pop(0)
            ops[dst] = next(inputs)
            # wow = int(input("> "))
            # ops[dst] = wow
            
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

def print_board(board, minx, miny, maxx, maxy):
    print('\033c')
    minx, miny = max(0,minx), max(0, miny)
    for y in range(miny, maxy+1):
        for x in range(minx, maxx+1):
            print(board.get((x,y), " "), end="")
        print()

    print("SCORE: {}".format(board[(-1,0)]))
   

# Solution here can be to figure out ball position and where we are?


def animate(codes, inputs):
    ops, outs = exec(codes[:], it.chain(inputs,it.repeat(0)))
    # Board is 42 wide x 23 tall?
    board = {}

    minx, miny = 10000000000000, 100000000000000
    maxx, maxy = -minx, -miny

    i = 0
    blocks = 0
    first_score = 0
    while i < len(outs):
        x, y, tile = outs[i], outs[i+1], outs[i+2]
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
        

# This gives out the ball position and how many blocks are left.
def one_run(codes, thing):
    ops, outs = exec(codes[:], it.chain(thing,it.repeat(0)))
    
    board = {}

    ball_pos = []
    paddle_pos = []
    scores = []

    i = 0
    blocks = 0
    while i < len(outs):
        x, y, tile = outs[i], outs[i+1], outs[i+2]
        i += 3

        if x == -1 and y == 0:
            scores.append(tile)
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
            paddle_pos.append((x,y))
            #print_board(board, minx, miny, maxx, maxy)
        elif tile == 4:
            board[(x,y)] = "O"
            ball_pos.append((x,y))
            #print_board(board, minx, miny, maxx, maxy)
        else:
            raise Exception("THIS IS AN ERROR")

    return (ball_pos, paddle_pos, scores, blocks)
        
def solve(s):
    codes = [int(x) for x in s.split(",")]
    codes[0] = 2

    last_len = 0
    paths = [0,0,0]
    tot_blocks = -1

    s2_done = False
    s3_done = False
    s4_done = False

    while True:
        # print(paths)
        bps, pps, scores, nb = one_run(codes, paths)
        if tot_blocks < 0:
            tot_blocks = nb
        
        blocks_left = nb - len(scores) + 2


        #print("BPS: {}".format([x for x, _ in bps]))
       # print("BPS: {}".format([x for x, _ in bps]))
        #print("BPS: {}".format([x for x, y in bps if y == 21]))
        print("BPS: {}".format(bps[-10:]))
        print("PPS: {}".format(pps))
        print("MOVES: {}".format(paths))
        print("SCORES: {}".format(scores))
        print("BLOCKS LEFT: {}".format(nb - len(scores) + 2))

        lx, ly = bps[-2]
        px, py = pps[-1]

        lt = len(bps)-2
        pt = len(paths)-1

        dist = abs(lx-px)
        print("Miss happens at {} with ball at {} and paddle at {}. Paddle has been still since {}".format(lt, lx, px, pt))
        print("the distance is {}".format(dist))
        
        if lt-pt < dist:
            print("We cannot make it!")
            animate(codes, paths)
            break

        rest_steps = lt-pt-dist
        #print("We are {} away and we can rest {}".format(dist, rest_steps))
        

        
        if scores[-2] == 2078:
            paths += [1, 1, 1, 1]
            #animate(codes, paths + [-1,1,1,1,1,1])
            #animate(codes, paths)
            #break

        if blocks_left == 178 and not s2_done:
            # animate(codes, paths)
            paths += [1, 1, 1, 1, 1, 1]
            s2_done = True
            #break
        
        if blocks_left == 148 and not s3_done:
            # animate(codes, paths)
            paths += [-1, -1]
            s3_done = True
            # break



        for _ in range(rest_steps):
            paths.append(0)

        while lx < px:
            paths.append(-1)
            px -= 1
        while lx > px:
            paths.append(1)
            px += 1

        if blocks_left == 101 and not s4_done:
            animate(codes, paths)
            s4_done = True
            # break
            # break




def solve2(s):
    codes = [int(x) for x in s.split(",")]
    codes[0] = 2
    ops, outs = exec(codes[:], it.repeat(1))
    
    board = {}

    minx, miny = 10000000000000, 100000000000000
    maxx, maxy = -minx, -miny

    i = 0
    blocks = 0
    first_score = 0
    while i < len(outs):
        x, y, tile = outs[i], outs[i+1], outs[i+2]
        # print("We have {} {} of type {}".format(x, y, tile))
        i += 3
        
        minx, miny = min(minx,x), min(miny,y)
        maxx, maxy = max(maxx,x), max(maxy,y)

        if x == -1 and y == 0:
            first_score = 1
            print("New score: {}".format(tile))
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
        elif tile == 4:
            board[(x,y)] = "O"
            #print_board(board, minx, miny, maxx, maxy)
        else:
            raise Exception("THIS IS AN ERROR")
        
        if first_score == 1:
            time.sleep(1/20)
        
        # input()

    print_board(board, minx, miny, maxx, maxy) 
    sss = ""
    minx, miny = max(0,minx), max(0, miny)
    for y in range(miny, maxy+1):
        for x in range(minx, maxx+1):
            sss += board[(x,y)]
        sss += "\n"
    
    return sss
    #return blocks
    # return outs

for line in fileinput.input():
    print(solve(line.strip()))
