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
                see.remove((kx, ky))

    return see


asts = set()

for y, line in enumerate(fileinput.input()):
    asts.update([(x,y) for (x,c) in enumerate(line.strip()) if c == "#"])


#pos = [(x,y,can_be_seen(x,y,asts)) for (x,y) in asts]

#bx,by,bs = max(pos, key=lambda p: p[2])

#print("({},{}): {}".format(bx,by,bs))




def solve(bx, by, asts):
    i = 0
    while len(asts) > 1:
        cbs = can_be_seen(bx, by, asts)
        # Now we need to sort them by their angle
        # We convert to radians, push them by 
        fx = lambda p: ((math.atan2(by - p[1], bx - p[0]) - (math.pi/2)) % (2*math.pi)) 
        order = sorted(list(cbs), key=fx)

        for p in order:
            i += 1
            asts.remove(p)
            if i == 200:
                return p

    raise Exception("What?")


#wow = solve(11, 13, asts)
wow = solve(20, 20, asts)

print(wow[0]*100 + wow[1])



