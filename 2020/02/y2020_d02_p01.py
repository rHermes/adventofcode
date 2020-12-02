import fileinput
import re

ans = 0
for line in fileinput.input():
    mth = re.match("([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)", line).groups()
    low = int(mth[0])
    hi = int(mth[1])

    cnt = 0
    for k in mth[3]:
        if k == mth[2]:
            cnt += 1

    if low <= cnt and cnt <= hi:
        ans += 1

print(ans)
