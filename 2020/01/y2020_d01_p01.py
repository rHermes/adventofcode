import fileinput
import itertools as it
import math

nums = [int(line.rstrip()) for line in fileinput.input()]
ans = next(filter(lambda x: sum(x) == 2020, it.combinations(nums, 2)))
print(math.prod(ans))
