import fileinput as fi

GEN_A_FAC = 16807
GEN_B_FAC = 48271

MOD = 2147483647

def solve(a, b):
    cnt = 0
    mask = 0b1111_1111_1111_1111
    for _ in range(40_000_000):
        a = (a * GEN_A_FAC) % MOD
        b = (b * GEN_B_FAC) % MOD

        cnt += (a & mask) == (b & mask)

    return cnt

g = fi.input()
a = int(next(g).split(" ")[-1])
b = int(next(g).split(" ")[-1])

print(solve(a, b)) # real
