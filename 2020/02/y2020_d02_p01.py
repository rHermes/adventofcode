import fileinput
import re

ans = 0
for line in fileinput.input():
    lo, hi, c, pwd = re.match("^(\d+)-(\d+) ([a-z]): ([a-z]+)$", line).groups()

    if int(lo) <= sum(x == c for x in pwd) <= int(hi):
        ans += 1

print(ans)
