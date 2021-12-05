import fileinput as fi

def solve(lines):
    seen = set()
    twice = set()

    for line in lines:
        (x1,y1), (x2,y2) = sorted([list(map(int, p.split(","))) for p in line.split(" -> ")])

        if x1 == x2:
            g = ((x1,y) for y in range(min(y1,y2), max(y1,y2)+1))
        elif y1 == y2:
            g = ((x,y1) for x in range(x1, x2+1))
        else:
            g = []

        for p in g:
            if p in seen:
                twice.add(p)
            else:
                seen.add(p)


    return len(twice)

print(solve(fi.input()))
