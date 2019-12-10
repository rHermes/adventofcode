import fileinput
import math



def can_be_seen(x,y, asts):
    if (x,y) not in asts:
        return 0

    see = set(asts)
    see.remove((x,y))
    bdist = sorted(list(asts), key=lambda p: math.sqrt((p[0]-x)**2 + (p[1]-y)**2))

    for (cx,cy) in bdist:
        if (cx,cy) not in see:
            continue

        dx, dy = (cx-x, cy-y)

        # This can be prime factor but for now we are not doing that
        for kx, ky in see - set([(cx,cy)]):
            lx, ly = (kx-x, ky-y)
            
            # We must check if lx, ly is a multiple of dx,dy. We could primefactor
            # but not doing that 
            remove = False
            if dx == 0:
                if lx == 0 and (ly / dy > 0):
                    remove = True
            elif dy == 0:
                if ly == 0 and (lx / dx > 0):
                    remove = True
            else:
                if ((lx / dx) == (ly / dy)) and (lx / dx) > 0:
                    remove = True

            if remove:
                # print(("At ({},{}) does ({},{}) block ({}, {}): ({},{}) vs ({},{})".format(x,y, cx, cy, kx, ky, dx, dy, lx, ly)))
                see.remove((kx, ky))


    return(len(see))


asts = set()

for y, line in enumerate(fileinput.input()):
    asts.update([(x,y) for (x,c) in enumerate(line.strip()) if c == "#"])


pos = [(x,y,can_be_seen(x,y,asts)) for (x,y) in asts]

bx,by,bs = max(pos, key=lambda p: p[2])

print("({},{}): {}".format(bx,by,bs))

#for (x,y) in asts:
#    ss = can_be_seen(x,y,asts)
#    print("From ({},{}): We can see {}".format(x,y,ss))
# ss = can_be_seen(3,4,asts)
# print("From ({},{}): We can see {}".format(3,4,ss))

