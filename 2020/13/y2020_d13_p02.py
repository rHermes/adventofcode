import fileinput as fi
from math import lcm


inp = fi.input()
erl = int(next(inp))
busses = ((i, int(x)) for (i,x) in enumerate(next(inp).split(",")) if x.rstrip() != 'x')

t, df = 0, 1
for i, b in busses:
    while (t+i) % b != 0:
        t += df
    df = lcm(b, df)

print(t)
