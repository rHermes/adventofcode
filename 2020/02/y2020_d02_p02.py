import fileinput
import re

ans = 0
for line in fileinput.input():
    lo, hi, c, pwd = re.match("^(\d+)-(\d+) ([a-z]): ([a-z]+)$", line).groups()

    if sum(pwd[int(x)-1] == c for x in (lo, hi)) == 1:
        ans += 1

print(ans)
