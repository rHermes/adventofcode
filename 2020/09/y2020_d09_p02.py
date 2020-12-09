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

def S(n):
    return (n*(n+1))//2

def part1(lines):
    N = 25
    # Precompute this as we will use it many times
    N1 = N-1
    SN1 = S(N1)

    # Create generator to read from list

    # Create list of numbers and sum
    nums = lines[:N]
    sums = list(map(sum,it.combinations(nums,2)))

    for (i, x) in enumerate(lines[N:]):
        if x not in sums:
            return x

        yi = i % N
        # Here we we select the number up to this point
        for sec in range(yi):
            sec_start = SN1 - S(N1 - sec)
            offset = yi - sec - 1
            sums[sec_start + offset] = nums[sec] + x

        sec_start = SN1 - S(N1 - yi)
        for (ik, k) in enumerate(range(sec_start,sec_start+(N1-yi)),yi+1):
            sums[k] = x + nums[ik]

        nums[yi] = x


lines = [int(x) for x in fileinput.input() if x.rstrip()]

TARGET = part1(lines)

s = 0
span = []
for x in lines:
    s += x
    span.append(x)
    while s > TARGET:
        s -= span.pop(0)
        
    if s == TARGET:
        print(min(span) + max(span))
        break
