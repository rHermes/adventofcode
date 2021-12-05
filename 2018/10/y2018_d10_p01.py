import fileinput as fi
import re

def part_at(part, t):
    (x, y), (dx, dy) = part
    return (x+dx*t, y+dy*t)

def area_at(parts, t):
    minx, miny = part_at(parts[0], t)
    maxx, maxy = minx, miny

    for part in parts[1:]:
        x, y = part_at(part, t)
        minx = min(x, minx)
        maxx = max(x, maxx)
        miny = min(y, miny)
        maxy = max(y, maxy)

    return (minx, miny), (maxx, maxy)

def print_parts_at(parts, t):
    (minx,miny), (maxx,maxy) = area_at(parts, t)

    seen = set(part_at(p, t) for p in parts)
    for y in range(miny,maxy+1):
        for x in range(minx,maxx+1):
            if (x,y) in seen:
                print("█", end="")
            else:
                print(" ", end="")

        print("")


def fair_at(parts, t):
    (minx, miny), (maxx, maxy) = area_at(parts, t)
    return (maxx-minx)*(maxy-miny)


def find_moment(parts):
    # We must furst increase until we find one where it is bigger
    left = 0
    prev_fair = fair_at(parts, left)
    left = 1
    while True:
        fair = fair_at(parts, left)
        if prev_fair < fair:
            break

        prev_fair = fair
        left *= 2

    right = left
    rv = fair

    left = left // 2
    lv = prev_fair


    # Now we can test
    while left+1 != right:
        md = (left+right) // 2

        # We find the slope at this point
        fair = fair_at(parts, md)
        ff = fair_at(parts, md+1)

        if fair < ff:
            right = md
            rv = fair
        else:
            left = md
            lv = fair

    if lv < rv:
        return left
    else:
        return right



def solve(parts):
    t = find_moment(parts)
    print_parts_at(parts, t)

numbers = [list(map(int, re.findall("-?[0-9]+", line))) for line in fi.input()]
parts = [((x,y), (dx,dy)) for (x,y,dx,dy) in numbers]
solve((parts))
