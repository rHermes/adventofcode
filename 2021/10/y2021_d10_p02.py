import fileinput as fi
from statistics import median

points = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

tbl = {
    "<": ">",
    "[": "]",
    "(": ")",
    "{": "}"
}

scores = []
for line in map(str.rstrip, fi.input()):
    stack = []
    for c in line:
        if c in tbl:
            stack.append(tbl[c])
        elif c == stack[-1]:
            stack.pop()
        else:
            break
    else:
        score = 0
        for c in reversed(stack):
            score *= 5
            score += points[c]

        scores.append(score)

print(median(scores))
