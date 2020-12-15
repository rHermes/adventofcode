import fileinput as fi

def solve(init, N):
    spoken = {k: v for (v,k) in enumerate(init)}
    last = init[-1]
    for i in range(len(init),N):
        spoken[last], last = i-1, i-1 - spoken.get(last, i-1)

    return last

numbers = [int(x) for x in next(fi.input()).split(",")]
print(solve(numbers, 30000000))
