import fileinput as fi

GEN_A_FAC = 16807
GEN_B_FAC = 48271

MOD = 2147483647

def g(cur, fac, md):
    while True:
        cur = (cur*fac) % MOD
        if cur % md == 0:
            yield cur

def solve(a, b):
    cnt = 0
    mask = 0b1111_1111_1111_1111
    for a, b, _ in zip(g(a, GEN_A_FAC, 4), g(b, GEN_B_FAC, 8), range(5_000_000)):
        cnt += (a & mask) == (b & mask)

    return cnt

inp = fi.input()
a = int(next(inp).split(" ")[-1])
b = int(next(inp).split(" ")[-1])

print(solve(a, b))
