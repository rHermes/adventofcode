import fileinput
import math

M = {(1,1): 0, (3,1): 0, (5,1): 0, (7,1): 0, (1,2): 0}
for (i,l) in enumerate(fileinput.input()):
    for (dx, dy) in M.keys():
        if i % dy == 0:
            M[(dx,dy)] += l[((i//dy)*dx) % (len(l)-1)] == '#'

print(math.prod(M.values()))
