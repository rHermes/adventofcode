import fileinput as fi

def solve(ins, N):
    a = ins[:]
    b = a[:]

    ans = 0
    for _ in range(N):
        ans += sum(not x for x in a)
        b[0], b[-1] = a[1], a[-2]

        for i in range(1, len(a)-1):
            b[i] = a[i-1] ^ a[i+1]

        a, b = b, a

    return ans


ins = ['^' == x for x in next(fi.input()).rstrip()]
print(solve(ins, 40))
