import fileinput as fi
import re


# There is actually no need for merging in the puzzle input, but I'm keeping
# this here, since it could drastically cut down compute time for other inputs
def merge_ranges(x: list[tuple[int,int]]):
    """The ranges have to be sorted"""
    i = 0
    while i < len(x)-1:
        fs, fe = x[i]
        ss, se = x[i+1]
        if ss < fe:
            x.pop(0)
            x[0] = (fs, max(fe, se))
        else:
            i += 1

# Input parsing
INPUT = "".join(fi.input()).rstrip()
groups = INPUT.split("\n\n")

# We store all mappings as [start,end)
phases = []
for group in groups[1:]:
    ranges = []
    for x in list(group.splitlines())[1:]:
        target, source, length = map(int, x.split(" "))
        ranges.append((source, source + length, target))
    
    ranges.sort()
    phases.append(ranges)

# Create the initial items
cur_ranges = []
seeds = [int(x) for x in re.findall("-?[0-9]+", groups[0])]
i = 0
while i < len(seeds):
    start, length = seeds[i], seeds[i+1]
    i += 2
    cur_ranges.append((start, start + length))

cur_ranges.sort()
merge_ranges(cur_ranges)

for phase in phases:
    # We have to go over ranges each time.
    ranges_left = list(cur_ranges)
    next_ranges = []

    while ranges_left:
        rs, re = ranges_left.pop(0)

        for (start, end, target) in phase:
            if not (start < re and rs < end):
                continue
            
            # If the start is not covered, we add it to the next_ranges, as we are not covered
            if rs < start:
                next_ranges.append((rs, start))
            
            gs = max(rs, start)
            ge = min(re, end)
            next_ranges.append((gs - start + target, ge - start + target))

            if end < re:
                ranges_left.append((end, re))
            
            print("we restart")
            break
        else:
            next_ranges.append((rs, re))
    
    next_ranges.sort()
    merge_ranges(next_ranges)

    cur_ranges = next_ranges
        
print(cur_ranges[0][0])
