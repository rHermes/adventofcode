import fileinput as fi
import re
import bisect

# Input parsing
INPUT = "".join(fi.input()).rstrip()
groups = INPUT.split("\n\n")

phases = []

# Prepare the 
for group in groups[1:]:
    ranges = []
    for x in list(group.splitlines())[1:]:
        target, source, length = map(int, x.split(" "))
        ranges.append((source + length - 1, source, target, length))
    
    ranges.sort()
    phases.append(ranges)

ans = 1000000000000000000000000000000
seeds = [int(x) for x in re.findall("-?[0-9]+", groups[0])]

for seed in seeds:
    cur = seed
    for phase in phases:
        i = bisect.bisect_left(phase, cur, key=lambda x: x[0])
        if i != len(phase):
            source_end, source_start, target_start, length = phase[i]
            if source_start <= cur <= source_end:
                cur = target_start + (cur - source_start)

    ans = min(ans, cur)

print(ans)
