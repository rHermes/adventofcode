import fileinput as fi
import itertools as it
import collections
import functools as ft
import copy


import more_itertools as mit

# findall
# search
# parse
from parse import *


lines = []
for l in fi.input():
    if l.rstrip():
        lines.append(l.rstrip())
    else:
        break

mem = {}



mask = ""
assigns = []

back_map = {}

for line in lines:
    if line.startswith("mask = "):
        k = parse("mask = {}", line)[0]
        mask = k

    else:
        k, y = list(parse("mem[{:d}] = {:d}", line))
        ll = []
        for m, v in zip(mask, "{:>036b}".format(k)):
            if m == "0":
                ll.append(v)
            elif m == "1":
                ll.append("1")
            else:
                ll.append("X")
 
        back_map["".join(ll)] = mask
        assigns.append((ll, y))
        # print("{:>036b}".format(k))

# for k, v in assigns:
#     print("".join(k), v)
# print(assigns)
# for k, v in mem.items():
#     print(k, v)


# xs is existing mask, ys is new
# check if new crashes with old
def collides(old, new):
    # First we check that they collide
    for x, y in zip(old, new):
        if x != y:
            # if they don't match and they have no conflict we add
            if x != "X" and y != "X":
                return False

    return True

# Narrow the hash down, returning an array of hashes to narrow down
def narrow_hashe(old, new):
    good = []
    cons = collections.deque([new])
    while cons:
        cur = cons.popleft()
        if not collides(old, cur):
            good.append(cur)
            continue
        
        # We colldie so we implement something
        # the first X we have that can be toggled 
        # we add to the pile
        for i in range(len(new)):
            if new[i] == 'X' and old[i] != 'X':
                zz = new.copy()
                if old[i] == '1':
                    zz[i] = '0'
                else:
                    zz[i] = '1'

                cons.append(zz)
                # good.append(zz)
                #break
        
    return good    




done = []
for dest, val in reversed(assigns):
    q = collections.deque([dest])
    while q:
        qc = q.popleft()
        for dd, _ in done:
            if collides(dd, qc):
                # print(back_map["".join(dest)], "which becomes", "".join(dest), "collides with",back_map["".join(dd)] )
                q.extend(narrow_hashe(dd, qc))
                break
        else:
            # If we made it through we do this
            done.append((qc, val))


    # done.append((dest,val))
ans = 0
for m, val in done:
    # print("".join(m), val)
    ans += 2**(sum([1 for x in m if x == 'X'])) * val
print(ans)
