import fileinput as fi

G = {}
def nways(springs, nums):
    global G

    if not springs:
        return not nums

    if not nums:
        return "#" not in springs

    if len(springs) < sum(nums):
        return 0

    sig = hash((springs, nums))
    if sig in G:
        return G[sig]

    k = len(springs) - nums[0]
    if "#" in springs:
        k = min(springs.index("#"), k)


    ans = 0
    for i in range(k+1):
        end = i+nums[0]
        if "." not in springs[i:end] and (len(springs) <= end or springs[end] != "#"):
            ans += nways(springs[end+1:], nums[1:])

    G[sig] = ans
    return ans

def solve(line):
    springs, nu = line.split()
    nums = tuple(int(x) for x in nu.split(","))
    ways = nways(springs, nums)
    return ways


ans = 0
for line in map(str.rstrip, fi.input()):
    ans += solve(line)

print(ans)
