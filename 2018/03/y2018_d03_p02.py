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

            if (cx, cy) not in mem:
                mem[(cx,cy)] = []

            mem[(cx,cy)].append(ids)

all_ids = set()
over_ids = set()

for k, v in mem.items():
    for c in v:
        all_ids.add(c)

    if len(v) > 1:
        for c in v:
            over_ids.add(c)


print(list(all_ids - over_ids)[0])
