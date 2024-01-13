import fileinput as fi
from fractions import Fraction

def vecCross(a, b):
    a1, a2, a3 = a
    b1, b2, b3 = b

    return ( a2*b3 - a3*b2, a3*b1 - a1*b3, a1*b2 - a2*b1)

def vecMinus(a, b):
    return tuple(x - y for x, y in zip(a, b))


def crossMatrix(m):
    # We assume m is a 3x3 matrxi
    return [
        [0, -m[2], m[1]],
        [m[2], 0, -m[0]],
        [-m[1], m[0], 0]
    ]

# # The rhs of the equations between stones i and j
def C(stones, i, j):
    ip, iv = stones[i]
    jp, jv = stones[j]
    return vecMinus(vecCross(ip, iv), vecCross(jp, jv))

def MP(stones, i, j):
    ip, _ = stones[i]
    jp, _ = stones[j]

    return crossMatrix(vecMinus(ip,jp))

def MV(stones, i, j):
    _, iv = stones[i]
    _, jv = stones[j]
    
    return crossMatrix(vecMinus(iv,jv))

def rowReduce(mat):
    h = 0
    k = 0

    M, N = len(mat), len(mat[0])

    while h < M and k < N:
        i_max = -1
        v_max = -100

        for i in range(h, M):
            if v_max < abs(mat[i][k]):
                v_max = abs(mat[i][k])
                i_max = i

        if mat[i_max][k] == 0:
            k = k + 1
        else:
            mat[h], mat[i_max] = mat[i_max], mat[h]

            for i in range(h+1, M):
                f = mat[i][k] / mat[h][k]
                mat[i][k] = 0
                for j in range(k+1, N):
                    mat[i][j] = mat[i][j] - mat[h][j] * f

            h += 1
            k += 1

    # Now we simplify it, so each column is 0
    for ri in range(M):
        row = mat[ri]
        f = 1 / row[ri]

        for i in range(ri, N):
            row[i] *= f

    # We now remove all above, one by one
    h = M-1
    while 0 <= h:
        i_first = 0
        while i_first < N:
            if mat[h][i_first] != 0:
                break
            else:
                i_first += 1

        if mat[h][i_first] == 0:
            h -= 1
            continue

        for ri in range(h):
            f = mat[ri][i_first]
            for ci in range(i_first, N):
                mat[ri][ci] -= f * mat[h][ci]


        h -= 1



# Parse the input
stones = []
for line in fi.input():
    pos, vel = line.split(" @ ")
    pos = tuple([Fraction(int(x)) for x in pos.split(", ")])
    vel = tuple([Fraction(int(x)) for x in vel.split(", ")])
    stones.append((pos, vel))

# We need two set of equations.
C0 = C(stones, 0, 1)
MP0 = MP(stones, 0, 1)
MV0 = MV(stones, 0, 1)

C1 = C(stones, 0, 2)
MP1 = MP(stones, 0, 2)
MV1 = MV(stones, 0, 2)

joinedC = (*C0, *C1)
joinedM =[list(a) + [-y for y in b] for a,b in zip(MP0, MV0)]
joinedM += [list(a) + [-y for y in b] for a,b in zip(MP1, MV1)]

# create a combined matrix
augmented_matrix = []
for c, m in zip(joinedC, joinedM):
    augmented_matrix.append(m + [c])

# Now we row reduce it
rowReduce(augmented_matrix)

# Assure that we get an integer answer out.
for row in augmented_matrix:
    assert(row[-1].denominator == 1)

vel = tuple(row[-1].numerator for row in augmented_matrix[0:3])
pos = tuple(row[-1].numerator for row in augmented_matrix[3:6])

# print(pos, vel)
print(sum(pos))
