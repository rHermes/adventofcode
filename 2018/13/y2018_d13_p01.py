import fileinput as fi

# The dy, dx pairs for each direction.
DIR = {"^": (-1,0), "v": (1,0), ">": (0,1), "<": (0,-1)}

# Corner handling
NDIR = {
    '\\': { "^": "<", ">": "v", "v": ">", "<": "^"},
    '/': { "^": ">", ">": "^", "v": "<", "<": "v" },
    "|": {"^": "^", "v": "v"},
    "-": {"<": "<", ">": ">"},
}

TURN = {
    "^": "<>",
    ">": "^v",
    "v": "><",
    "<": "v^",
}

lines = list(fi.input())

# Read the carts from
carts = []
seen = set()
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c in "^v<>":
            carts.append((y,x,0,c))
            seen.add((y,x))

# Remove the carts from the board
for y,x, _, c in carts:
    wl = list(lines[y])
    wl[x] = "-|"[c in "^v"]
    lines[y] = "".join(wl)


done = False
while not done:
    carts = sorted(carts)
    for i in range(len(carts)):
        y, x, gen, c = carts[i]

        if lines[y][x] in NDIR:
            c = NDIR[lines[y][x]][c]
        else:
            if gen == 0:
                c = TURN[c][0]
            elif gen == 2:
                c = TURN[c][1]

            gen = (gen+1) % 3

        seen.remove((y,x))
        dy, dx = DIR[c]
        y += dy
        x += dx

        if (y,x) in seen:
            print("{},{}".format(x,y))
            done = True
            break
        else:
            seen.add((y,x))

        carts[i] = (y,x,gen,c)
