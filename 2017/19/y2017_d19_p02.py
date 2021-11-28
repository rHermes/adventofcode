import fileinput as fi

dirs = {
    "n": (0, -1),
    "e": (1, 0),
    "s": (0, 1),
    "w": (-1, 0)
}

anti = {"n": "s", "e": "w", "s": "n", "w": "e"}

def find_start(lines):
    x, y = 0, 0
    while lines[y][x] != '|':
        x += 1

    return (x,y)


def solve(lines, pt):
    x, y = pt
    d = 's'
    ans = 0
    while lines[y][x] != ' ':
        if lines[y][x] == '+':
            for nd in "nesw":
                if nd == anti[d]:
                    continue

                gx, gy = dirs[nd]
                if lines[y + gy][x + gx] != ' ':
                    d = nd
                    break
            else:
                print("WTF")

        dx, dy = dirs[d]
        x, y = x + dx, y + dy
        ans += 1

    return ans

# Input parsing
lines = list("".join(fi.input()).rstrip("\n").splitlines())

x, y = find_start(lines)
print(solve(lines, (x,y)))
