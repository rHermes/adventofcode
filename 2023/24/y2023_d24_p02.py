# Ok, so this is going to be a bit of a dozy to explain, but I'll do my best
# as it will be really difficult to remember the exact steps later.
#
# We begin with defining the following variables:
#
# p    = The initial position of our new hailstone
# v    = The velocity of our new hailstone
# t[i] = The time of intersection with this new stone for stone i
# p[i] = The initial position of hailstone i
# v[i] = The velocity of hailstone i
#
# In our calculations later we use the following notation:
#
# * = scalar multiplication
# . = matrix multiplication
# x = cross product
#
# We are then looking to solve the equation:
#
# p + t[i]*v = p[i] + t[i]*v[i]
#
# Which we reorder:
#
# p - p[i] = t[i] * (v[i] - v)
#
# To get rid of the t[i], we are going to apply the cross product on
# both sides, with (v[i] - v)
#
# (p - p[i]) x (v[i] - v) = t[i] * (v[i] - v) x (v[i] - v)
# (p - p[i]) x (v[i] - v) = 0
#
# If we expand this we get:
#
# (p - p[i]) x (v[i] - v) = 0
# (p - p[i]) x v[i] - (p - p[i]) x v = 0
# (p x v[i]) - (p[i] x v[i]) - (p x v) + (p[i] x v) = 0
# (p x v[i]) - (p[i] x v[i]) + (p[i] x v) = p x v
#
# The key insight here, is that the only non linear factor here is
# (p x v) and it's common to all hailstones. Therefor we can can
# create an equation with two hailstones i and j:
#
# (p x v[i]) - (p[i] x v[i]) + (p[i] x v) = (p x v[j]) - (p[j] x v[j]) + (p[j] x v)
# (p x v[i]) - (p x v[j]) + (p[i] x v) - (p[j] x v) = (p[i] x v[i]) - (p[j] x v[j])
# p x (v[i] - v[j]) + (p[i] - p[j]) x v = (p[i] x v[i]) - (p[j] x v[j])
# (v[j] - v[i]) x p + (p[i] - p[j]) x v = (p[i] x v[i]) - (p[j] x v[j])
#
# Now we can actually convert a cross product to a matrix, with the
# following function
#
# a x b = crossM(a) . b  
#
# where
#
#               0, -az,  ay
# crossM(a) =  az,   0, -ax
#             -ay,  ax,   0
#
#
# Using this, we can now convert the above to:
#
# crossM(v[j] - v[i]) . p + crossM(p[i] - p[j]) . v = (p[i] x v[i]) - (p[j] x v[j])
#
# We define 
# 
# MV(i,j) = crossM(v[j] - v[i]) 
# MP(i,j) = crossM(p[i] - p[j])
# C(i,j) = (p[i] x v[i])  - (p[j] x v[j])
#
# And with this we get:
#
# MV(i,j) . p + MP(i, j) . v = C
#
# Now we can treat these as block matrices and we get:
#
#                          [ p ]
# [ MV(i, j), MP(i, j) ] . [ v ] = C(i, j)
#
#         (3x6)          . (6x1) = (3x1)
#
# Now that we have this in the form A.x = b, we can solve it with row reduction.
# However, we have 6 unknowns and only 3 equations. To make the solution unique,
# we simply repeat the same equations, but for a different pair of hailstones.
# we introduce a third hailstone k, and now we get:
#                            
# [ MV(i, j), MP(i, j) ]   [ p ]   [ C(i, j) ]
# [ MV(i, k), MP(i, k) ] . [ v ] = [ C(i, k) ]
#
#        (6x6)           . (6x1) = (6x1)
#
# Now we just apply row reduction and if there is a solution we should find it.
# There are some more things we need to keep track of here. This does not
# hold the guarantee that it will work for all other hailstones we have, so
# we need to go through the list and verify that it is indeed a solution.
# 
# We also need to make sure that the time it intersects is an integer and that
# it's more than 0.
#
# To avoid errors, we will use fractions in the matrices during row reductions.

import fileinput as fi

# For a free 2-3x speedup switch this out with cfractions
try:
    from cfractions import Fraction
except ImportError as e:
    from fractions import Fraction

def vecCross(a, b):
    a1, a2, a3 = a
    b1, b2, b3 = b

    return (a2*b3 - a3*b2, a3*b1 - a1*b3, a1*b2 - a2*b1)

def vecMinus(a, b):
    return tuple(x - y for x, y in zip(a, b))

def linearlyIndependent(a, b):
    # The two vectors are dependent if the cross product is 0
    return any(v != 0 for v in vecCross(a,b))

def crossMatrix(m):
    # We assume m is a 1x3 vector.
    # This returns the matrix that is equal to doing the cross operation
    return [
        [0, -m[2], m[1]],
        [m[2], 0, -m[0]],
        [-m[1], m[0], 0]
    ]

def findIndependentSet(stones):
    # We want three stones that have independent speed vectors.
    selected = [0]
    selectedVecs = [stones[0][1]]
    while len(selected) < 3:
        for i in range(selected[-1]+1, len(stones)):
            _, iv = stones[i]

            if all(linearlyIndependent(iv, sv) for sv in selectedVecs):
                selected.append(i)
                selectedVecs.append(iv)
                break
        else:
            print("We were unable to find a linearly independent set!")
            exit(1)

    return selected

def createLinearEquations(stones, i, j):
    ip, iv = stones[i]
    jp, jv = stones[j]

    C = vecMinus(vecCross(ip, iv), vecCross(jp, jv))
    MV = crossMatrix(vecMinus(jv, iv))
    MP = crossMatrix(vecMinus(ip, jp))

    # We return the augmented matrix
    return [[*a, *b, c] for a,b,c in zip(MV, MP, C)]

def rowReduce(mat):
    # Taken from https://en.wikipedia.org/wiki/Gaussian_elimination#Pseudocode
    # With some modifications
    M, N = len(mat), len(mat[0])

    # Pivot row
    h = 0
    # Pivot column
    k = 0
    while h < M and k < N:
        # We find the index of the element with the largest absolute value,
        # as this is the row we will use as a pivot.
        i_max, v_max = -1, -1
        for i in range(h, M):
            if v_max < abs(mat[i][k]):
                v_max = abs(mat[i][k])
                i_max = i

        if mat[i_max][k] == 0:
            # There is no pivot in this column, we continue to the next
            k = k + 1
        else:
            # We swap the row with the current pivot row, so it's in the
            # right place.
            mat[h], mat[i_max] = mat[i_max], mat[h]

            # We also scale our column, so that 1
            f = 1 / mat[h][k]
            for j in range(k, N):
                mat[h][j] *= f

            # We zero out all the values in the column between the row.
            for i in range(h+1, M):
                f = mat[i][k]
                for j in range(k, N):
                    mat[i][j] = mat[i][j] - mat[h][j] * f

            h += 1
            k += 1

    # This is the step to get it to reduced echelon form.
    for h in range(M-1, -1, -1):
        i_first = 0
        while i_first < N:
            if mat[h][i_first] != 0:
                break
            else:
                i_first += 1
        else:
            continue

        if mat[h][i_first] == 0:
            continue

        for ri in range(h):
            f = mat[ri][i_first]
            for ci in range(i_first, N):
                mat[ri][ci] -= f * mat[h][ci]



# Parse the input
stones = []
for line in fi.input():
    pos, vel = line.split(" @ ")
    # We use fractions here, to avoid floating point errors.
    pos = tuple([Fraction(int(x)) for x in pos.split(", ")])
    vel = tuple([Fraction(int(x)) for x in vel.split(", ")])
    stones.append((pos, vel))

# We find three independent stones
s1, s2, s3 = findIndependentSet(stones)

# We need two set of equations, to get a 6x6 matrix total.
system01 = createLinearEquations(stones, s1, s2)
system02 = createLinearEquations(stones, s1, s3)

# Combine the two augmented matrices, so we have enough equations to solve it.
combined = system01 + system02
rowReduce(combined)

# Assure that we get an integer answer out.
for row in combined:
    assert(row[-1].denominator == 1)

pos = tuple(row[-1].numerator for row in combined[0:3])
vel = tuple(row[-1].numerator for row in combined[3:6])

# Verify that the collision happens at an integer time and in the future for all stones.
for spos, svel in stones:
    ts = set()
    for i in range(3):
        nom = pos[i] - spos[i].numerator
        den = svel[i].numerator - vel[i]
        if den == 0:
            if nom != 0:
                raise RuntimeError("unable to intersect all stones")
        else:
            ts.add(Fraction(nom,den))

    if 1 < len(ts) or list(ts)[0] <= 0 or list(ts)[0].denominator != 1:
        raise RuntimeError("unable to intersect all stones")
    
print(sum(pos))
