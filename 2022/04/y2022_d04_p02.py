import fileinput as fi
import re


lines = filter(bool, map(str.rstrip, fi.input()))
s = 0
for line in lines:
    startA, endA, startB, endB = map(int,re.match(r"(\d+)-(\d+),(\d+)-(\d+)", line).groups())
    s += (startA <= endB and startB <= endA)

print(s)
