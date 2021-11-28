import fileinput as fi

def solve(step):
    ans = 0
    cur = 0
    for i in range(1, 50000001):
        cur = (cur + step) % i
        if cur == 0:
            ans = i
        cur += 1

    return ans

print(solve(int(next(fi.input()).rstrip())))
