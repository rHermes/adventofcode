import fileinput

def solve(x):
    return (x//3)-2

test_cases = [(12,2),(14,2),(1969,654),(100756,33583)]
for (x,ans) in test_cases:
    assert(solve(x) == ans)


ans = 0
for line in fileinput.input():
    ans += solve(int(line.rstrip()))

print(ans)
