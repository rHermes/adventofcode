import fileinput as fi
import re
import collections

dirs = {"e": 2+0j, "se": 1-1j, "sw": -1-1j, "w": -2+0j, "nw": -1+1j, "ne": 1+1j}
seen = set()
for line in fi.input():
    seen ^= {sum(dirs[x] for x in re.findall("e|se|sw|w|nw|ne", line))}

dd = collections.defaultdict(int)
for _ in range(100):
    dd.clear()
    for tile in seen:
        for d in dirs.values():
            dd[tile+d] += 1

    good = set()
    for tile, v in dd.items():
        if v <= 2 and (tile in seen or v == 2):
            good.add(tile)

    seen = good

print(len(seen))
