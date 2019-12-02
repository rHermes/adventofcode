import fileinput
import collections


def solve(ids):
    seen = set() 
    for s in ids:
        for i in range(len(s)):
            k = s[:i] + 'Ø' + s[(i+1):]
            if k in seen:
                return s[:i] + s[(i+1):]
            else:
                seen.add(k)

ids = [line.rstrip() for line in fileinput.input()]
print(solve(ids))
