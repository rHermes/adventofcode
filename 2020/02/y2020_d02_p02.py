import fileinput
import re


ans = 0
for line in fileinput.input():
    mth = re.match("([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)", line).groups()
    low = int(mth[0])
    hi = int(mth[1])

    cnt = 0
    if mth[3][low-1] == mth[2]:
        cnt += 1

    if mth[2] == mth[3][hi-1]:
        cnt += 1

    if cnt == 1:
        ans += 1

print(ans)
