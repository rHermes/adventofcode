import fileinput as fi

def solve(s, n=256):
    xs = [0 for _ in range(9)]
    for x in s:
        xs[x] += 1

    for i in range(n):
        y = xs[0]
        xs[:8] = xs[1:]
        xs[8] = y
        xs[6] += y

    return sum(xs)

nums = map(int, next(fi.input()).split(","))
print(solve(nums))
