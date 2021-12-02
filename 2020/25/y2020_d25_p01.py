import fileinput as fi
from math import ceil, sqrt

# https://en.wikipedia.org/wiki/Baby-step_giant-step
# Returns x such that g^x % M == h
def solve(g, h, M):
    m = ceil(sqrt(M))
    table = {}
    e = 1
    for i in range(m):
        table[e] = i
        e = (e*g) % M

    factor = pow(g, M-m-1, M)
    e = h
    for i in range(m):
        if e in table:
            return i * m + table[e]
        e = (e*factor) % M

    return None

M = 20201227
card, door = [int(x) for x in fi.input()]
print(pow(door,solve(7,card,M),M))
