import fileinput as fi
import statistics as st

# https://en.wikipedia.org/wiki/Arithmetic_mean#Motivating_properties
def solve(nums):
    x = int(st.fmean(nums))
    return sum((abs(x - n)*(abs(x-n) + 1)) // 2 for n in nums)

print(solve([int(x) for x in next(fi.input()).split(",")]))
