import fileinput as fi
import re

dirs = {"e": 2+0j, "se": 1-1j, "sw": -1-1j, "w": -2+0j, "nw": -1+1j, "ne": 1+1j}
seen = set()
for line in fi.input():
    seen ^= {sum(dirs[x] for x in re.findall("e|se|sw|w|nw|ne", line))}

print(len(seen))
