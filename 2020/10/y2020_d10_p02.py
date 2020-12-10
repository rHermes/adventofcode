import fileinput as fi

nums = frozenset([int(x) for x in fi.input() if x.rstrip()])

# We rely on the cache for terminating, makes the code a bit shorter.
def solver(nums, cur, cache):
    if cur in cache:
        return cache[cur]

    ans = 0
    for y in range(1,4):
        if cur + y in nums:
            ans += solver(nums, cur + y, cache)

    cache[cur] = ans
    return ans


print(solver(nums, 0, {max(nums): 1}))
