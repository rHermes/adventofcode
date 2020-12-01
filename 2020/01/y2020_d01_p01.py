import fileinput


def solve(nums, target, N):
    for i, x in enumerate(nums, 1):
        nt = target - x
        if nt == 0 and N == 1:
            return x
        elif nt > 0 and N > 1:
            nx = solve(nums[i:], nt, N-1)
            if nx:
                return x * nx

nums = [int(line.rstrip()) for line in fileinput.input()]
print(solve(nums, 2020, 2))
