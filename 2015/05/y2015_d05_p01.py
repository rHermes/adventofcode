import fileinput as fi
import re

pats = [
    (r"(?:[aeiou].*){3}", True),
    (r"([a-z])\1", True),
    (r"(ab|cd|pq|xy)", False),
]

ans = 0
for line in fi.input():
    ans += all(bool(re.search(pat, line)) == res for pat, res in pats)

print(ans)
