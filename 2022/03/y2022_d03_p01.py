import fileinput as fi
import string

ans = 0
for line in filter(bool, map(str.rstrip, fi.input())):
    n = len(line)//2
    c = set(line[:n]) & set(line[n:])
    ans += sum(string.ascii_letters.index(x) + 1 for x in c)

print(ans)
