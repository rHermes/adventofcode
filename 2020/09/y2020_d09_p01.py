# The written solution is O(n*d) where d is the
# number of items. Look in the commit log for my own
# old solution
import fileinput
import itertools as it
from collections import deque

def solve(stream, N=25):
    # Use deque to make popping and so on faster
    nums = deque(it.islice(stream, N), N)
    for x in stream:
        s = frozenset(nums)
        if not any(x - y in s for y in s if x - y != y):
            return x

        nums.append(x)

# Create generator to read from list
print(solve(int(x) for x in fileinput.input()))
