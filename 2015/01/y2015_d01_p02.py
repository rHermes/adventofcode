import fileinput

def solve(s):
    ans = 0
    for i, x in enumerate(s, start=1):
        ans += {"(": 1, ")": -1}[x]
        
        if ans < 0:
            return i

test_cases = [(")", 1), ("()())", 5)]
for (x,ans) in test_cases:
    assert(solve(x) == ans)


ans = 0
for line in fileinput.input():
    ans += solve(line.rstrip())

print(ans)
