import fileinput as fi
from collections import defaultdict


guards = defaultdict(list)
guard = None
start = None
for line in sorted(map(str.strip,fi.input())):
    if line[25] == '#':
        guard = int(line[26:-13])
    elif line[19] == "f":
        start = int(line[15:17])
    elif line[19] == "w":
        end = int(line[15:17])
        guards[guard].append((start, end))

max_sleeps = 0
ans = 0
for guard, sleeps in guards.items():
    minutes = [0 for _ in range(60)]
    for s,e in sleeps:
        for i in range(s,e):
            minutes[i] += 1

    minute, val = max(enumerate(minutes), key=lambda p: p[1])
    if max_sleeps < val:
        max_sleeps = val
        ans = minute*guard

print(ans)
