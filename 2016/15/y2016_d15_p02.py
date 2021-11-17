import fileinput as fi
import re

discs = []
for line in fi.input():
    m = re.match("Disc #(\d+) has (\d+) positions; at time=(\d+), it is at position (\d+).", line)
    if m:
        discs.append(tuple(map(int,m.groups())))

discs.append((len(discs)+1, 11, 0, 0))

period = 1
time = 0
for (disc, npos, stime, spos) in discs:
    while (time + disc + spos) % (npos) != 0:
        time += period

    period *= npos

print(time)
