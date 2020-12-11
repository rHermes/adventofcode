# This was really brilliant! After seeing a meme on the subreddit about
# tribonacci I realized that this could be done with just 3 numbers.
import fileinput as fi

nums = sorted([int(x) for x in fi.input() if x.rstrip()])

# we use tribbonacci here
a, b, c, last = [nums[0] == x for x in [3,2,1,0]]

for x in nums:
    df, last  = x - last, x
    if df == 1:
        a, b, c = b, c, a + b + c
    elif df == 2:
        a, b, c = c, 0, a + b + c
    else:
        a, b, c = 0, 0, c

print(c)
