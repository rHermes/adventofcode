import fileinput as fi
import intervaltree as itree

tree = itree.IntervalTree([itree.Interval(0, 4294967295+1)])
for line in fi.input():
    a, b = line.split("-")
    tree.chop(int(a), int(b)+1)

# We want to merge all intervals into one.
tree.merge_overlaps(strict=False)
print(sum(x.length() for x in tree))
