import fileinput
import itertools as it

def FFT(idx, offset):
    outs = []
    for i in range(0, offset):
        outs.append(0)

    LEN = len(idx) + offset - 1

    for i in range(offset, LEN):
        x = 0
        ans = 0
        while x < LEN:
            jx =  x - 1
            ones = idx[min(jx+2*i, LEN-1)] - idx[min(jx+i, LEN-1)]
            minus = idx[min(jx+4*i, LEN-1)] - idx[min(jx+3*i, LEN-1)]
            ans += ones - minus
            x += 4*i
    
        outs.append(abs(ans) % 10)

    return outs

def build_index(kv, offset):
    idx = {}
    idx[offset-1] = 0
    for x in range(offset,len(kv)):
        idx[x] = kv[x] + idx[x-1]

    return idx


def solve(s):
    ns = [int(x) for x in s]
    offset = int(s[:7])
    kv = list(it.chain.from_iterable(it.repeat(ns,10000)))

    N = 100

    for i in range(N):
        idx = build_index(kv, offset)
        kv = FFT(idx, offset)

    return "".join(str(x) for x in kv[offset:offset+8])

for line in fileinput.input():
    print(solve(line.strip()))
