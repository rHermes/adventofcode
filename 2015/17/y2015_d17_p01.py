import fileinput as fi
import itertools as it

# from more_itertools there is the `powerset` function which would have made
# this almost a oneliner.
# import more_itertools as mit

nums = [int(x) for x in fi.input() if x.strip()]

ans = 0
for i in range(len(nums)):
    for co in it.combinations(nums, r=i):
        if sum(co) == 150:
            ans += 1

print(ans)
