import fileinput as fi
import itertools as it
import re
import collections

# Input parsing
INPUT = "".join(fi.input()).rstrip()
groups = INPUT.split("\n\n")
lines = list(INPUT.splitlines())
numbers = [list(map(int, re.findall("[0-9]+", line))) for line in lines]


def get_dims(pts):
    vl = list(pts.keys())
    # WE figure out the dimensions
    min_x = vl[0][0]
    max_x = min_x
    min_y = vl[0][1]
    max_y = min_y

    for x, y in vl[1:]:
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)

    return ((min_x, min_y), (max_x, max_y))

# Print part of the screen, from, a, b
def print_screen(pts, a, b):
    (min_x, min_y) = a
    (max_x, max_y) = b
    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            if (x,y) in pts:
                print("{}".format(pts[(x,y)]), end="")
            else:
                print(".", end="")
        print("")

def print_whole_screen(pts):
    (min_x, min_y), (max_x, max_y) = get_dims(pts)
    print_screen(pts, (min_x-1, min_y-1), (max_x+1, max_y+1))

def closest(pts, x, y, printer=False):
    lowest_dist = 9999999999999999999999999
    lowest_nm = []
    for (px, py), nm in pts.items():
        d = abs(px - x) + abs(py - y)
        if d < lowest_dist:
            lowest_dist = d
            lowest_nm = [nm]
        elif d == lowest_dist:
            lowest_nm.append(nm)

    if len(lowest_nm) != 1:
        return "."
    else:
        nm = lowest_nm[0]
        if lowest_dist == 0 and printer:
            return nm.upper()
        else:
            return nm.lower()


# return all we need to know
def precomp(pts, printer=False):
    (min_x, min_y), (max_x, max_y) = get_dims(pts)
    offset = 1
    screen = []
    for y in range(min_y-offset, max_y+offset+1):
        row = []
        for x in range(min_x-offset, max_x+offset+1):
            row.append(closest(pts, x, y, printer=printer))
        screen.append(row)

    return screen
    

def get_infs(screen):
    infs = set()

    infs.update(screen[0])
    infs.update(screen[-1])
    infs.update([r[0] for r in screen])
    infs.update([r[-1] for r in screen])

    return infs


def solve(pts):
    dims = get_dims(pts)
    # print(dims)
    w = dims[1][0] - dims[0][0] 
    h = dims[1][1] - dims[0][1] 
    # print("X: {}, Y: {}, Area: {}".format(w, h, w*h))

    # pscreen = precomp(pts, printer=True)
    screen = precomp(pts, printer=False)
    infs = get_infs(screen)

    # for row in pscreen:
    #     print("".join(row))

    wc = collections.Counter(it.chain.from_iterable(screen))

    for k in infs:
        del wc[k]

    return wc.most_common(1)[0][1]




pts = {tuple(x): str(y) for x, y in zip(numbers, it.count())}
# solve(pts)
print(solve(pts))
