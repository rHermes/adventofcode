import fileinput as fi
import re

pats = [
    r"([a-z]{2}).*\1",
    r"([a-z]).\1",
]

ans = 0
for line in fi.input():
    ans += all(re.search(pat, line) for pat in pats)

print(ans)
