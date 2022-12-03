import fileinput as fi
import more_itertools as mit


# Input parsing
lines = map(str.rstrip, fi.input())
groups = mit.split_at(lines, lambda x: not x)
print(max(sum(map(int,group)) for group in groups))
