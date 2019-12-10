import fileinput
import math

# The logic for checking if two vectors are multiples here are as following:
#
# Assume that you have u = (x1,y1) and v = (x2, y2). The two vectors are 
# multiples if:
#
# (u.v)*u == (u.u)*v
#
# In the 2d case, it factors down to: x1*y2 == y1*x2
#
# To prove this then, we can just state that x2 = x1*k and y2 = y1*j
# and plug it into the equation
#
# x1*y1*j == y1*x2*k <=> j == k
#
# If j and k are the same, then v is a multiple of u.
#
# In our case, we use this and we need to check the signs of both, to
# make sure they are thesame

def sign(x):
    if x < 0:
        return -1 
    elif x > 0:
        return 1
    else:
        return 0

def can_be_seen(x,y, asts, cutoff=None):
    if cutoff is None:
        cutoff = 0

    if (x,y) not in asts:
        return 0

    see = set(asts)
    see.remove((x,y))
    bdist = sorted(list(asts), key=lambda p: math.sqrt((p[0]-x)**2 + (p[1]-y)**2))

    for (cx,cy) in bdist:
        if (cx,cy) not in see:
            continue

        dx, dy = cx-x, cy-y
        sdx, sdy = sign(dx), sign(dy)
        for kx, ky in see - set([(cx,cy)]):
            lx, ly = kx-x, ky-y
            if (dx*ly == dy*lx) and sdx == sign(lx) and sdy == sign(ly):
                see.remove((kx, ky))
                if len(see) < cutoff:
                    return set()

    return see


# Read in input
mx = 0
asts = set()
for y, line in enumerate(fileinput.input()):
    mx = max(mx, len(line.strip()))
    asts.update([(x,-y) for (x,c) in enumerate(line.strip()) if c == "#"])

# Center of drawing for speed
cen_x = mx / 2
cen_y = y / 2

# Sorted by distance to middle, to eliminate most quickly
bdist = sorted(list(asts), key=lambda p: math.sqrt((p[0]-cen_x)**2 + (p[1]-cen_y)**2))

bx, by, bs = 0, 0, 0
for x, y in bdist:
    s = len(can_be_seen(x, y, asts, cutoff=bs))
    if s > bs:
        bx, by, bs = x, y, s

print("({},{}): {}".format(bx,by,bs))
