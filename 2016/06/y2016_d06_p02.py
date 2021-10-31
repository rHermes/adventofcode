import fileinput as fi
import collections

INPUT = "".join(fi.input()).rstrip()
lines = list(INPUT.splitlines())

cols = [collections.Counter() for _ in lines[0]]
for line in lines:
    for cnt, k in zip(cols, line):
        cnt[k] += 1

ans = "".join(c.most_common()[-1][0] for c in cols)
print(ans)
