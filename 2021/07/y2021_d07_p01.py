import fileinput as fi
import statistics as st

# https://en.wikipedia.org/wiki/Median#Optimality_property
def solve(nums):
    x = st.median_low(nums)
    return sum(abs(x - n) for n in nums)

print(solve([int(x) for x in next(fi.input()).split(",")]))
