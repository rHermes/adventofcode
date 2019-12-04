import fileinput


def solve(lo, hi):
    n = 0
    for x in range(lo, hi+1):
        y = [int(c) for c in str(x)]
        if y != sorted(y):
            continue
        
        for i in range(len(y)-1):
            if y[i] == y[i+1]:
                break
        else:
            continue
        
        n += 1

    return n


for line in fileinput.input():
    a, b = [int(x) for x in line.rstrip().split("-")]
    print(solve(a,b))
