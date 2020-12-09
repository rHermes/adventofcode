# Idea here is to keep just 2 variables going:
#
# - the list of the current items.
# - the current sum
#
# Update these as new inputs come in. If the new item
# makes the sum to large, remove elements at the end until
# its within range. If it's perfect, we are done. If not, we continue reading.
import fileinput
import itertools as it
from collections import deque

def solve_part1(stream, N=25):
    # Use deque to make popping and so on faster
    nums = deque(it.islice(stream, N), N)
    for x in stream:
        s = frozenset(nums)
        if not any(x - y in s for y in s if x - y != y):
            return x

        nums.append(x)

lines = [int(x) for x in fileinput.input() if x.rstrip()]

TARGET = solve_part1(iter(lines))

s = 0
span = deque()
for x in lines:
    s += x
    span.append(x)
    while s > TARGET:
        s -= span.popleft()
        
    if s == TARGET:
        print(min(span) + max(span))
        break
