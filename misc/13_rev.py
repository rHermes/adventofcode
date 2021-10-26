def read_in_ops(fp):
    with open(fp, "r") as f:
        wow = f.read()

    wow = wow.strip()
    codes = [int(x) for x in wow.split(",")]
    return codes

def work(ops, play=False):
    # m[381] seems to be integrety check or temp variable?
    # m[382] is where we store screen X
    # m[383] is where we store screen Y
    # m[384] is the input
    # m[385] is coins
    # m[386] is the score
    # m[387] is the number of blocks remaining
    # m[392] is the paddle X

    outputs = []
    inputs = []

    W = ops[582]
    H = ops[604]

    BOARD_OFFSET = 639
    SCORE = 0
    INPUT = 0
    PADDLE_X = ops[392]
    BLOCKS_LEFT = ops[387]
    BALL_Y = ops[388]
    BALL_X = ops[389]
    BALL_DIR_Y = ops[390]
    BALL_DIR_X = ops[391]

    COINS = int(play == False)

    # This returns the character at a position in the board
    def f578(y,x):
        idx = y*W + x
        return ops[BOARD_OFFSET+idx]
    
    # This sets the value and prints it out
    def f549(c,y,x):
        idx = y*W + x
        ops[BOARD_OFFSET+idx] = c
        outputs.append(x)
        outputs.append(y)
        outputs.append(c)

    # Don't know what this does 
    def f456(p1, p2, p3, p4):
       # 456:        109 BASE   8
       # 458:      22202 MULT   p4, p3, L0
       # 462:      22201 ADD    L0, p2, L0
       # 466:      21202 MULT   p1, 64, L1
       # 470:       2207 LT     L0, L1, m[381]
       # 474:       1005 JT     m[381], 492
       # 477:      21202 MULT   L1, -1, L2
       # 481:      22201 ADD    L0, L2, L0
       # 485:       2207 LT     L0, L1, m[381]
       # 489:       1006 JF     m[381], 481
       # 492:      21202 MULT   p1, 8, L1
       # 496:       2207 LT     L0, L1, m[381]
       # 500:       1005 JT     m[381], 518
       # 503:      21202 MULT   L1, -1, L2
       # 507:      22201 ADD    L0, L2, L0
       # 511:       2207 LT     L0, L1, m[381]
       # 515:       1006 JF     m[381], 507
       # 518:       2207 LT     L0, p1, m[381]
       # 522:       1005 JT     m[381], 540
       # 525:      21202 MULT   p1, -1, L2
       # 529:      22201 ADD    L0, L2, L0
       # 533:       2207 LT     L0, p1, m[381]
       # 537:       1006 JF     m[381], 529
       # 540:      22101 ADD    0, L0, p4
       # 544:        109 BASE   -8
       # 546:       2106 JF     0, m[base + 0]

        L0 = p4 * p3
        L0 = L0 + p2
        L1 = p1 * 64

        if not (L0 < L1):
            # 477
            L2 = L1 * -1
            # 481
            L0 = L0 + L2
            while not (L0 < L1):
                L0 = L0 + L2

        # 492
        L1 = p1 * 8

        if not (L0 < L1):
            # 503
            L2 = L1 * -1
            # 507
            L0 = L0 + L2
            while not (L0 < L1):
                L0 = L0 + L2

        # 518
        k = L0 < p1
        if not (L0 < p1):
            # 525
            L2 = p1 * -1
            # 529
            L0 = L0 + L2
            while not (L0 < p1):
                L0 = L0 + L2

        return L0
    
    def f456_simpler(p1, p2, p3, p4):
        L0 = p4 * p3 + p2
        L1 = p1 * 64

        L0 = L0 % (p1 * 64)
        L0 = L0 % (p1 * 8)
        L0 = L0 % (p1)


        L0 = ((((p4 * p3 + p2) % (p1 * 64)) % (p1 * 8)) % p1)
        return L0
    
    # This calculates new score I think
    def f601(p1, p2):
        tmp0 = H * p2 + p1

        # Here there are some werid tales, have to check this out
        # M1 = max(ops[612] + ops[613], ops[612] * ops[613])
        # M2 = max(ops[616] + ops[617], ops[616] * ops[617])
        # M3 = max(ops[620] + ops[621], ops[620] * ops[621])
        M1 = (ops[612] * ops[613]) or (ops[612] + ops[613])
        M2 = (ops[616] * ops[617]) or (ops[616] + ops[617])
        M3 = (ops[620] * ops[621]) or (ops[620] + ops[621])

        # print("{}".format((M3,M2,M1,tmp0)))

        # 603 is return
        btmp0 = f456(M3, M2, M1, tmp0)

        bshouldbe = f456_simpler(M3, M2, M1, tmp0)

        assert(btmp0 == bshouldbe)
        
        # This is a mystery constant
        M4 = ops[632]

        return M4 + btmp0


    # This calculates scores somehow
    def f393(y,x):
        f549(0,y,x)
        
        # This is the position of the block
        pos = f601(y,x)
        SCORE = SCORE + ops[pos]

        outputs.append(-1)
        outputs.append(0)
        outputs.append(SCORE)

        BLOCKS_LEFT = BLOCKS_LEFT - 1

        if BLOCKS_LEFT == 0:
            raise Exception("We halted here!")


    X = 0
    Y = 0
    blocks_pos = []
    while True:
        btmp0 = f578(Y,X)
        outputs.append(X)
        outputs.append(Y)
        outputs.append(btmp0)

        if btmp0 == 2:
            blocks_pos.append((X,Y))
            

        X += 1
        if X < W:
            continue

        Y += 1
        if Y < H:
            # print("")
            X = 0
            continue
        
        #print("")
        break



    if COINS:
        return outputs

    outputs.append(-1)
    outputs.append(0)
    outputs.append(SCORE)


    # HERE we read in
    INPUT = 1

    if INPUT < 0:
        if 1 < PADDLE_X:
            INPUT = -1
            f549(0, H-1, PADDLE_X)
            PADDLE_X = PADDLE_X + INPUT
            f549(3, H-1, PADDLE_X)
        pass
    else:
        if 0 < INPUT:
            if PADDLE_X < W-2:
                INPUT = 1
                f549(0, H-1, PADDLE_X)
                PADDLE_X = PADDLE_X + INPUT
                f549(3, H-1, PADDLE_X)
            else:
                pass
        else:
            pass

    # m[381] seems to be integrety check or temp variable?
    # m[382] is where we store screen X
    # m[383] is where we store screen Y
    # m[384] is the input
    # m[385] is coins
    # m[386] is the score
    # m[387] is the number of blocks remaining
    # m[388] is ball y pos?
    # m[389] is ball x pos?
    # m[390] is the trajectory of the ball when the game starts, 1 is going down -1 is going up
    # m[391] is the ball trajctory in the x axis
    # m[392] is the paddle X

    # 161
    INPUT = 0
    
    # Get what is 
    btmp0 = f578(BALL_Y + BALL_DIR_Y, BALL_X)
    if btmp0 == 2:
        # 190
        pass
    
    may = 0
    for (x,y) in blocks_pos:
        pos_of_score = f601(y,x)
        if pos_of_score < len(ops) and pos_of_score > -1:
            val_of_score = ops[pos_of_score]
            print("Value of block at {}: ops[{}] = {}".format((x,y), pos_of_score, val_of_score))
            may += val_of_score
        else:
            print("Value of block at {}: was outside of range {}".format((x,y), pos_of_score))


    print("Total value: {}".format(may))

    
    mm =f456(966, 326, 487, 212)
    if mm  != 208:
        print("What the fuck happened here: {} vs {}".format(mm, 208))


    


    

def print_outs(outputs):
    its = iter(outputs)

    while True:
        x, y, tile = next(its), next(its), next(its)

        if x == -1 and y == 0:
            break
        if tile == 0:
            pass



if __name__ == "__main__":
    ops = read_in_ops("../2019/13/input2.txt")

    outs = work(ops, play=True)

    print(outs)
