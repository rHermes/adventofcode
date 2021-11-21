import fileinput as fi
import intervaltree as itree

# Input parsing
INPUT = "".join(fi.input()).rstrip()
groups = INPUT.split("\n\n")
lines = list(INPUT.splitlines())

# state = set(range(0,10))
tree = itree.IntervalTree([itree.Interval(0, 4294967295)])
for line in lines:
    a, b = line.split("-")
    tree.chop(int(a), int(b)+1)

print(sum(x.length() for x in tree))
