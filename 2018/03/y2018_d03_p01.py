import fileinput


mem = {}
for line in fileinput.input():
    parts = line.rstrip().split(" ")
    ids = int(parts[0][1:])
    x, y = [int(k) for k in parts[2][:-1].split(",")]
    w, h = [int(k) for k in parts[3].split("x")]

    for i in range(w):
        for j in range(h):
            cx = x + i
            cy = y + j

            mem[(cx,cy)] = mem.get((cx,cy), 0) + 1

over = [(k,v) for k, v in mem.items() if v > 1]

print(len(over))
