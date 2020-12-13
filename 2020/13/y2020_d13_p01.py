import fileinput as fi

inp = fi.input()
erl = int(next(inp))
busses = (int(x) for x in next(inp).split(",") if x.rstrip() != 'x')

# Find the buss closest to being a full divisor after erl
f = lambda x: x - (erl % x)

b = min(busses, key=f)
print(b*f(b))
