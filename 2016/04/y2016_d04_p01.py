import collections
import fileinput as fi
import functools as ft
import re
import string

ans = 0
for line in fi.input():
    m  = re.match(r"(.*)-([0-9]+)\[(.*)\]", line)
    if not m:
        continue

    name, sid, ch = m.groups()

    c = collections.Counter(sorted(name.replace("-", "")))
    check = "".join(x for x, _ in c.most_common(5))

    if check == ch:
        ans += int(sid)

print(ans)
