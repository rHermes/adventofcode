import fileinput

# This could be optimized, to only loop through half the list and then multiply by 2,
# but I'm to lazy to do so
def solve(s):
    off = len(s) // 2
    ans = 0
    for i in range(len(s)):
        if s[i] == s[(i+off) % len(s)]:
            ans += int(s[i])

    return ans

test_cases = [("1212", 6), ("1221", 0), ("123425", 4), ("123123", 12), ("12131415", 4)]
for t, e in test_cases:
    assert(solve(t) == e)

ans = 0
for line in fileinput.input():
    ans += solve(line.rstrip())

print(ans)
