import fileinput
import itertools as it

def FFT(digs):
    outs = []
    for i in range(1, len(digs)+1):
        x = 0
        ans = 0
        while x < len(digs):
            jx =  x - 1
            ones = digs[(jx+i):(jx+2*i)]
            minus = digs[(jx+(3*i)):(jx+(4*i))]
            ans += sum(ones) - sum(minus)
            x += 4*i

        outs.append(abs(ans) % 10)

    return outs

def solve(s):
    ns = [int(x) for x in s]
    kv = ns[:]
    for _ in range(100):
        kv = FFT(kv)

    mem = "".join(str(x) for x in kv[:8])
    return mem


for line in fileinput.input():
    print(solve(line.strip()))
