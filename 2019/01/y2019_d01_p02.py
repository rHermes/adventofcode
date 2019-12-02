import fileinput

def solve(x):
    y = (x//3)-2
    if y <= 0:
        return 0
    else:
        return y + solve(y)

test_cases = [(14,2),(1969,966),(100756,50346)]
for (x,ans) in test_cases:
    assert(solve(x) == ans)


ans = 0
for line in fileinput.input():
    ans += solve(int(line.rstrip()))

print(ans)
