# Ok, so learned a lot from redoing this. I also learned how to do this on
# a stream, so it's a one pass algorithm. The idea is that I allocate an
# array of N members, and an array of C(N,2) elements, where C(n,r) is
# the combinations function.
#
# I use the N number array to store the N previous numbers nad the
# other array to store the sums. When a new number comes, I check if
# it's in the sums array and if not, we are done.
#
# If it's in the sums array, we need to replace the oldest number in
# the numbers array, which is done in a rolling manner, by using modulus
# on a running counter.
#
# The tricky bit is recomputing the sums array. We want to do as few
# memory operations as possible as storing in memory is slow. Luckly
# for us, we can calculate which spots in the numbers array affect
# which spots in the sums array.
#
# I did the math for calculating this myself and I'm not sure it's
# the best. I don't have a good way to explain it but I'll outline
# the idea.
#
# We assume that the sums array goes like this, given that the contests
# are indexes of the numbers to sum from the numbers array
#
# [(0,1), (0,2), ..., (0,N-1), (1,2), (1,3), ..., (N-3,N-1), (N-2, N-1)]
#
# We mentally split this list into sections, where the section is
# decided by the first number in the tuple. When we change a number
# in the numbers array, we need to change all tuples who have that
# index in it. If we change index k, then we will have to change 1
# number in all sections smaller than k and all the tuples in section
# k.
#
# The reasons for this is that all the sections before k, will have
# one entry where the section index is combined with k. All entries
# in section k contains k, per definition. All sections after k,
# cannot contain k, as it's already been covered by entries in the
# k section. If this is is hard to grasp, try writing out the
# sums array for a small N, and put each section on it's own row.
# The pattern will emerge :)
#
# Now that we have the plan clear, we need to know a few things about
# the secions. We need to be able to select them and find items in
# them. To do this, we need to know where each section starts.
#
# The length of each section is one less than the previous and
# the first section is N-1 long. This means the second section
# is ((N-1)-1) long and starts at (N-1)-1, because we zero index.
#
# The length of section i is therfor N-1-i
#
# We define function S(n) as:
#
# S(n) = 1 + 2 + ... + N.
#
# This can also be written as:
#
# S(n) = (n*(n+1))/2
#
# Section i then starts on S(N-1) - S(N-1 - i)
#
# If you did the exercise over with printing out the sums array, you will
# see that the numbers element with index k, in section i, is offset
# k - i - 1, the 1 is because we zero index.
#
# Now we have all the components to find the indexes in the sums array
# that need to be updated when we change out a number in the numbers array.
import fileinput
import itertools as it

def S(n):
    return (n*(n+1))//2

N = 25
# Precompute this as we will use it many times
N1 = N-1
SN1 = S(N1)

# Create generator to read from list
g = (int(x) for x in fileinput.input() if x.rstrip())

# Create list of numbers and sum
nums = list(it.islice(g, N))
sums = list(map(sum,it.combinations(nums,2)))

for (i, x) in enumerate(g):
    if x not in sums:
        print(x)
        break

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
