import fileinput as fi

def solve(n: int) -> str:
    w = [3, 7]
    a, b = 0, 1

    while len(w) < n+10:
        c = w[a] + w[b]
        w.extend(divmod(c, 10) if c >= 10 else (c,))
        a = (a + w[a] + 1) % len(w)
        b = (b + w[b] + 1) % len(w)

    lop = []
    for j in range(n,n+10):
        lop.append(str(w[j % len(w)]))

    return "".join(lop)

print(solve(int(next(fi.input()))))
