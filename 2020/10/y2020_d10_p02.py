import fileinput as fi
import itertools as it

# findall, parse, search, with_pattern
from parse import *

import more_itertools as mit


ins = []
for line in fi.input():
    if line.rstrip():
        ins.append(line.rstrip())

nums = [int(x) for x in ins]
nums.append(max(nums)+3)


# Quick notes:
# - did a simple mistake on part 2 with not setting caching, but rather reutnring current
# - Did a mistake on part one where  I didn't break a loop.
# - Spent way to long understanding the task
# - Today was an all around fuck fest

# FUKKKKKK
def solver(nums, end, cur, cache):
    if cur in cache:
        return cache[cur]

    if cur == end:
        cache[end] = 1
        return 1

    ans = 0
    for y in range(1,4):
        if cur + y in nums:
            ans += solver(nums, end, cur + y, cache)
    
    cache[cur] = ans
    return ans
        

cache = {}
ans = solver(frozenset(nums), max(nums), 0, cache)
print(ans)
