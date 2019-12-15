import fileinput

def solve(s):
    ops = [int(x) for x in s.split(",")]

    W = ops[582]
    H = ops[604]

    BOARD_OFFSET = 639

    M1 = (ops[612] *  ops[613]) or (ops[612] + ops[613])
    M2 = (ops[616] *  ops[617]) or (ops[616] + ops[617])
    M3 = (ops[620] *  ops[621]) or (ops[620] + ops[621])
    M4 = ops[632]

    score = 0
    for y in range(H):
        for x in range(W):
            c = ops[BOARD_OFFSET+ y*W + x]
            if c != 2:
                continue

            t = H * x  + y
            # The pos in memory
            pos = ((((t * M1 + M2) % (M3 * 64)) % (M3 * 8)) % M3) + M4
            score += ops[pos]

    return score


for line in fileinput.input():
    print(solve(line.strip()))
