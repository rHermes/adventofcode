import fileinput as fi
import more_itertools as mit
import heapq

# Input parsing
lines = map(str.rstrip, fi.input())

# Grouping
groups = mit.split_at(lines, lambda x: not x)

# Getting the number of calories
numbers = (sum(map(int,group)) for group in groups)

print(sum(heapq.nlargest(3, numbers)))
