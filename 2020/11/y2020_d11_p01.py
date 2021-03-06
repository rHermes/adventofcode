import fileinput
import itertools as it

# Let's build a jump table
def jumptbl(M, ROWS, COLS, x, y):
    arounds = []
    for dy, dx in [(-1,-1), (-1, 0), (-1, 1), (0,-1), (0, 1), (1,-1), (1,0), (1,1)]:
        zx = x + dx
        zy = y + dy
        idx = zy*COLS + zx
        if 0 <= zx < COLS and 0 <= zy < ROWS and M[idx] != None:
            arounds.append(idx)

    return arounds


# Creates a compressed version of a jump array
def compress(M, ROWS, COLS):
    comp = []
    # translate from full to sparse
    trans = {}

    # Build spare index
    for y in range(COLS):
        for x in range(ROWS):
            idx = y*COLS + x
            if M[idx] == None:
                continue

            trans[idx] = len(comp)
            comp.append(M[idx])

    # Build jump table
    jmp = {}
    for oidx, nidx in trans.items():
        y = oidx // COLS
        x = oidx % COLS
        # Second pass, now to create jump table
        adj = frozenset(trans[k] for k in jumptbl(M, ROWS, COLS, x, y))
        if len(adj) < 4:
            comp[nidx] = True
        else:
            jmp[nidx] = adj

    return (comp, jmp)

# Step from M to N uing jmp
def step(M, N, jmp):
    changed = False
    for idx, adj in jmp.items():
        t = sum(M[x] for x in adj)
        N[idx] = (M[idx] and t < 4) or ((not M[idx]) and t == 0)
        changed |= N[idx] != M[idx]

    return changed


lines = [line.rstrip() for line in fileinput.input()]
ROWS = len(lines)
COLS = len(lines[0])

# None takes the spot of Empty
M = [{'L': False, '#': True, '.': None}[x] for x in it.chain(*lines)]
comp, jmp = compress(M, ROWS, COLS)

A = comp
B = A.copy()

while step(A, B, jmp):
    B, A = A, B

print(sum(A))
