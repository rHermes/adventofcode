import fileinput
from functools import reduce
from operator import xor

# Convert straight from pass to id
def pass_to_id(p):
    return sum(1<<(9-i) for (i,c) in enumerate(p) if c in "BR")

def red(acc, cur):
    mi, ma, xo = acc
    return (min(cur,mi), max(cur,ma), xo ^ cur)

mi, ma, inperf = reduce(red, map(pass_to_id, fileinput.input()), (2**10,0,0))
print(reduce(xor, range(mi, ma+1), inperf))
