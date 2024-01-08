import fileinput as fi
import itertools as it

# For a free 2-3x speedup switch this out with cfractions
from cfractions import Fraction

stones = []
for line in fi.input():
    pos, vel = line.split(" @ ")
    pos = tuple(int(x) for x in pos.split(", "))
    vel = tuple(int(x) for x in vel.split(", "))
    stones.append((pos, vel))

# ok, so we know only one thing, 
#for i in range(len(stones)):
#
    

