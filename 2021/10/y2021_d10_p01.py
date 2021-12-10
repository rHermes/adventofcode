import fileinput as fi

points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

tbl = {
    "<": ">",
    "[": "]",
    "(": ")",
    "{": "}"
}

ans = 0
for line in map(str.rstrip, fi.input()):
    stack = []
    for c in line:
        if c in tbl:
            stack.append(tbl[c])
        elif c == stack[-1]:
            stack.pop()
        else:
            ans += points[c]
            break

print(ans)
