import fileinput
import itertools as it

def FFT(digs):
    outs = []
    for i in range(1,len(digs)+1):

        pat = it.islice(it.cycle(
                it.chain(
                    it.repeat(0,i),
                    it.repeat(1,i),
                    it.repeat(0,i),
                    it.repeat(-1,i)
                )
            ), 1, None)


        wow = [a*b for (a,b) in zip(digs,pat)]
        nn = abs(sum(wow)) % 10
        outs.append(nn)

    return outs

def solve(s):
    ns = [int(x) for x in s]
    kv = list(it.chain.from_iterable(it.repeat(ns,1000)))
    for j in range(100):
        print(j)
        kv = FFT(kv)

    mem = "".join(str(x) for x in kv[:8])
    return mem


for line in fileinput.input():
    print(solve(line.strip()))
