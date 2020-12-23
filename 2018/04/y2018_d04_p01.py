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


sleepy = {guard: sum(e-s for s,e in sleeps) for guard, sleeps in guards.items()}
guard = max(sleepy, key=sleepy.get)
minutes = [0 for _ in range(60)]
for s,e in guards[guard]:
    for i in range(s,e):
        minutes[i] += 1

minute, val = max(enumerate(minutes), key=lambda p: p[1])

print(minute*guard)
