# Here we use the chinese remainder theorem, the sieving method.
import fileinput as fi

inp = fi.input()
erl = int(next(inp))
buses = [((-i) % int(x), int(x)) for (i,x) in enumerate(next(inp).split(",")) if x.rstrip() != 'x']

# Sorting the inputs makes this much faster
buses = sorted(buses, key=lambda x: x[1], reverse=True)

t, df = buses[0]
for i, b in buses[1:]:
    while (t-i) % b != 0:
        t += df
    df *= b

print(t)
