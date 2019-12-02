import fileinput

def solve(s):
    s = s + s[0]
    ans = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            ans += int(s[i])

    return ans

test_cases = [("1122", 3), ("1111", 4), ("1234", 0), ("91212129", 9)]
for t, e in test_cases:
    assert(solve(t) == e)

ans = 0
for line in fileinput.input():
    ans += solve(line.rstrip())

print(ans)
