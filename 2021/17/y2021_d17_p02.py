import fileinput as fi

# Returns the final position of x, given a high y.
def final_x(x0, dx):
    return x0 + ((dx * (dx + 1))//2)

# Returns the y positon at t with initial velocity dy
def y_at(dy, t):
    return -(t * (t - 1 - 2*dy)) // 2

# We create a bound on the valid xmin, xmax
def find_valid_xs(xmin, xmax):
    valid = set()
    for dx in range(0, xmax+1):
        if final_x(0, dx) < xmin:
            continue

        x = 0
        ndx = dx
        while x <= xmax:
            if xmin <= x:
                break

            x += ndx
            ndx -= 1
        else:
            continue

        valid.add(dx)

    return valid


def step(x,y, dx, dy):
    if 0 < dx:
        ndx = dx-1
    else:
        ndx = dx

    return (x+dx, y+dy,ndx, dy-1)

# Retuns if the shot would have gone in and if it's worth trying to
# change y
def try_vec(xmin,xmax,ymin,ymax, dx, dy):
    x, y = 0, 0
    max_y = 0
    found = False
    while ymin <= y and x <= xmax:
        # We will never hit now, might as well just break it of
        # We will also never hit the target, as giving us more hight
        # will not lead to us getting father.
        if dx == 0 and x < xmin:
            return False, True

        if ymin <= y <= ymax and xmin <= x <= xmax:
            return True, False
        else:
            x, y, dx, dy = step(x, y, dx, dy)

    return False, (xmax < x and ymax < y)


def solve(xmin,xmax,ymin,ymax):
    assert(xmin <= xmax and ymin <= ymax)

    # We assert that x can only be positive. This is reasonable, given the puzzle text.
    assert(0 <= xmin)
    # We also assume that y is always below us. This is reasonable, given the puzzle text.
    assert(ymax <= 0)

    ans = 0
    gav = find_valid_xs(xmin,xmax)
    for dx in gav:
        # We cannot actually solve this generally, so we have to guess at the max y
        for dy in range(ymin, 1000):
            hit, stop_it = try_vec(xmin,xmax,ymin,ymax,dx,dy)
            if hit:
                ans += 1

            if stop_it:
                break

    return ans


# y equation, where m is the initial vector: y_m(t) = - (t * (t - 1 - 2*m)) // 2

line = next(fi.input()).rstrip()
parts = line.split()
xmin, xmax = map(int,parts[2][2:-1].split(".."))
ymin, ymax = map(int,parts[3][2:].split(".."))

print(solve(xmin,xmax,ymin,ymax))
