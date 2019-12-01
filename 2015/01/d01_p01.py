import fileinput

def solve(s):
    return sum([{"(": 1, ")": -1}[x] for x in s])

test_cases = [("(())", 0)]
for (x,ans) in test_cases:
    assert(solve(x) == ans)


ans = 0
for line in fileinput.input():
    ans += solve(line.rstrip())

print(ans)
