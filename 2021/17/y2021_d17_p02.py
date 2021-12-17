import fileinput as fi

# Returns the final position of x, given a high y.
def final_x(x0, dx):
    return x0 + ((dx * (dx + 1))//2)

# Returns the y positon at t with initial velocity dy
def y_at(dy, t):
    return -(t * (t - 1 - 2*dy)) // 2

# A single step
def step(x, y, dx, dy):
    return (x+dx, y+dy, max(0, dx-1), dy-1)

# Retuns if the shot would have gone in and if it's worth trying to
# change y
def try_vec(xmin,xmax,ymin,ymax, dx, dy):
    x, y = 0, 0
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
    # We assert that he ship is always below and to the right of us. This is reasonable
    # given the puzzles text.
    assert(0 <= xmin and ymax <= 0)

    ans = 0
    for dx in range(xmax+1):
        if final_x(0, dx) < xmin:
            continue

        for dy in range(ymin, -ymin+1):
            hit, stop_it = try_vec(xmin,xmax,ymin,ymax,dx,dy)
            if hit:
                ans += 1

            if stop_it:
                break

    return ans


line = next(fi.input()).rstrip()
parts = line.split()
xmin, xmax = map(int,parts[2][2:-1].split(".."))
ymin, ymax = map(int,parts[3][2:].split(".."))

print(solve(xmin,xmax,ymin,ymax))
