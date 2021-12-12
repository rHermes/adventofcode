import fileinput as fi

def solve(s: str) -> int:
    w = [3, 7]
    cur = "37"
    a, b = 0, 1
    while True:
        kw = cur.find(s, -len(s)-1)
        if kw != -1:
            return kw

        c = w[a] + w[b]
        digits = [int(x) for x in str(c)]
        w.extend(digits)
        cur += str(c)
        a = (a + w[a] + 1) % len(w)
        b = (b + w[b] + 1) % len(w)

print(solve(next(fi.input()).rstrip()))
