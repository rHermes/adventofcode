import fileinput as fi
import itertools as it
import numpy as np


def crossMatrix(m):
    # We assume m is a 3x3 matrxi
    return np.array([
        [0, -m[2], m[1]],
        [m[2], 0, -m[0]],
        [-m[1], m[0], 0]
    ])

# The rhs of the equations between stones i and j
def C(stones, i, j):
    ip, iv = stones[i]
    jp, jv = stones[j]
    return np.cross(ip, iv) - np.cross(jp, jv)

def MP(stones, i, j):
    ip, _ = stones[i]
    jp, _ = stones[j]

    return crossMatrix(ip - jp)

def MV(stones, i, j):
    _, iv = stones[i]
    _, jv = stones[j]
    
    # the sign is flipped here, because we want to make the end result prettier
    return crossMatrix(iv - jv)

stones = []
for line in fi.input():
    pos, vel = line.split(" @ ")
    pos = np.array([int(x) for x in pos.split(", ")])
    vel = np.array([int(x) for x in vel.split(", ")])
    stones.append((pos, vel))

# print(stones)

C0 = C(stones, 0, 1)
MP0 = MP(stones, 0, 1)
MV0 = MV(stones, 0, 1)

C1 = C(stones, 0, 2)
MP1 = MP(stones, 0, 2)
MV1 = MV(stones, 0, 2)

joinedC = np.block([C0, C1])
joinedM = np.block([
    [MP0, -MV0],
    [MP1, -MV1]
])


wk = np.linalg.solve(joinedM, joinedC)
vel, pos = np.split(wk, 2)
ans = 0
for k in pos:
    ans += int(k)
print(ans)
